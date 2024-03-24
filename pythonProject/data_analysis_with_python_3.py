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


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                         "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("###########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("mdklgnvdskgvjkldffkjngf")
    else:
        cat_summary(df, col, plot=True)


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)


##############################################
# 3.Sayısal Değişken Analizi (Analysis of Numerical Variables)
##############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()



cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
cat_but_car =[ col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in [["category", "object"]]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[["age", "fare"]].describe().T
num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]
num_cols = [col for col in num_cols if col not in cat_cols]

def num_summary(dataframe, numerical_col):
    quantiles=[0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)



def num_summary(dataframe, numerical_col, plot= False):
    quantiles=[0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(num_cols)
        plt.show(block= True)
num_summary(df, "age", plot=True)

for col in num_cols:
    num_summary(df,col, plot=True)


##############################################
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
##############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

#docstring
def grab_col_names(dataframe, cat_th=10, car_th=20):

    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isim

    Parameters
    ----------
    dataframe: dataframe
         değişken isimleri alınmak istenen dataframe'dir
    cat_th: int, float
         numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
         kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
        cat_cals: list
                Kategorik değişken listesi
        num_cols:list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Notes
    --------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_car cat_col'un içerisinde.

    """

help(grab_col_names)







