import scrapy
import time
import csv
from newscrawling.items import NewscrawlingItem

class NewsUrlSpider(scrapy.Spider):
    name = 'newsUrlCrawler'

    def start_requests(self):
        #office_section_code={}&news_office_checked={}
        # press=[[2,1001],[3,1018],[8,2227]] # 연합뉴스, 이데일리, 연합인포맥스
        url_list=['https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=2011.01.01&de=2011.03.31&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0',
                    'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=2011.01.01&de=2011.03.31&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1018&is_sug_officeid=0',
                    'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=2011.01.01&de=2011.03.31&related=0&mynews=1&office_type=1&office_section_code=8&news_office_checked=2227&is_sug_officeid=0']
 
        # urls=['https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=2011.01.01&de=2011.03.31&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&nso=so%3Ar%2Cp%3Afrom20110101to20110331&is_sug_officeid=0&start='+str(i) for i in range(1, 3992,10)] # 11 -> 3992로 바꿔주기
        for j in range(21,22,1): # 수정
            for i in range(1,13,3):
                if i>=10:
                    urls=[f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.{i}.01&de=20{j}.{i+2}.31&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0&start='+str(i) for i in range(1, 3992,10)] # 11 -> 3992로 바꿔주기
                    for url in urls:
                        try:
                            yield scrapy.Request(url=url, callback = self.parse)
                        except:
                            break
                else:
                    urls=[f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=2&photo=0&field=0&pd=3&ds=20{j}.0{i}.01&de=20{j}.0{i+2}.31&related=0&mynews=1&office_type=1&office_section_code=2&news_office_checked=1001&is_sug_officeid=0&start='+str(i) for i in range(1, 3992,10)] # 11 -> 3992로 바꿔주기
                    for url in urls:
                        try:
                            yield scrapy.Request(url=url, callback = self.parse)
                        except:
                            break
            
    def parse(self, response):
        for i in range(1,11):
            try:
                item = NewscrawlingItem()
                item['url'] = response.xpath('//*[@id="sp_nws%d"]/div/div/div[1]/div[2]/a[2]/@href' %i).extract()[0]
            except:
                break

        time.sleep(5)

        yield item

class NewsSpider(scrapy.Spider):
    name = "newsCrawler"
 
    def start_requests(self):
        with open('newsUrlCrawl.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield scrapy.Request(row['url'], self.parse)

    def parse(self, response):
        item = NewscrawlingItem()
                                        
        item['source'] = response.xpath('//*[@id="contents"]/div[13]/div/a/em').extract()[0]
        item['title'] = response.xpath('//*[@id="ct"]/div[1]/div[2]/h2').extract()[0]
        item['date'] = response.xpath('//*[@id="ct"]/div[1]/div[3]/div[1]/div[1]/span').extract()[0]
        item['article'] = response.xpath('//*[@id="dic_area"]/text()').extract()
                
        # print(item['title'])
        print(item['article'])
 
        time.sleep(5)
 
        yield item

