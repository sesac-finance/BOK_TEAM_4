import scrapy
from minutes.items import MinutesItem

class Minutes(scrapy.Spider):
    name = 'minutes'

    def start_requests(self):
        urls = [
            'https://www.bok.or.kr/portal/bbs/B0000245/list.do?menuNo=200761&pageIndex='+ str(i) for i in range(1,25)
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)


    def parse(self, response):
        item = MinutesItem()

        for i in range(1, 10):
        
            try:
                item['file_url'] = response.xpath(f'//*[@id="content"]/div[3]/ul/li[{i}]/div/div[1]/div/div/ul/li[2]/a[1]/@href').extract()
                item['date'] = response.xpath(f'//*[@id="content"]/div[3]/ul/li[{i}]/div/div[2]/div/span[1]/text()').extract()
                yield item
            except:
                pass
