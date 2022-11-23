from tika import parser
import os

# pdf에 있는 텍스트를 추출
def extract_text():
    PDF_DIR = "./PDF"
    pdf_list = os.listdir(PDF_DIR)

    for pdf in pdf_list:
        path = PDF_DIR + f"/{pdf}"
        parsed = parser.from_file(path)
        txt_dir = f"./TXT/{pdf[:-4]}.txt"
        txt = open(txt_dir, 'w', encoding='utf-8-sig')
        print(parsed['content'], file=txt)
        txt.close()

extract_text()