print("############################################")
print("##  8.1. 자료형 변환하기        ")
print("############################################")

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

#reserve_tb=pd.read_csv('./data/reserve.csv', encoding='UTF-8')

print(type(40000/3))
print(int(40000/3))
print(float(40000/3))

df=pd.DataFrame({'value':[40000/3]})

print(df.dtypes)

print(df['value'].astype('int8')  )
print(df['value'].astype('int16')  )
print(df['value'].astype('int32')  )
print(df['value'].astype('int64')  )

print(df['value'].astype('float16')  )
print(df['value'].astype('float32')  )
print(df['value'].astype('float64')  )
#print(df['value'].astype('float128')  )


print(df['value'].astype('int')  )
print(df['value'].astype('float')  )

print('---------------')


