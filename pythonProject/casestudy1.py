###################
# GÖREV 1
###################
# Verilen değerlerin veri yapılarını inceleyiniz.
# Type() metodunu kullanınız.


x = 8
type(x)

x = 3.2
type(x)

x = 8j + 18
type(x)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

################
# GÖREV 2
################
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
# String metodlarını kullanınız.


text = "The goal is to turn data into information, and information into insight."

text_upper = text.upper()
text_replaced = text_upper.replace(',', ' ').replace('.', ' ')

words_list = text_replaced.split()

words_output = [f'{word}' for word in words_list]

words_output

############
# GÖREV 3
############
# Verilen listeye aşağıdaki adımları uygulayınız.
# Adım1: Verilen listenin eleman sayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım4: Sekizinci indeksteki elemanı siliniz.
# Adım5: Yeni bir eleman ekleyiniz.
# Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

element_count = len(lst)

first_element = lst[0]
tenth_element = lst[9]

elements_to_remove = ["D", "A", "T", "A"]
lst = [element for element in lst if element not in elements_to_remove]

del lst[8]

lst.append("X")

lst.insert(8, "N")  # Adding 'N' at the seventh index

# Yapılan değişikliklerin hepsinin çıktısı
(element_count, first_element, tenth_element, lst)

#############
# GÖREV 4
#############
# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# Adım1: Key değerlerine erişiniz.
# Adım2: Value'lara erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım5: Antonio'yu dictionary'den siliniz.


dict_info = {
    'Christian': ['America', 18],
    'Daisy': ['England', 12],
    'Antonio': ['Spain', 22],
    'Dante': ['Italy', 25]
}

keys = list(dict_info.keys())

values = list(dict_info.values())

dict_info['Daisy'][1] = 13

dict_info['Ahmet'] = ['Turkey', 24]

del dict_info['Antonio']

###############
# GÖREV 5
###############
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere
# atayan ve bu listeleri return eden fonksiyon yazınız.
# Liste elemanlarına tek tek erişmeniz gerekmektedir.
# Her bir elemanın çift veya tek olma durumunu kontrol etmekiçin % yapısını kullanabilirsiniz.


l = [2, 13, 18, 93, 22]


def separate_even_odd(numbers):
    even_list = [num for num in numbers if num % 2 == 0]
    odd_list = [num for num in numbers if num % 2 != 0]
    return even_list, odd_list


even_list, odd_list = separate_even_odd(l)

#############
# GÖREV 6
############
# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin
# isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını
# temsil ederken son üç öğrencide tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak
# öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


def format_output(students):
    output = []
    # Engineering students
    for i in range(3):
        output.append(f"Mühendislik Fakültesi {i + 1}. öğrenci: {students[i]}")
    # Medical students
    for i in range(3, 6):
        output.append(f"Tıp Fakültesi {i - 2}. öğrenci: {students[i]}")
    return "\n".join(output)


formatted_students = format_output(ogrenciler)
print(formatted_students)
 # 2.yol

for i, x in enumerate(ogrenciler,1):
    if i<4:
        print("Mühendislik Fakültesi",i, ". öğrenci:",x)
        i+=1
    else:
        i-= 3
        print("Tıp Fakültesi", i, ". öğrenci: ",x)


# 3. yol
[print("Mühendislik Fakültesi{}. öğrenci: {}".format(index,values)) ,if index<4]

############
# GÖREV 7
############
# Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri
# yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.

# Verilen listeler
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

# Zip fonksiyonu ile listeleri birleştirip her bir ders için string formatlama
ders_bilgileri = zip(ders_kodu, kredi, kontenjan)
formatted_output = [
    f"Kredisi {k} olan {dk} kodlu dersin kontenjanı {ko} kişidir."
    for dk, k, ko in ders_bilgileri
]

# Formatlanmış çıktıları birleştirip yazdırma
output_str = "\n".join(formatted_output)
print(output_str)

#########
# 2.YOL
########
for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")
#############
# GÖREV 8
#############
# Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1.küme 2.kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2.kümenin 1.kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
# Kapsayıp kapsamadığını kontrol etmek için issuperset() metodunu, farklı ve ortak elemanlar için ise
# intersection ve difference metodlarını kullanınız.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])
def check_sets_and_return_unique(k1, k2):
    if k1.issuperset(k2):
        return k1.intersection(k2)
    else:
        return k2.difference(k1)

unique_from_kume2 = check_sets_and_return_unique(kume1, kume2)
unique_from_kume2

# 2.yol
def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)
kume(kume2, kume1)

