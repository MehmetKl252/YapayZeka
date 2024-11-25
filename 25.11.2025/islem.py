gorev_listesi=[]
def gorev_ekle(gorev_listesi):
    gorev=input("görev ekle:")
    gorev_listesi.append(gorev)
    print("görev başarı ile eklendi..")

def gorev_goruntule(gorev_listesi):
    print("eklenen görevler:")
    for i in gorev_listesi:
        print("-",i)
while True:
    print("işlem sıralaması:")
    print("görev ekle(1):")
    print("gorev listele(2):")
    secim=input("işlem seçiniz:")
    if secim=='1':
        gorev_ekle(gorev_listesi)
    elif secim=='2':
        gorev_goruntule(gorev_listesi)
    else:
        print("yanlış görev seçtiniz..")




