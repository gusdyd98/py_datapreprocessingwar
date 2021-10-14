import gc

print("############################################")
print("##  4.1. 결합, 마스터 테이블에서 정보 얻기      ")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')
hotel_tb=pd.read_csv('./data/hotel.csv', encoding='UTF-8')

result=pd.merge(reserve_tb, hotel_tb, on='hotel_id', how='inner')\
    .query('people_num == 1 & is_business')

print(hotel_tb.head())
print(reserve_tb.head())

print('------------------')
print(result)

result=pd.merge(reserve_tb.query('people_num == 1'),
                hotel_tb.query('is_business'),
                on='hotel_id', how='inner')

print('------------------')
print(result)


print("############################################")
print("##  4.2. 결합, 조건에 따라 결합할 마스터 테이블 변경하기")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')
hotel_tb=pd.read_csv('./data/hotel.csv', encoding='UTF-8')

print(hotel_tb.head())

small_area_mst=hotel_tb\
    .groupby(['big_area_name', 'small_area_name'], as_index=False)\
    .size().reset_index()


small_area_mst.columns=['index','big_area_name', 'small_area_name', 'hotel_cnt']

print(small_area_mst.head())

small_area_mst['join_area_id']=\
    np.where(small_area_mst['hotel_cnt']-1>=20,
             small_area_mst['small_area_name'],
             small_area_mst['big_area_name'])

small_area_mst.drop(['hotel_cnt', 'big_area_name'], axis=1, inplace=True)

print('-------------------------')
print(small_area_mst.head())

base_hotel_mst=pd.merge(hotel_tb, small_area_mst, on='small_area_name')\
    .loc[:, ['hotel_id', 'join_area_id']]

print('-------------------------')
print(base_hotel_mst.head())

del small_area_mst
gc.collect()

print('1------------------------')
recommend_hotel_mst=pd.concat([\
    hotel_tb[['small_area_name', 'hotel_id']]\
        .rename(columns={'small_area_name': 'join_area_id'}, inplace=False),
    hotel_tb[['big_area_name', 'hotel_id']]\
        .rename(columns={'big_area_name': 'join_area_id'}, inplace=False)\
    ])

print(recommend_hotel_mst.head())
print('2------------------------')
recommend_hotel_mst.rename(columns={'hotel_id':'rec_hotel_id'}, inplace=True)
print(recommend_hotel_mst.head())
print('3------------------------')

result=pd.merge(base_hotel_mst, recommend_hotel_mst, on='join_area_id')\
    .loc[:,['hotel_id', 'rec_hotel_id']]\
    .query('hotel_id != rec_hotel_id')

print('4------------------------')
print('-------------------------')
print(base_hotel_mst.head())
print('-------------------------')
print(recommend_hotel_mst.head())
print('-------------------------')
print(result)


print("############################################")
print("##  4.3. 과거의 데이터 정보 얻기 (n번 이전 까지의 데이터")
print("############################################")

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')
hotel_tb=pd.read_csv('./data/hotel.csv', encoding='UTF-8')

print(hotel_tb.head())

