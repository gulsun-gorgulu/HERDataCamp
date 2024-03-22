# Pandas Alıştırmalar
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()
# Görev 2: Titanic verisetindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()
# Görev3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()
# Görev4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
df["pclass"].nunique()
# Görev5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[['pclass', 'parch']].nunique()
# Görev6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
embarked_dtype_before = df["embarked"].dtype

if embarked_dtype_before != "category":
    df["embarked"] = df["embarked"].astype("category")
embarked_dtype_before = df["embarked"].dtype
# Görev7: embarked değeri C olanların tüm bilgelerini gösteriniz.
embarked_c = df[df['embarked'] == 'C']
# Görev8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
not_embarked_s = df[df['embarked'] != 'S']
# Görev9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
young_females = df[(df['sex'] == 'female') & (df['age'] < 30)]
# Görev10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
high_fare_or_elderly_info = df[(df['fare'] > 500) | (df['age'] > 70)]
# Görev 11:  Her bir değişkendeki boş değerlerin toplamını bulunuz.
missing_values = df.isnull().sum()
# Görev 12:  who değişkenini dataframe’den çıkarınız.
df.drop(columns='who', inplace=True)
# Görev13:  deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri(mode) ile doldurunuz.
deck_mode = df['deck'].mode()[0]
df['deck'] = df['deck'].fillna(deck_mode)
# Görev14:  age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
age_median = df['age'].median()
df['age'] = df['age'].fillna(age_median)
# Görev15:  survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
survived_grouped_stats = df.groupby(['pclass', 'sex'])['survived'].agg(['sum', 'count', 'mean'])

# Görev16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyon ukullanarak titanik veri setinde age_flag adında bir değişken oluşturunuzoluşturunuz.
# (apply ve lambda yapılarını kullanınız)
df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)
df.head()

# Görev17:  Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
tips_sample = sns.load_dataset("tips")
tips_sample.head()
#
##### Görev18:  Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
tips_grouped_by_time = tips_sample.groupby('time')['total_bill'].agg(['sum', 'min', 'max', 'mean'])
print(tips_grouped_by_time)
# Görev19: Günlere ve time göre total_bill değerlerini n toplamını, min, max ve ortalamasını bulunuz
tips_grouped_by_day_and_time = tips_sample.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean'])
print(tips_grouped_by_day_and_time)
# Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
lunch_female_grouped = tips_sample[(tips_sample['time'] == 'Lunch') & (tips_sample['sex'] == 'Female')] \
    .groupby('day', observed=True) \
    .agg({
        'total_bill': ['sum', 'min', 'max', 'mean'],
        'tip': ['sum', 'min', 'max', 'mean']
    })

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
average_bill_conditioned = tips_sample.loc[(tips_sample['size'] < 3) & (tips_sample['total_bill'] > 10), 'total_bill'].mean()

# Görev22:  total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği total bill ve tip in toplamını versin.
tips_sample['total_bill_tip_sum'] = tips_sample['total_bill'] + tips_sample['tip']

# Görev23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir data frame'e atayınız
sorted_tips_sample = tips_sample.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
