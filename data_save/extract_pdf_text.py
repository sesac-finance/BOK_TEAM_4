import os
import shutil
from tika import parser

def extract_pdf_text():
    PDF_DIR = '/Users/stillssi/Desktop/BOK_TEAM_4/pdf_data' #PDF 파일 경로
    os.listdir(PDF_DIR)

    file_list = os.listdir(PDF_DIR)

    for file in file_list:    
        pdf_path =  f"/Users/stillssi/Desktop/BOK_TEAM_4/pdf_data/{file}" 
        parsed = parser.from_file(pdf_path)
        SAVE_DIR = '/Users/stillssi/Desktop/BOK_TEAM_4/text_data/'+file[0:10]+'.txt'
        txt = open(SAVE_DIR, 'w', encoding = 'utf-8')
        print(parsed['content'], file = txt)
        txt.close()
