#############
# GÖREV 1
#############
# List Comprehension yapısı kullanarak car_crashes verisindeki numeric
# değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# Numeric olmayan değişkenlerin de isimleri büyümeli.
# Tek bir list comprehension yapısı kullanılmalı.
import seaborn as sns

df = sns.load_dataset("car_crashes")

numeric_columns = ['NUM_' + col.upper() if df[col].dtype in ['float64', 'int64'] else col for col in df.columns]

numeric_columns = [col for col in numeric_columns if col.startswith('NUM_')]

print(numeric_columns)

##############
# GÖREV 2
############
# List Comprehension yapısı kullanarak car_crashes verisinde isminde "no"
# barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# Tüm değişkenlerin isimleri büyük harf olmalı.
# Tek bir list comprehension yapısı ile yapılmalı.
import seaborn as sns

df = sns.load_dataset("car_crashes")

new_columns = [f'{col.upper()}_FLAG' if 'no' not in col else col.upper() for col in df.columns]

print(new_columns)

################
# GÖREV 3
################
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir data frame oluşturunuz
# Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz
# ve adını new_df olarak isimlendiriniz

import seaborn as sns

df = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]


