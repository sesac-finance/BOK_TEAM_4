import scrapy
import csv
from newscrawling.items import NewscrawlingItem
import random

class NewsUrlSpider(scrapy.Spider):
    name = 'edaily' # scrapy crawl edaily -o edaily.csv

    def start_requests(self):
        #office_section_code={}&news_office_checked={}
        # press=[[2,1001],[3,1018],[8,2227]] # 연합뉴스, 이데일리, 연합인포맥스
        # url_list=[f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0&start={k}',
        #           f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1018&is_sug_officeid=0&start={k}',
        #           f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=8&news_office_checked=2227&is_sug_officeid=0&start={k}']
 
        for j in range(11,22,1): # 년도 21 -> 11 로 바꿔주기
            for i in range(1,13,3): # 3개월씩 끊어 크롤링
                for k in range(1, 3992,10): # 페이지수 : 11 -> 3992로 바꿔주기
                    if i>=10:
                        try:
                            url=f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1018&is_sug_officeid=0&start={k}'
                            yield scrapy.Request(url=url, callback = self.parse)
                        except:
                            break
                    else:
                        try:
                            url=f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.0{i}.01&de=20{j}.0{i+2}&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1018&is_sug_officeid=0&start={k}'
                            yield scrapy.Request(url=url, callback = self.parse)
                        except:
                            break
            
    def parse(self, response):
        user_agents_list = [
            'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            ]

        paths=response.css('.list_news li')
        for path in paths:
            url = path.css('.info_group > a::attr(href)')[1].get()
            yield scrapy.Request(url=url, callback = self.re_parse, headers={'User-Agent': random.choice(user_agents_list)})

    def re_parse(self,response):
        item = NewscrawlingItem()
        try:
            item['date'] = response.css('.media_end_head_info_datestamp_time::text').get().split()[0]
            item['press'] = response.css('.media_end_head_top_logo img::attr(title)').get() 
            item['article'] = response.css('#dic_area::text').getall()
        except:
            pass
        yield item


        