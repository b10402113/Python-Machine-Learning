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
        if next_url != None:
            next_url = "https://www.1111.com.tw/job-bank/job-index.asp" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
        # i = 0
        # while i <= 100:
        #     next_url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=11&asc=0&page="+str(i)+"&mode=s"
        #     i = i + 1
        #     yield Request(next_url , callback=self.parse,dont_filter=True)