# -*- coding: utf-8 -*-
import scrapy
import time
import json
from soft_jobs.items import SoftJobsItem
from scrapy import Request

class YuratorSpider(scrapy.Spider):
    name = 'yurator'
    allowed_domains = ['104.com']
    start_urls = [
        'https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=11&asc=0&page=0'
    ]

    def parse(self, response):
        div_list = response.xpath("//div[@id='js-job-content']/article")
        for div in div_list:
            item = SoftJobsItem()
            # jsonresponse = json.loads(response.body_as_unicode())
            # item["job_title"] = tr.xpath("./td[1]/a/text()").extract_first()
            job_company= div.xpath("./div[@class='b-block__left']/ul[@class='b-list-inline b-clearfix']/li[2]/a/text()").extract()
            # 去除前後空白
            item["job_company"] = job_company[0].strip()
            date = div.xpath("./div[@class='b-block__left']/h2[@class='b-tit']/span/text()")[0].extract()
            item["job_salary"] = div.xpath("./div[@class='b-block__left']/div[@class='job-list-tag b-content']/span/text()")[0].extract()
            item["job_date"] = date.strip()
            item["job_title"] = div.xpath("./div[@class='b-block__left']/h2[@class='b-tit']/a/text()")[0].extract()
            # item["job_company"] = tr.xpath("./td[5]/text()").extract_first()
            yield item
        i = 0
        while i <= 100:
            next_url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=11&asc=0&page="+str(i)+"&mode=s"
            i = i + 1
            yield Request(next_url , callback=self.parse,dont_filter=True)