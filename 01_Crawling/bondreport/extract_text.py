from tika import parser
import os

# pdf에 있는 텍스트를 추출
def extract_text():
    pdf_dir = "/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/PDF"
    pdf_list = os.listdir(pdf_dir)

    for pdf in pdf_list:
        # print(pdf)
        # print(pdf[:-4])
        path = f"/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/PDF/{pdf}"
        parsed = parser.from_file(path)
        txt_dir = f"/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/TXT/{pdf[:-4]}.txt"
        txt = open(txt_dir, 'w', encoding='utf-8-sig')
        print(parsed['content'], file=txt)
        txt.close()

extract_text()