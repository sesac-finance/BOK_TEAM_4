import os
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

    # ngram 생성하기


    from ekonlpy.sentiment import MPCK
    import pandas as pd
    TXT_DIR = "../../01_Crawling/financecrawler/TXT"
    PDF_DIR = "../../01_Crawling/financecrawler/PDF"
    data = pd.read_csv('../../01_Crawling/financecrawler/new.csv')
    df = pd.DataFrame(columns=['date', 'content', 'scores', 'ngrams'])
    text_list = os.listdir(TXT_DIR)
    pdf_list = os.listdir(PDF_DIR)
    ngram_list = []
    scores = []
    content = []
    dates = []
    for i in range(len(text_list)):
        # 텍스트 불러오기
        text_file = open(TXT_DIR + f"/{text_list[i]}", 'r', encoding='utf-8-sig')
        text = ''
        for line in text_file:
            new_line = line.strip()
            if len(new_line) == 0:
                continue
            else:
                text += new_line
        # 정규 표현식
        re_text = re.sub('[^ ㄱ-ㅣ가-힣]+', '', text).lstrip().rstrip()
        content.append(re_text)
        dates.append(data['date'].loc[i])
        # MPCK 객체 생성
        mpck = MPCK()
        tokens = mpck.tokenize(re_text)
        ngrams = mpck.ngramize(tokens)
        score = mpck.classify(tokens+ngrams, intensity_cutoff=1.5)
        scores.append(score)
        ngram_list.append(ngrams)