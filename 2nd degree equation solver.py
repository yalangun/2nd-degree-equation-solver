print("2. derece denklem çözücü")
from math import sqrt
a = 0
b = 0
c = 0
        
x = input("lütfen değişken giriniz:")
            
while(len(x) != 1):
    x = input("tek karakterli değişken giriniz:")
            
while True:
    try:
        soru_sayac = int(input("Kaç terim girilecek? "))
        if soru_sayac > 0:
            break
        else:
            print("Lütfen sıfırdan büyük bir sayı giriniz.")
    except ValueError:
        print("Lütfen sadece sayı giriniz.")
        
            
terimler = []
katsayılar = []
katsayı = "" 
kod = 0
            
for n in range(soru_sayac):
                terim = input("lütfen terim giriniz.(örn: 5x^^2 , 78x , -42): ")
                terimler.insert(1,terim)
            
for n in range(soru_sayac):
                 terim = terimler[n]
                 for i in range(len(terim)):
                    if terim[i] == x:
                       if len(terim) - 1 != i:
                            katsayı = terim[:i]
                            if katsayı == '':
                                a += 1
                                break
                            if katsayı == '-':
                                a += -1
                                break
                            a += int(katsayı)
                            break
                       else:
                            katsayı = terim[:i]
                            if katsayı == '':
                                b += 1
                                break
                            if katsayı == '-':
                                b += -1
                                break
                            b += int(katsayı)
                            break
                    elif len(terim) - 1 == i:
                        katsayı = terim
                        c += int(katsayı)
            
delta = b**2 - 4*a*c
            
if(delta < 0):
                print("denklemin reel kökü yoktur")
elif(a == 0):
                cevab = -b/c
                print(cevab)
else:
            
                diskriminant1 = (-b + sqrt(delta))/ (2*a)
                diskriminant2 = (-b - sqrt(delta))/ (2*a)
                
                print(diskriminant1,diskriminant2)


