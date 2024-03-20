####################
# NUMPY
####################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attributes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# İndex Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
# klasik python yolu
ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# numpy yolu
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

#################################
# NumPy Array'i Oluşturmal  (Creating numpy arrays)
#########################

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))

##############################################
#   NumPy Array Özellikleri (Attributes of Numpy Arrays)
###############################################

import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype

############
# Yeniden Şekillendirme (Reshaping)
############

import numpy as np

np.random.randint(1, 10, size= 9)
np.random.randint(1, 10, size= 9).reshape(3, 3)

ar = np.random.randint(1, 10, size= 9)
ar.reshape(3, 3)

####################
# Index Seçimi ( Index Selection
####################
import numpy as np

a= np.random.randint(10, size =10)
a[0]
a [0:5]
a[0] = 999

m = np.random.randint(10, size =(3, 5))
m[0, 0]
m[2,3]

m[:, 0]

m[0:2, 0:3]

#############
#Fancy Index
############

import numpy as np

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [1, 2, 3]
v[catch]

#################################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#################################################

import numpy as np
v= np.array([1, 2, 3, 4, 5])

############
#Klasik Döngü
############

ab = []
for i in v:
    if i < 3:
        ab.append(i)


##########
#Numpy ile
#########
v < 3
v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]

###########################################
#Matematiksel İşlemler (Mathematical Operations)
###########################################
import numpy as np
v= np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v,1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

###############################
# Numpy ile İki bilinmeyenli denklem Çözümü
################################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5,1], [1,3]])
b = np.array([12,10])

np.linalg.solve(a,b)


################################
# PANDAS
################################
#Pandas Serisi (Pandas Series)
#Veri Okuma (Reading Data)
#Veriye Hızlı Bakış (Quick Look at Data)
#Pandas'ta Seçim İşlemleri (Selection in Pandas)
#Toplulaştırma ve Gruplama (Aggregation & Grouping)
#Apply ve Lambda
#Birleştirme (Join) İşlemleri

################################
#Pandas Serisi (Pandas Series)
################################

import pandas as pd

s =pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)


############################
# Veri Okuma (Reading Data)

import pandas as pd

df = pd.read_csv("pythonProject4/datasets/Advertising.csv")

df.head()

################################
# Veriye Hızlı Bakış (Quick Look at Data)
###############################

import pandas as pd
import seaborn as sns

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
df["sex"].head()

####################################
# pandas'ta Seçim İşlemleri (Selection in Pandas)
####################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0,axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# df = df.drop(delete_indexes, axis=0) ----> Değişikliği kalıcı olarak siler
# df.drop(delete_indexes, axis=0, inplace=True) -----> Methodun kalıcı olması gerektiği bilgisini veren bir argüman/parametredir.

############################
# Değişkeni Indexe Çevirmek
############################

df["age"].head()
df.age.head()

df.index = df["age"]

#silme işlemi sütun olacağı için 1 diyoruz satır olsaydı 0 derdik

df.drop("age", axis=1).head()

#kalıcı silme
df.drop("age", axis=1, inplace=True)
df.head()
df.reset_index().head()
#################
# Indexi Değişkene Çevirmek
################
df.index
df["age"]= df.index

df.head()

#2.yol
df.reset_index().head()
df = df.reset_index()
df.head()

#####################################
# Değişkenler Üzerinde İşlemler
#####################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

"age" in df  #bu dataframe bu dataset içerinde var mı sorusuna cevap verir
df["age"].head()
df.age.head()

type(df["age"].head()) #ÖNEMLİ#

df[["age"]].head() # iki tane köşeli parantez kullanıyoruz
# 1-Değişken seçerken sonucu seri ya da dataframe olarak alabilirsiniz.
# 2-Köşeli parantez girmeniz durumunda veri yapısı bozulmaz ve dataframe olmaya devam eder.

type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]


df["age2"] = df["age"]**2
df["age3"] =df["age"] / df["age2"]

# Silme İşlemi
df.drop("age3", axis=1).head()

# Kalıcı Silme
df.drop(col_names, axis=1).head()

# Veri setinde belirli bir string ifadeyi barındıran değişkenleri silmek istiyorum

df.loc[:, ~df.columns.str.contains("age")].head()

#######################
# iloc & loc
######################
# iloc: Numpy'dan, listelerden alışık olduğumuz klasik, integer based yani indeks bilgisi vererek seçim yapma işlemlerini ifade eder.
# Açılımı: Integer Based Selection
# loc: Mutlak olarak indekslerdeki label'lara göre seçim yapar.
# Açılımı: Label Based Selection
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# İloc: integer based selection
df.iloc[0:3]  #çıktısı 0 dan 3 e kadar yani 0,1,2 veriyor
df.iloc[0,0]

# loc: label based selection
df.loc[0:3] #çıktısı 0 dan 3 de dahil olarak yani 0,1,2,3 veriyor

df.iloc[0:3, 0:3]
df.loc[0:3, "age"]

# ! Satır ya da indekslerdeki değerlerin bizzat kendilerine
# göre seçim işlemi yapmak istersek bu durumda loc kullanıyoruz.
# Burada fancy kavramı da geçerliliğini korumaktadır

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

##########################
# Koşullu Seçim (Conditional Selection)
#########################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# Bu veri setinde yaşı 50 den büyük olanlara erişmek istiyoruz diyelim
df[df["age"] > 50].head()
# Bu veri setinde yaşı 50 den büyük olan kaç kişi var
df[df["age"] > 50]["age"].count()

# Bu veri setinde yaşı 50 den büyük olan kişilerin sınıf bilgisini elde etmek istersek
df.loc[df["age"] > 50, ["age", "class"]].head()

# Yaşı 50 den büyük erkekleri seçmek istersek
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

# Yolculuk için gemiye binilen limanı ifade eden embark_town değişkeni için örneğin Cherbourg limanı seçelim
df["embark_town"].value_counts()

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]



