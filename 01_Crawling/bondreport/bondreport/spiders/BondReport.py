import scrapy
from bondreport.items import BondreportItem

class BondReport(scrapy.Spider):
    name = "bondreport"

    def start_requests(self):
        urls = ["https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2011-01-01&writeToDate=2021-12-31&x=32&y=11&page=" + str(i) for i in range(1,108)]

        for url in urls:
            yield scrapy.Request(url= url, callback=self.parse)

    def parse(self, response): # response에는 위 url에 대한 결과값이 담김
        item = BondreportItem()

        for i in range(3,48):

            if not response.xpath(f'//*[@id="contentarea_left"]/div[3]/table[1]/tr[{i}]/td[3]/a/@href').extract():
                continue
            else:
                item['file_url'] = response.xpath(f'//*[@id="contentarea_left"]/div[3]/table[1]/tr[{i}]/td[3]/a/@href').extract()
                yield item      
        
