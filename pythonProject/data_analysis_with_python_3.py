##########################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ANVANCED FUNCTIONAL EDA)
##########################################
# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
# 5. Korelasyon Analizi (Analysis of Correlation)

##########################################
# 1. Genel Resim
##########################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe, head=5):
    print("######################## Shape ##########################")
    print(dataframe.shape)
    print("######################## Types ##########################")
    print(dataframe.dtypes)
    print("######################## Head ##########################")
    print(dataframe.head(head))
    print("######################## Tail ##########################")
    print(dataframe.tail(head))
    print("######################## NA ##########################")
    print(dataframe.isnull().sum())
    print("######################## Quanties ##########################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

df = sns.load_dataset("tips")
check_df(df)
df = sns.load_dataset("flights")
check_df(df)

#####################################################
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
#####################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

#Tek bir değişkeni analiz etmek istiyorsak value_counts() kullanırız
df["embarked"].value_counts()

#Fonksiyonel şekilde genellenebilirlik kaygısıyla değişken tiplerini yakalayacak ve bunların özelinde analiz yapacak
# bir fonksiyon yazma işlemi gerçekleştireceğiz.
# Elimize bir kategorik değişken geldiğinde önce tek bir değişkeni analiz etmek  istediğimizde,
# örneğin value_counts() fonksiyonunu kullanarak sınıf sayılarına erişebiiriz
# Elimizdeki örneğin, bir başka değişkenin unique değerlerine erişmek istersek unique() fonksiyonunu kullanabiliriz.

df["sex"].unique()
df["sex"].nunique()
df["class"].nunique()

# Bu veri setinin içerisinden otomatik bir şekilde bana bütün olası kategorik değişkenleri seçsin

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# Tipi integere ya da float olan değişkenleri bul. Bunların eşsiz sayısına bak.
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

cat_but_car =[ col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in [["category", "object"]]]

cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]
df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]

df["embarked"].value_counts()
100 * df["embarked"].value_counts() / len(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("###########################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)
