#################################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
#################################################
import numpy as np
#################
# MATPLOTLIB
################
# Kategorik değişken: sütun grafik. Countplot bar
# Sayısal değişken: hist, boxplot

####################################
# Kategorik değişken Görselleştirme
####################################
import pandas as pd
import seaborn as sns
import  matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

#Bu iki grafik istatistiksel iki grafiktir. Yani bir veriyi tanımaya çalışırken asıl
# amacımız değişkenlerin dağılım yapılarını gözlemlemektir.
# Bu sebebple histogram ve kutu grafik bize hem sayısal değişkenin hangi aralıklarında
# hangi frekanslarda gözlemler var bunu gösterir, hem de veri setinin içindeki bu değişkenin kendi
# İçindeki dağılım bilgisini ve bu dağılıma göre ne kadar aykırı değer olabileceği bilgisini gösterir

#####################################
# Matplotlib'in Özellikleri
#####################################

#########
#plot
########
#Veriyi görselleştirmek için kullandığımız fonksiyonlardan birisidir.

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6,8,10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

#############
# marker
#############

y = np.array([13,28,11, 100])

plt.plot(y, 'o')
plt.show()

plt.plot( y, '*')
plt.show()

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

##############
# line
#############

y = np.array([13,28,11, 100])

plt.plot(y, linestyle = "dashed")
plt.show()


plt.plot(y, linestyle = "dotted")
plt.show()
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)
#####################
# Subplots
####################
import numpy as np
import pandas as pd
import seaborn as sns
import  matplotlib.pyplot as plt

#plot1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

#plot2
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

#plot3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()

######################
# SEABORN
######################

import numpy as np
import pandas as pd
import seaborn as sns
import  matplotlib.pyplot as plt
df =  sns.load_dataset("tips")
df.head()

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

#matplotlib versiyonu
df['sex'].value_counts().plot(kind='bar')
plt.show()

#################################
# Sayısal Değişken Görselleştirme
#################################
sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()

## ORNEK ##
import seaborn as sns
df = sns.load_dataset("tips")
sns.scatterplot(x=df["tip"], y=df["total_bill"],
                hue=df["smoker"], data=df)
plt.show()

#sns.boxplot ile çizdirilen bir grafikte aşağıdakilerden hangisi gözlemlenemez?
#Aykırı değerler
#Standart sapmanın 1.5 katına tekabül eden değerler (GÖZLENMEZ)
#Median değer
#Mean(ortalama) değer


#df.plot.barh() kodu aşağıdakilerden hangisini temsil eder? Yatay bar grafiği

#Bir değişkende 'outlier' olup olmadığını grafikten bakarak tespit etmek istiyorsak
# aşağıdakilerden hangisi en uygun grafik çeşididir?  sns.boxplot