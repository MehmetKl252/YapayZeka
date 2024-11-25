class Ogrenci:
    def __init__(self, ad, soyad):
        self.ad=ad
        self.soyad=soyad
class Egitmen:
    def __init__(self, ad, soyad):
        self.ad=ad
        self.soyad=soyad
class Bolum:
    def __init__(self, bolum):
        self.bolum=bolum
class Sinif:
    def __init__(self, sinif):
        self.sinif=sinif
class Ders:
    def __init__(self, ders):
        self.ders=ders
#//////// kullanıcı veri girişi////////////////
veri_ad=input("öğrenci adı:")
veri_soyad=input("öğrenci soyadı:")
veri_ead=input("öğretmen adı:")
veri_esoyad=input("öğretmen soyadı:")
veri_bolum=input("bölüm adı:")
veri_sinif=input("sınıf adı:")
#///////////girilen verileri sınıfa atama//////////////
ogrenci=Ogrenci(veri_ad,veri_soyad)
egitmen=Egitmen(veri_ead,veri_esoyad)
bolum=Bolum(veri_bolum)
sinif=Sinif(veri_sinif)
dersler=[]
while True:
    ders_ekle=input("ders ekle:")
    ders=Ders(ders_ekle)
    dersler.append(ders_ekle)
    ekle=input("farklı bir ders eklemek istermisiniz:e/h:")
    if ekle=='h':
        break
print(f'öğrenci adı soyadı:{veri_ad} {veri_soyad}\neğitmen adı:{veri_ead} {veri_esoyad}')
print(f'bölüm:{veri_bolum}\nsınıfı:{veri_sinif}')
print(f'dersler:{dersler}')


