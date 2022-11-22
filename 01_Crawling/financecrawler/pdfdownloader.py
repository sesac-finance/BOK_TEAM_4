import requests
import pandas as pd

reports = pd.read_csv('naver_report.csv', encoding='utf-8-sig')
titles = reports['title'].values
urls = reports['file_url'].values

for url, title in zip(urls[:10], titles[:10]):
    url = url.rstrip()
    r = requests.get(url, allow_redirects=True)
    open(f'./pdf/{title.rstrip()}.pdf', 'wb').write(r.content)