# def topla(a,b):
#     return print("Sayıların toplamı=",a+b)

meyveler=[] #meyve dizini(sepet)
ekle=input("meyve ekle:") # 1.ekle
meyveler.append(ekle)
while True:
    secim=input("yeni bir ürün eklemek istermisiniz e/h:")
    if secim=='e':
        ekle=input("meyve ekle:") # 1.ekle
        meyveler.append(ekle) # 1. ürünü sepetin içine ekle
    else:
        print("ürün ekleme işlemi bitti..")
        break
print(meyveler) # eklediğin ürünleri listele
