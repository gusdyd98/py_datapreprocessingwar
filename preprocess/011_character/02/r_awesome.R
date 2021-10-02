library(dplyr)
source('preprocess/load_data/data_loader.R')

load_txt_df()

# 아래 부터 책에 게재
library(RMeCab)

# poc引数で対象の品詞を指定
# typeは文字単位または単語単位のどちらかを指定(単語単位の処理は、1)
word_matrix <- docDF('data/txt', pos=c('NNG', 'NNP','NNB','VV'), type=1)


