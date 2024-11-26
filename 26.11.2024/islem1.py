gorev_listesi=[]
# Görev ekleme fonksiyonu
def gorev_ekle(gorev_listesi):
    gorev=input("görev ekle:")
    gorev_listesi.append(gorev)
    print("görev başarı ile eklendi..")
# Görev silme fonksiyonu
def gorev_sil(gorev_listesi):
    gorev=input("silinecek görev adı:")
    if gorev in gorev_listesi:
        gorev_listesi.remove(gorev)
        print("gorev başarı ile silindi!!")
    else:
        print("görev adı bulunamadı")
# Görev listeleme fonksiyonu
def gorev_goruntule(gorev_listesi):
    print("eklenen görevler:")
    for i in gorev_listesi:
        print("-",i)
    if not i in gorev_listesi:
        print("öğe bulunamadı..")
while True:
    print("işlem sıralaması:\ngörev ekle(1):\ngorev sil(2):\ngorev listele(3):")
    secim=input("işlem seçiniz:")
    if secim=='1':
        gorev_ekle(gorev_listesi)
    elif secim=='2':
        gorev_sil(gorev_listesi)
    elif secim=='3':
        gorev_goruntule(gorev_listesi)
    else:
        print("yanlış görev seçtiniz..")




