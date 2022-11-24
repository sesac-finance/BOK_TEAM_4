import os
import re
from ekonlpy.sentiment import MPCK
import pandas as pd

TXT_DIR = "/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/organized_txt"
PDF_DIR = "/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/PDF"
data = pd.read_csv('/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/new.csv')

df = pd.DataFrame(columns=['date', 'content', 'scores', 'ngrams'])
text_list = os.listdir(TXT_DIR)
pdf_list = os.listdir(PDF_DIR)
ngram_list = []
scores = []
content = []
dates = []

for i in range(len(text_list)):
    
    text_file = open(TXT_DIR + f"/{text_list[i]}", 'r', encoding='utf-8-sig')
    text = ''
    for line in text_file:
        new_line = line.strip()
        if len(new_line) == 0:
            continue
        else:
            text += new_line

    re_text = re.sub('[^ ㄱ-ㅣ가-힣]+', '', text).lstrip().rstrip()
    content.append(re_text)
    dates.append(data['date'].loc[i])

    mpck = MPCK()
    tokens = mpck.tokenize(re_text)
    ngrams = mpck.ngramize(tokens)
    score = mpck.classify(tokens+ngrams, intensity_cutoff=1.5)
    scores.append(score)
    ngram_list.append(ngrams)


df['date'] = dates
df['date'] = pd.to_datetime(df['date'], yearfirst=True)
df['content'] = content
df['scores'] = scores
df['ngrams'] = ngram_list

df.to_csv('bondreport.csv', mode = 'w', encoding='utf-8-sig')