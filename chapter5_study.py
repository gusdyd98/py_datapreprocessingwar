print("############################################")
print("##  5.1. 분할        ")
print("############################################")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

production_tb=pd.read_csv('./data/production.csv', encoding='UTF-8')

print(production_tb)

train_data, test_data, train_target, test_target =\
    train_test_split(production_tb.drop('fault_flg', axis=1),
                     production_tb[['fault_flg']],
                     test_size=0.2)

print('---------------')

print(train_test_split(production_tb.drop('fault_flg', axis=1),
                 production_tb[['fault_flg']],
                 test_size=0.2))

print('---------------')
print(train_data)

train_data.reset_index(inplace=True, drop=True)
test_data.reset_index(inplace=True, drop=True)
train_target.reset_index(inplace=True, drop=True)
test_target.reset_index(inplace=True, drop=True)

print('---------------')
print(train_data)
print('---------------')
print(test_data)
print('---------------')
print(train_target)
print('---------------')
print(test_target)


row_no_list=list(range(len(train_target)))
print('---------------')
print(row_no_list)

k_fold=KFold(n_splits=4, shuffle=True)
print('---------------')
print(k_fold)

for train_cv_no, test_cv_no in k_fold.split(row_no_list):
    train_cv=train_data.iloc[train_cv_no, :]
    print('---------------')
    print(train_cv)
    test_cv=train_data.iloc[test_cv_no, :]
    print('---------------')
    print(test_cv)

