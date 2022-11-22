import scrapy
import time
import csv
from newscrawling.items import NewscrawlingItem

class NewsUrlSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        #office_section_code={}&news_office_checked={}
        # press=[[2,1001],[3,1018],[8,2227]] # 연합뉴스, 이데일리, 연합인포맥스
        # url_list=[f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0&start={k}',
        #             f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1018&is_sug_officeid=0&start={k}',
        #             f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=8&news_office_checked=2227&is_sug_officeid=0&start={k}']
 
        for j in range(21,22,1): # 년도 21 -> 11 로 바꿔주기
            for i in range(1,13,3): # 3개월씩 끊어 크롤링
                for k in range(1, 11,10): # 페이지수 : 11 -> 3992로 바꿔주기
                    if i>=10:
                        try:
                            url=f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}.31&docid=&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0&start={k}'
                            yield scrapy.Request(url=url, callback = self.parse)
                        except:
                            break
                    else:
                        try:
                            url=f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.0{i}.01&de=20{j}.0{i+2}.31&docid=&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0&start={k}'
                            yield scrapy.Request(url=url, callback = self.parse)
                        except:
                            break
            
    def parse(self, response):
        paths = [f'//*[@id="sp_nws{i}"]/div/div/div[1]/div[2]/a[2]/@href' for i in range(1,6)] # 11 -> 4001
        for path in paths:
            try:          
                re_url = response.xpath(path).extract()[0]
                print(re_url)
                yield scrapy.Request(url=re_url, callback = self.re_parse)
            except:
                pass
                # time.sleep(5)

    def re_parse(self,response):
        print('*'*100)
        item = NewscrawlingItem()
                                        
        item['press'] = response.xpath('//*[@id="contents"]/div[13]/div/a/em').extract()[0]
        item['title'] = response.xpath('//*[@id="ct"]/div[1]/div[2]/h2').extract()[0]
        item['date'] = response.xpath('//*[@id="ct"]/div[1]/div[3]/div[1]/div[1]/span').extract()[0]
        item['article'] = response.xpath('//*[@id="dic_area"]/text()').extract()
                
        print(item['title'])
        print(item['article'])
 
        # time.sleep(5)
 
        yield item