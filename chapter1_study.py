import pandas as pd

reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

print(reserve_tb.head())

print("############################################")
print("##  예제2.xx                     ")
print("############################################")
print(reserve_tb.iloc[:, 0:6])

pd.set_option('display.max_columns', None)

print(reserve_tb[['checkin_date', 'checkin_time','checkout_date',
                  'reserve_id', 'hotel_id', 'customer_id',
                  'reserve_datetime' ]])

print(reserve_tb[['reserve_id', 'hotel_id', 'customer_id',
            'reserve_datetime', 'checkin_date', 'checkin_time',
            'checkout_date']])

print(reserve_tb.loc[:, ['reserve_id', 'hotel_id', 'customer_id',
                  'reserve_datetime', 'checkin_date', 'checkin_time',
                  'checkout_date']])

print(reserve_tb.drop(['people_num', 'total_price'], axis=1, inplace=True))

print("############################################")
print("##  59page. 조건에 맞는 행 추출                ")
print("############################################")
import pandas as pd

pd.set_option('display.max_columns', None)

print(reserve_tb[(reserve_tb['checkout_date'] >= '2016-10-13') &
           (reserve_tb['checkout_date'] <= '2016-10-14')])

print("------------------------")
print(reserve_tb.loc[(reserve_tb['checkout_date'] >= '2016-10-13') &
                 (reserve_tb['checkout_date'] <= '2016-10-14'), :])

print("------------------------")
print(reserve_tb.query(' "2016-10-13" <= checkout_date <= "2016-10-14" '))


print("############################################")
print("##  62page. 데이터 값을 고려하지 않는 샘플링             ")
print("############################################")
import pandas as pd

pd.set_option('display.max_columns', None)

