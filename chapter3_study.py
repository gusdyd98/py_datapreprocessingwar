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
print("##  3.3.81page 최댓값, 최솟값, 대푯값 산출
print("############################################")

import pandas as pd

pd.set_option('display.max_columns', None)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')
