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

