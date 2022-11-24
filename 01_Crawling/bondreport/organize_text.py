import os

txt_dir = '/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/TXT'
txt_list = os.listdir(txt_dir)

# 공백 없애기
def organize_txt(txt_name):
    text_file = open(f'/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/TXT/{txt_name}','r')
    text = ''
    for line in text_file:
        new_line = line.strip()
        if len(new_line) == 0: continue
        else:
            text += (new_line + '')
        
    f = open(f'/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/organized_txt/{txt_name}', 'w')
    f.write(text)
    f.close()
    # print(text)
    
for txt in txt_list:
    organize_txt(txt)


