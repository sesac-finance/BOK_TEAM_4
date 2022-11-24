import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib import rc
from ekonlpy.sentiment import MPCK

def load_data_preprocessing():
    df=pd.read_csv('./naver_news_scrapy_total_prep.csv', usecols=['media','date','content','content_len'])

    # 분석할 기간에 해당하는 데이터 추출
    df=df[(df['date']>= 20110101) & (df['date'] <= 20211231)] 

    # date 컬럼 데이터 타입 datetime으로 변경
    df['date'] = pd.to_datetime(df['date'].astype('str'))

    # 언론사명이 다른 5개의 데이터 삭제, 인덱스 초기화
    EPA = df[df['media'].str.contains('EPA')].index
    df.drop(EPA,inplace=True)
    df.reset_index(drop=True,inplace=True)

    return df.to_csv('naver_news_prep.csv', index=False)

def visualization():
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

def news_ngram():
    df=pd.read_csv('./naver_news_prep.csv')

    mpck = MPCK()
    ngram_list=[]
    for i in df['content']:
        tokens = mpck.tokenize(i)
        ngrams = mpck.ngramize(tokens)
        ngram_list.append(ngrams)
        score = mpck.classify(tokens + ngrams, intensity_cutoff=1.5)
    print(ngram_list)