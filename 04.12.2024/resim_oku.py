import cv2 as cv
resim=cv.imread(r'C:\Users\Mehmet\projegoruntuisleme\Demo\resim.png')
# Eğer resim başarılı bir şekilde okunmuşsa
if resim is not None:
    # Resmi görüntüle    
    cv.imshow('Resim', resim)
    
    # Bir tuşa basılana kadar bekleme
    cv.waitKey(0)
    
    # Pencereleri kapatma
    # cv.destroyAllWindows()
else:
    print("Resim bulunamadı!")

