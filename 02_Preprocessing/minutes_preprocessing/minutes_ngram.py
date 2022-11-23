import re
import os
from eKoNLPy.ekonlpy.sentiment import MPCK
import itertools

def minutes_ngram():
    '''
    의사록 5-gram 함수
    return: n-gram 개수
    '''
    ngram_list = []

    TXT_DIR = '//Users/stillssi/Desktop/minutes/Data/split_data/' #split text 파일 경로
    file_list = os.listdir(TXT_DIR)
    for file in file_list:
        f = open(TXT_DIR+file,'r', encoding='utf-8')
        lines = f.readlines()

        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        text = []
        for l in lines:
            result = hangul.sub('', l)
            result = result.split(' ')
            result_removed = [i for i in result if i != '']
            text.append(result_removed)
        
        text = list(itertools.chain(*text))
        resultt = ' '.join(text)   

        mpck = MPCK()
        tokens = mpck.tokenize(resultt)
        ngrams = mpck.ngramize(tokens)
        ngram_list.append(ngrams)
        score = mpck.classify(tokens + ngrams, intensity_cutoff=1.5)
        # ngram_list = list(itertools.chain(*ngram_list))
        # ngram_list = list(set(ngram_list))
    return len(ngram_list)

minutes_ngram()