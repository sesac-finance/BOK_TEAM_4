 # -*- coding: utf-8 -*-
import scrapy
from financecrawler.items import FinancecrawlerItem

class ReportCrawlerSpider(scrapy.Spider):
    # https://finance.naver.com/research/debenture_list.naver
    
    name = "financecrawler"

    def start_requests(self):
        urls = ['https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2011-01-01&writeToDate=2021-12-31&page={0}'.format(i) for i in range(1, 108, 1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = FinancecrawlerItem()

        for i in range(3, 48, 1):
            if not response.xpath(f'//*[@id="contentarea_left"]/div[3]/table[1]/tr[{i}]/td[3]/a/@href').extract():
                continue
            else:
                item['title'] = response.xpath(f'//*[@id="contentarea_left"]/div[3]/table[1]/tr[{i}]/td[1]/a/text()').extract()
                item['date'] = response.xpath(f'//*[@id="contentarea_left"]/div[3]/table[1]/tr[{i}]/td[4]/text()').extract()
                item['file_url'] = response.xpath(f'//*[@id="contentarea_left"]/div[3]/table[1]/tr[{i}]/td[3]/a/@href').extract()
                yield item
