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

result=reserve_tb.groupby('customer_id')\
    .apply(lambda x: x.sort_values(by='reserve_datetime', ascending=True))\
    .reset_index(drop=True)

print(result)

result['price_avg']=pd.Series(
    result.groupby('customer_id')
    ['total_price'].rolling(center=False, window=3, min_periods=1).mean()
    .reset_index(drop=True)
)

print('-----------------')
print(result)

result['price_avg']=\
    result.groupby('customer_id')['price_avg'].shift(periods=1)

print('-----------------')
print(result)

print("############################################")
print("##  4.4. 과거의 데이터 정보 얻기 (과거 n일의 합계)")
print("############################################")

import pandas as pd
import numpy as np
import pandas.tseries.offsets as offsets
import operator

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')
hotel_tb=pd.read_csv('./data/hotel.csv', encoding='UTF-8')

print(hotel_tb.head())

reserve_tb['reserve_datetime']=\
    pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

sum_table=pd.merge(
    reserve_tb[['reserve_id', 'customer_id', 'reserve_datetime']],
    reserve_tb[['customer_id', 'reserve_datetime', 'total_price']]
        .rename(columns={'reserve_datetime':'reserve_datetime_before'}),
    on='customer_id')
print('--------------')
print(sum_table)

print('--------------')
print(reserve_tb[['reserve_id', 'customer_id', 'reserve_datetime']])
print('--------------')
print(reserve_tb[['customer_id', 'reserve_datetime', 'total_price']])


sum_table=sum_table[operator.and_(
    sum_table['reserve_datetime'] > sum_table['reserve_datetime_before'],
    sum_table['reserve_datetime']+offsets.Day(-90) <= sum_table['reserve_datetime_before'])].groupby('reserve_id')['total_price'].sum().reset_index()


print('--------------')
print(sum_table)

sum_table.columns=['reserve_id','total_price_sum']
print('--------------')
print(sum_table)

result=pd.merge(reserve_tb, sum_table, on='reserve_id', how='left').fillna(0)
print('--------------')
print(result)

print("############################################")
print("##  4.5. 상호 결합")
print("############################################")

import pandas as pd
import numpy as np
import pandas.tseries.offsets as offsets
import operator
import datetime
from   dateutil.relativedelta import relativedelta

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')
customer_tb=pd.read_csv('./data/customer.csv', encoding='UTF-8')

print(customer_tb.head())

month_mst=pd.DataFrame({
    'year_month':
        [(datetime.date(2017,1,1) + relativedelta(months=x)).strftime("%Y%m")
         for x in range(0,3)]
})
print('---------------')
print(month_mst)

customer_tb['join_key']=0
month_mst['join_key']=0

print('---------------')
print(month_mst)

customer_mst=pd.merge(
    customer_tb[['customer_id', 'join_key']], month_mst, on='join_key'
)

print('---------------')
print(customer_mst)

reserve_tb['year_month']=reserve_tb['checkin_date']\
    .apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d').strftime("%Y%m"))

print('---------------')
print(reserve_tb)

summary_result=pd.merge(
    customer_mst,
    reserve_tb[['customer_id', 'year_month', 'total_price']],
    on=['customer_id', 'year_month'], how='left').groupby(['customer_id','year_month'])['total_price']\
    .sum().reset_index()

summary_result.fillna(0, inplace=True)


print('---------------')
print(summary_result)


