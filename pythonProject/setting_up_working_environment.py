##############################################
# Sayılar (Numbers) ve Karakter Dizileri(Strings)
##############################################

print("Hello world")
print("Hello AI Era")

print(9)
var = 9.2

type(9.2)

##############################################
# Atamalar ve Değişkenler (Assignments & Variables)
##############################################

a = 9
print(a)

b = "hello ai era"
print(b)


c = 10

variable2 = a * c

variable1 = a - c

d = a - c

# Virtual Environment (Sanal Ortam) Nedir?
# İzole çalışma ortamları oluşturmak için kullanılan araçlardır.
# Farklı çalışmalar için oluşabilecek farklı kütüphane ve versiyon ihtiyaçlarını
# çalışmalar birbirini etkilemeyecek
# şekilde oluşturma imkanı sağlar.

# Virtual Environment (Sanal Ortam) oluşturmak için kullanılan araçlardan bazıları:
# * venv
# * virtualenv
# * pipenv
# * conda

# Package Management (Paket Yönetimi) Nedir?
# Paket/modül/kütüphane yönetimi:

# Package Management (Paket Yönetimi) araçlardan bazıları:
# * pip (requirements.txt)
# * pipenv (Pipfile)
# * conda (environment.yaml)

# Conda:
# 1. Paket yönetimi
# 2. Bağımlılık yönetimi

# * venv ve * virtualenv - paket yönetim aracı olarak pip'i kullanıyor.
# * venv
# * virtualenv

# * pipenv ve * conda - hem paket yönetimi, hem virtual environment yönetimi yapabiliyor.
# * pipenv
# * conda

# Sonuç:
# * conda - package management ve virtual environment yönetimi için kullanılabilir.
# * pip - package management için kullanılabilir.
# * conda > * pip


##############################################
# Sanal Ortam (Virtual Environment) ve Paket Yönetimi (Package Management)
##############################################

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create -n myenv

# Sanal ortamı aktiv etme:
# conda activate myenv

# Sanal ortamı deaktiv etme:
# conda deactivate

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme (numpy):
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme (numpy):
# conda remove package_name

# Belirli bir versiyona göre paket yükleme (numpy): (P.s. pip-de iki == kullanılır, conda-da bir =)
# conda install numpy=1.20.1

# Paket yükseltme (numpy):
# conda upgrade package_name

# Tüm paketlerin yükseltilmesi:
# conda upgrade -all


# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme (pandas):
# pip install pandas

# Paket yükleme versiyona göre (pandas): (P.s. pip-de iki == kullanılır, conda-da bir =)
# pip install pandas==1.2.1
