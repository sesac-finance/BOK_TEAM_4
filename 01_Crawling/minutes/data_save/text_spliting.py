import os
import shutil
import re
def split_text():
    TXT_DIR = '/Users/stillssi/Desktop/minutes/Data/text_data/'
    file_list = os.listdir(TXT_DIR)
    
    for file in file_list:
        f = open(TXT_DIR+file, 'r', encoding='utf-8')
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        #의결 날짜 추출
        date_index = [i for i in range(len(lines)) if '일 자' in lines[i] or '일    자' in lines[i] or '일 시' in lines[i] or '일    시' in lines[i]]
        date = re.sub(r'[^0-9]', '', lines[date_index[0]])[1:]
        year = date[0:4]
        if len(date) == 6:
            month = date[4]
            day = date[5]
        elif len(date) == 7:
            month = date[4]
            day = date[5:]
        else:
            month = date[4:6]
            day = date[6:]

        
        #필요 내용 추출
        first_index = [i for i in range(len(lines)) if '의결안건' in lines[i]]
        second_index = [i for i in range(len(lines)) if '위원 토의내용' in lines[i]]
        last_index = [j for j in range(len(lines)) if '심의결과' in lines[j]]

        SAVE_FOLDER = '/Users/stillssi/Desktop/minutes/Data/split_data/'
        if not os.path.isdir(SAVE_FOLDER):
            os.mkdir(SAVE_FOLDER)
        #의결 날짜로 파일명
        k = open('/Users/stillssi/Desktop/minutes/Data/split_data/'+f'{year}.{month}.{day}.txt', 'a', encoding='utf-8')
        
        try:
            k.write(''.join(lines[first_index[0]:second_index[0]]))
        except:
            pass
        
        for i,j in zip(second_index, last_index):
            k.write(''.join(lines[i:j]))
        k.close()
    # if os.path.exists(TXT_DIR):
    #     shutil.rmtree(TXT_DIR)
split_text()