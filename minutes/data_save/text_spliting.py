import os
import shutil
def split_text():
    TXT_DIR = '/Users/stillssi/Desktop/BOK_TEAM_4/Data/text_data/'
    file_list = os.listdir(TXT_DIR)
    for file in file_list:
        f = open(TXT_DIR+file, 'r', encoding='utf-8')
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        first_index = [i for i in range(len(lines)) if '의결안건' in lines[i]]
        second_index = [i for i in range(len(lines)) if '위원 토의내용' in lines[i]]
        last_index = [j for j in range(len(lines)) if '심의결과' in lines[j]]
        print(first_index, second_index, last_index)
        SAVE_FOLDER = '/Users/stillssi/Desktop/BOK_TEAM_4/Data/split_data/'
        if not os.path.isdir(SAVE_FOLDER):
            os.mkdir(SAVE_FOLDER)
        k = open('/Users/stillssi/Desktop/BOK_TEAM_4/Data/split_data/'+file, 'a', encoding='utf-8')
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