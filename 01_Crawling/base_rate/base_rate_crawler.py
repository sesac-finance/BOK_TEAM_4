import requests
from bs4 import BeautifulSoup
import pandas as pd

base_rate_url = 'https://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643'

def base_rate_crawler() -> list:
    '''
    기능: 한국은행 홈페이지에서 기준 금리 크롤링
    결과: 기준금리 변경일자 & 기준금리
    '''

    base_result = []

    res = requests.get(base_rate_url)
    print(f'응답코드: {res.status_code}')

    soup = BeautifulSoup(res.text, 'html.parser')
    
    for li in soup.select('.fixed tbody tr'):
        year = int(li.select('td')[0].text)
        month = int(li.select('td')[1].text.split()[0].replace('월',''))
        day = int(li.select('td')[1].text.split()[1].replace('일',''))
        base_rate = float(li.select('td')[2].text)

        if year<= 2021 and year>=2011:
            base_result.append([f'{year}.{month}.{day}', base_rate])
        else:
            pass
    return base_result


def save_base_rate(base_result:list):
    '''
    기준금리->csv파일로 저장하는 함수
    '''
    base_rate_df = pd.DataFrame(base_result, columns=['date','rate'])
    base_rate_df.to_csv('01_Crawling/base_rate/base_rate.csv', index=False, encoding='utf-8-sig')
    print('저장 완료')

base_result = base_rate_crawler()
save_base_rate(base_result=base_result)