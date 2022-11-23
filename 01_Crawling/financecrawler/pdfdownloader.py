import requests
import pandas as pd

reports = pd.read_csv('naver_report.csv', encoding='utf-8-sig')
titles = reports['title'].values
urls = reports['file_url'].values
dates = reports['date'].values

for url in urls:
    url = url.rstrip()
    response = requests.get(url)
    pdf_name = url[-17:-4]
    open(f'./PDF/{pdf_name}.pdf', 'wb').write(response.content)