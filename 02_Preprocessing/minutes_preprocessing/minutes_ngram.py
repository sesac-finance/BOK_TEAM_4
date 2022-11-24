import re
import os
from eKoNLPy.ekonlpy.sentiment import MPCK
import itertools
from eKoNLPy.ekonlpy.tag import MeCab
def minutes_ngram():
    '''
    의사록 5-gram 함수
    return: n-gram 개수
    '''
    ngram_list = []
    mpck = MPCK()
    mecab = MeCab()
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

        tokens = mpck.tokenize(resultt)
        
        ngrams = mpck.ngramize(tokens)
        
        score = mpck.classify(tokens + ngrams, intensity_cutoff=1.3)
        ngram_list_1 = list(itertools.chain(*ngram_list))
        ngram_list_1 = list(set(ngram_list_1))

    return len(ngram_list_1)

minutes_ngram()