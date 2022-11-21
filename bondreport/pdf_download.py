import requests
import pandas as pd

# 크롤링한 url을 통해 pdf로 저장
def pdf_download(file_loc):
    
    reports = pd.read_csv(file_loc)
    urls = reports['file_url'].values

    for url in urls:
        pdf_name = url[-17:-4]
        response = requests.get(url)
        open(f'/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/PDF/{pdf_name}.pdf', 'wb').write(response.content)

pdf_download('/Users/jang-yunji/Desktop/프로젝트/BOK_TEAM_4/bondreport/BondreportFile.csv')