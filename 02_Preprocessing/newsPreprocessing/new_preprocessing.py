import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib import rc
from ekonlpy.sentiment import MPCK
import itertools

def cleansing(text):
    repl =''
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' # 자음, 모음 제거
    text = re.sub(pattern= pattern, repl=repl, string=text)
    pattern = '[^가-히\s]' # 특수기호 제거
    text = re.sub(pattern= pattern, repl=repl, string=text)
    pattern = '<[^>]*>' # html 제거
    text = re.sub(pattern = pattern, repl=repl,string=text)
    pattern = '\.([^\.]*(?:기자|뉴스|특파원|교수|작가|대표|논설|고문|주필|부문장|팀장|장관|원장|연구원|이사장|위원|실장|차장|부장|에세이|화백|사설|소장|단장|과장|기획자|큐레이터|저작권|평론가|©|©|ⓒ|\@|\/|=|▶|무단|전재|재배포|금지|\[|\]|\(\))[^\.]*)$'
    text = re.sub(pattern = pattern, repl=repl,string=text)   

    return text

def load_data_preprocessing():
    df=pd.read_csv('./naver_news_scrapy_total_prep.csv', usecols=['media','date','content'])

    # 분석할 기간에 해당하는 데이터 추출
    df=df[(df['date']>= 20110101) & (df['date'] <= 20211231)] 

    # date 컬럼 데이터 타입 datetime으로 변경
    df['date'] = pd.to_datetime(df['date'].astype('str'))

    # 언론사명이 다른 5개의 데이터 삭제, 인덱스 초기화
    EPA = df[df['media'].str.contains('EPA')].index
    df.drop(EPA,inplace=True)
    df.reset_index(drop=True,inplace=True)

    # 본문 데이터 정제
    df['content'] = df['content'].map(lambda x: cleansing(x))

    return df.to_csv('naver_news_prep.csv', index=False)
    
def visualization(): # 언론사, 연도 별 뉴스량 시각화
    df=pd.read_csv('./naver_news_prep.csv')

    # date 컬럼 데이터 타입 datetime으로 변경
    df['date'] = pd.to_datetime(df['date'])
    # year 컬럼 추가
    df['year']=df.date.dt.year

    rc('font', family='AppleGothic')

    labels=['연합뉴스','연합인포맥스','이데일리']
    plt.rcParams['axes.unicode_minus'] = False

    label = df['year'].unique()
    index=np.arange(len(label))
    legend=df['media'].unique()
    alpha = 0.5

    sum_by_media_year = df.groupby(['year','media'])['content'].count().unstack('media')
    sum_by_media_year.plot(kind='bar', stacked=True)

    plt.title('Total number of news per agency over time', fontsize=10)
    plt.xticks(index, fontsize=7, rotation=90)
    plt.figure(figsize=(25,22))
    plt.show()

def news_ngram_list(text): # ngram 생성
    ngram_list=[]

    mpck = MPCK()
    tokens = mpck.tokenize(text)
    ngrams = mpck.ngramize(tokens)
    ngram_list.append(ngrams)
    ngram_list = list(itertools.chain(*ngram_list)) # 이중 리스트 형성 안되도록 풀어주기
    return ngram_list

def news_ngram(): # ngram 추출 후 new_df에 저장
    new_df=pd.DataFrame(columns=['date','ngrams'])
    df=pd.read_csv('./naver_news_prep.csv',usecols=['date','content'])
    new_df['date']=df['date'].map(lambda x: pd.to_datetime(x))
    new_df['ngrams'] = df['content'].map(lambda x: news_ngram_list(x))

    return new_df

df=news_ngram()
df.to_csv('news_ngram_data.csv')