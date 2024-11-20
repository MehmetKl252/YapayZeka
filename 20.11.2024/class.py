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

veri_ad=input("öğrenci adı:")
veri_soyad=input("öğrenci soyadı:")
veri_ead=input("eğitmen adı:")
veri_esoyad=input("eğitmen soyadı:")
veri_bolum=input("bölüm adı:")
veri_sinif=input("sınıfınızı giriniz:")

ogrenci=Ogrenci(veri_ad,veri_soyad)
egitmen=Egitmen(veri_ead, veri_esoyad)
sinif=Sinif(veri_sinif)
bolum=Bolum(veri_bolum)

dersler=[]
while True:
    ekle_ders=input("ders ekle:") #başlık
    ders=Ders(ekle_ders) # class-sınıf
    dersler.append(ekle_ders) # ders ekleme
    ekle=input("yeni bir ders eklemek istermisiniz(e/h):")
    if ekle=='h':
        break
#///////////Ders ekleme listesi//////////////////////
print("öğrenci adı:",veri_ad,veri_soyad)
print("eğitmen adı:",veri_ead,veri_soyad)
print("sınıf:",veri_sinif)
print("bölüm:",veri_bolum)
print("seçtiğiniz dersler:",dersler,"\n")