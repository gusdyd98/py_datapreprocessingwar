import numpy as np

print("############################################")
print("##  72page. 집약                     ")
print("############################################")

import pandas as pd

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

rsv_cnt_tb=reserve_tb.groupby('hotel_id').size().reset_index()

rsv_cnt_tb.columns=['hotel_id', 'rsv_cnt']

cus_cnt_tb=reserve_tb.groupby('hotel_id')['customer_id'].nunique().reset_index()

cus_cnt_tb.columns=['hotel_id', 'cus_cnt']

print(cus_cnt_tb)

pd.merge(rsv_cnt_tb, cus_cnt_tb, on='hotel_id')

print(rsv_cnt_tb)


print('------------')
import pandas as pd

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

result=reserve_tb.groupby('hotel_id').agg({'reserve_id':'count', 'customer_id':'nunique'})

result.reset_index(inplace=True)
result.columns=['hotel_id', 'rsv_cnt', 'cus_cnt']

print(result)


print('------------')
print('SUM값 구하기----')
import pandas as pd

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

result=reserve_tb\
    .groupby(['hotel_id','people_num'])['total_price']\
    .sum().reset_index()

result.rename(columns={'total_price':'price_sum'}, inplace=True)

print(result)



print("############################################")
print("##  3.3.81page 최댓값, 최솟값, 대푯값 산출       ")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

result= reserve_tb.groupby('hotel_id')\
    .agg({'total_price':['max','min','mean','median',
                         lambda x: np.percentile(x, q=20)]})\
    .reset_index()

result.columns=['hotel_id', 'price_max', 'price_min', 'price_mean', 'price_median', 'price_20per']

print(result)

print("############################################")
print("##  3.4.85page 분포 계산        ")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

result= reserve_tb.groupby('hotel_id') \
    .agg({'total_price':['var','std']}) \
    .reset_index()

result.columns=['hotel_id', 'price_var', 'price_std']

result.fillna(0, inplace=True)
print(result)

print("############################################")
print("##  3.5. 최빈값 계산    ")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

print(reserve_tb['total_price'].head())

result= reserve_tb['total_price'].round(-3).mode()
result.columns=['mostcommon_total_price']

print('-----------')
print(result)

print("############################################")
print("##  3.6. 순위 계산    ")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

reserve_tb['reserve_datetime']=pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

reserve_tb['log_no']=reserve_tb.groupby('customer_id')['reserve_datetime']\
    .rank(ascending=True, method='first')

print('-----------')
print(reserve_tb.head())

print("############################################")
print("##  3.6. 랭크 계산    ")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

reserve_tb['reserve_datetime']=pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

rsv_cnt_tb=reserve_tb.groupby('hotel_id').size().reset_index()
rsv_cnt_tb.columns=['hotel_id', 'rsv_cnt']

print(rsv_cnt_tb)

rsv_cnt_tb['rsv_cnt_rank']=rsv_cnt_tb['rsv_cnt']\
    .rank(ascending=False, method='min')

print('-----------')
print(rsv_cnt_tb)

