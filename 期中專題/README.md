# Python機器學習入門 - 期中專題
透過Scrapy抓取1111及104的資料
## 一、安裝Scrapy
首先，在指定的目錄下，輸入：
```
pip install scrapy
```
也能使用
```
conda install -c conda-forge scrapy=1.3.0
```
就能安裝Scrapy。
## 二、建立Scrapy專案
安裝好後，我們就可以開始使用Scrapy的框架，下指令：
```
scrapy startproject soft_jobs(項目名稱)
```
我取名為soft_jobs的原因是這個項目就是用來做軟體工作的爬蟲，
接著會看到，目錄下出現了：
![](https://i.imgur.com/exob3rj.png)
代表已經建立專案成功囉！
## 三、創建第一隻爬蟲
專案創好後，我們就能開始實現爬蟲了，首先要建立第一支爬蟲：
```
scrapy genspider [爬蟲名稱] [網域]
```
創立好後，就會在spider的目錄下，看到已經有基本配備出現：
![](https://i.imgur.com/AfkZiTt.png)
名稱與網域都已經設定好，接著就是開始開發了。

## 四、開始開發
### （一）設定items.py
在items.py中可以設定公共模板資料，我設定了四個：
*	job_title
*	job_salary
*	job_company
*	job_date
```python=
import scrapy

class SoftJobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    job_salary = scrapy.Field()
    job_company = scrapy.Field()
    job_date = scrapy.Field()
    pass

```
### (二) 設定pipline
設定pipline，可以最後統一處理資料
```python=
class SoftJobsPipeline(object):
    def process_item(self, item, spider):
		# 這邊統一把資料print出來
        print(item)
        return item
```
### (三) 撰寫主要程式碼
#### 第一部分 - 104.com
```python3
import scrapy
import time
import json
# 這邊是將item的資料引入進來，之後就能以item["job_company"]...直接使用
from soft_jobs.items import SoftJobsItem
from scrapy import Request

class YuratorSpider(scrapy.Spider):
    name = 'yurator'
    allowed_domains = ['104.com']
	# 這邊是程式起始的url，也就是説會從這一個網站開始爬
    start_urls = [
        'https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=11&asc=0&page=0'
    ]
	# parse函數是必備的，用來處理response資料
    def parse(self, response):
        div_list = response.xpath("//div[@id='js-job-content']/article")
        for div in div_list:
            item = SoftJobsItem()
	     # 找到公司的html後，將其分析並輸入到company
            job_company= div.xpath("./div[@class='b-block__left']/ul[@class='b-list-inline b-clearfix']/li[2]/a/text()").extract()
            # 去除前後空白
            item["job_company"] = job_company[0].strip()
            date = div.xpath("./div[@class='b-block__left']/h2[@class='b-tit']/span/text()")[0].extract()
            item["job_salary"] = div.xpath("./div[@class='b-block__left']/div[@class='job-list-tag b-content']/span/text()")[0].extract()
            item["job_date"] = date.strip()
            item["job_title"] = div.xpath("./div[@class='b-block__left']/h2[@class='b-tit']/a/text()")[0].extract()
            # item["job_company"] = tr.xpath("./td[5]/text()").extract_first()
            yield item
	# 這邊是用來爬1~100頁的資訊
        i = 0
        while i <= 100:
            next_url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=11&asc=0&page="+str(i)+"&mode=s"
            i = i + 1
            yield Request(next_url , callback=self.parse,dont_filter=True)
```
說明上述程式碼，主要就是找到頁面中各個資料的資訊，並parse出我要的資訊，這邊有遇到一個很大的問題，就是104網站是動態顯示的網站，因此很難找出總共有幾頁，經過頻頻出錯的關係，我決定先抓100頁資料，顯示如下：
![](https://i.imgur.com/uKGxDjR.png)

#### 第二部分 - 1111.com.tw
1111與104的做法大同小異，但1111有下一頁的url可循，所以可以用recursion的方式來做爬取資料，總共爬了2000多筆。
```python=
# -*- coding: utf-8 -*-
import scrapy
import time
import json
from soft_jobs.items import SoftJobsItem
from scrapy import Request

class QuadraoneSpider(scrapy.Spider):
    name = 'quadraone'
    allowed_domains = ['https://www.1111.com.tw/']
    start_urls = ['https://www.1111.com.tw/job-bank/job-index.asp?ss=s&tt=1,2,4,16&wc=100100&d0=140200&si=1&ps=40&trans=1&page=1']

    def parse(self, response):
        print("開始")
        item = SoftJobsItem()
        job_title = response.xpath("//div[@class='jbInfoin']/h3/a/text()").extract()
        job_company = response.xpath("//div[@class='jbInfoin']/h4/a/text()").extract()
        job_salary = response.xpath("//div[@class='needs']/span[@class='mnone']/text()").extract()
        job_date = response.xpath("//div[@class='date']/span/text()").extract()
        for i in range(0 , len(job_title)):
            item["job_title"]  = job_title[i]
            item["job_company"] = job_company[i]
            item["job_salary"] = job_salary[i]
            item["job_date"] = job_date[i]
            yield item
        print(job_title[1])
        next_url = response.xpath("//a[@class='begin']/@href").extract_first()
        print(next_url)
	#如果有下一頁的話
        if next_url != None:
            next_url = "https://www.1111.com.tw/job-bank/job-index.asp" + next_url
	    # 跑倒下ㄧ頁
            yield scrapy.Request(
                next_url,
                callback=self.parse,
		 # 這邊是指不去過濾訊息就回傳
                dont_filter=True
            )
```
成果圖：
![](https://i.imgur.com/2h2Y1ce.png)

## 五、輸出成csv檔案
只要輸入下面的指令，就能把資料一筆一筆的輸出成csv檔案，好讓我們用numpy做分析。
```
scrapy crawl yurator（名稱） -o file.csv -t csv
```
登愣！
這就產生了：
![](https://i.imgur.com/J23iO5k.png)

## 六、Numpy + Matplotlib分析：
https://nbviewer.jupyter.org/github/b10402113/Python-Machine-Learning/blob/master/%E6%9C%9F%E4%B8%AD%E5%B0%88%E9%A1%8C/%E6%9C%9F%E4%B8%AD%E5%B0%88%E9%A1%8C.ipynb
