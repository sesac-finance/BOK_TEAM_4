import re
import os
from eKoNLPy.ekonlpy.sentiment import MPCK
import pandas as pd
def minutes_ngram():
    '''
    의사록 5-gram 함수
    return: n-gram 개수
    '''
    mpck = MPCK()
    TXT_DIR = '//Users/stillssi/Desktop/minutes/Data/split_data/' #split text 파일 경로
    label_data = pd.read_csv('/Users/stillssi/Desktop/BOK_TEAM_4/02_Preprocessing/minutes_preprocessing/base_rate_label.csv')
    file_list = os.listdir(TXT_DIR)
    df = pd.DataFrame(columns=['date', 'ngrams', 'label'])
    
    for file in file_list:
        ngram_list = []

        try:
            f = open(TXT_DIR+file,'r', encoding='utf-8')
            lines = f.readlines()

            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
            
            for l in lines:
                result = hangul.sub('', l)
                result = result.split(' ')
                result_removed = [i for i in result if i != '']
                
                line = ' '.join(result_removed)
                tokens = mpck.tokenize(line)
                ngrams = mpck.ngramize(tokens)
                ngram_list.append(ngrams)
            df.loc[i] = [file,ngram_list,]
            dates.append(data['date'].loc[i])
            
                
        except:
            pass

    return ngram_list

minutes_ngram()