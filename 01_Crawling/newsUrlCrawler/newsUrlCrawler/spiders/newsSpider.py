import scrapy
import time
import csv
from newsUrlCrawler.items import NewscrawlingItem

class NewsUrlSpider(scrapy.Spider):
    name = 'newsUrlCrawler'
    def start_requests(self):
        url_list = []
        for i in range(2021,2022):
            for j in range(1,13,3):
                if j<10:
                    a = '0'+str(j)
                else:
                    a = str(j)
                if j+2<10:
                    b = '0'+str(j+2)
                else:
                    b = str(j+2)
                url_list.append(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B8%88%EB%A6%AC&sort=2&pd=3&ds={i}.{a}.01&de={i}.{b}.28&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&nso=so:r,a:all&start=')
        

        for url in url_list:
            for page in range(1,3992,10):
                url_1 = url + str(page)
                yield scrapy.Request(url = url_1, callback = self.parse, cb_kwargs = dict(page = page))
                time.sleep(0.4)
                

            
    def parse(self, response, page:int):
        item = NewscrawlingItem()
        for list_num in range(page,page+10):
            try:
                item['news_name'] = response.xpath(f'//*[@id="sp_nws{list_num}"]/div/div/div[1]/div[2]/a[1]/text()').extract()[0]
                item['date'] = response.xpath(f'//*[@id="sp_nws{list_num}"]/div/div/div[1]/div[2]/span/text()').extract()[0]
                item['url'] = response.xpath(f'//*[@id="sp_nws{list_num}"]/div/div/a/@href').extract()[0]
                yield item
            except:
                break
