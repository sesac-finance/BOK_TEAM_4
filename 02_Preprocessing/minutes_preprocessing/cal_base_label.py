import pandas as pd
import datetime
from datetime import timedelta
from datetime import datetime

def present_rate():
    b = []
    dataframe_list = []
    base_rate = pd.read_csv('/Users/stillssi/Desktop/BOK_TEAM_4/01_Crawling/base_rate/base_rate.csv')
    base_rate['date'] = pd.to_datetime(base_rate['date'])
    base_rate = base_rate.sort_values(by='date',ascending=True)
    base_rate.set_index('date', inplace=True)
    for i in range(len(base_rate.index)):
        start_date = pd.to_datetime(base_rate.index[i]) ## 시작 날짜
        try:
            tmp = {}
            end_date = pd.to_datetime(base_rate.index[i+1]) ## 마지막 날짜\
            bet = pd.date_range(start_date,end_date+ timedelta(days = -1),freq='D').values
            
            tmp = {'date': bet, 'rate': [base_rate.loc[start_date].rate]*len(bet)} 
            b = pd.DataFrame(tmp)
            b.set_index('date', inplace=True)
            dataframe_list.append(b)
        except:
            break
        
    merge_dataframe = pd.concat(dataframe_list)
    merge_dataframe = merge_dataframe.iloc[46:4100]
    merge_dataframe.to_csv('./base_rate.csv')
    return merge_dataframe



def future_rate(fra):
    da_list, ra_list = [],[]
    base_r = fra
    for i in range(len(base_r.index)):
        if base_r.index[i] == datetime.strptime('2022-01-01', '%Y-%m-%d'):
            break
        da_list.append(base_r.index[i])
        ra_list.append(base_r.loc[base_r.index[i] + timedelta(days = 28)].rate)
        
    label_ = {'date': da_list, 'rate': ra_list}
    label_df = pd.DataFrame(label_)
    label_df.set_index('date', inplace=True)
    return label_df


def please2(x):
    return 1 if x > 0.03 else -1 if x < -0.03 else 0

pre_rate = present_rate()
fu_rate = future_rate(pre_rate)
new_df = (pre_rate - fu_rate)
new_df['label'] = new_df['rate'].apply(lambda x : please2(x))
new_df.to_csv('base_rate_label.csv')
