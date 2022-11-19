from requests import get
import pandas as pd
import numpy as np
def read_file():
    df = pd.read_csv('/Users/stillssi/Desktop/BOK_TEAM_4/minutes/minutes_file_list.csv')
    return df['date'].tolist(), df['file_url'].tolist()


def download(date,url):
    for x,y in zip(date,url):
        with open(f'/Users/stillssi/Desktop/BOK_TEAM_4/pdf_data/{x}.pdf', "wb") as file:
            response = get(y)
            file.write(response.content)

date, url = read_file()
download(date, url)