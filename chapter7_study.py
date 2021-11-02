print("############################################")
print("##  7.1. 전개        ")
print("############################################")

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

print(reserve_tb)

result=pd.pivot_table(reserve_tb, index='customer_id', columns='people_num', values='reserve_id',
               aggfunc=lambda x: len(x), fill_value=0)

print('---------------')
print(result)


print("############################################")
print("##  7.2. 희소행렬로의 변환 ")
print("############################################")

import pandas as pd
from scipy.sparse import csc_matrix

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

print(reserve_tb)

cnt_tb=reserve_tb\
    .groupby(['customer_id', 'people_num'])['reserve_id'].size()\
    .reset_index()

cnt_tb.columns=['customer_id', 'people_num', 'rsv_cnt']

print('---------------')
print(cnt_tb)

customer_id=pd.Categorical(cnt_tb['customer_id'])
people_num=pd.Categorical(cnt_tb['people_num'])


result=csc_matrix((cnt_tb['rsv_cnt'], (customer_id.codes, people_num.codes)),
                  shape=(len(customer_id.categories), len(people_num.categories)))
print('헤헤헤')
print(result)



