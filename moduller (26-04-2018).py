
#(karCiroHesabi) (modul)
def kar(gelir,gider):
    gelir=int(gelir)
    gider=int(gider)
    print("toplam işletme karı:",gelir-gider)

def adamBasiCiro(toplamCiro,toplamCalisan):
    toplamCiro=int(toplamCiro)
    toplamCalisan=int(toplamCalisan)
    print("Adam Başı Ciro:",toplamCiro/toplamCalisan)

#(birinci yöntem) modul_cagirma
from karCiroHesabi import*
kar(500,300)
adamBasiCiro(1000,300)

#(ikinci yöntem) modul_cagirma
from karCiroHesabi import*
x=(input("toplam gelirinizi girin:"))
y=(input("toplam giderinizi girin:"))
t=(input("toplam cironuzu girin:"))
z=(input("çalışan sayısını girin:"))
kar(x,y)
adamBasiCiro(t,z)


#(bilancoHesabi) (modul)
   
   
def aktif(kasa,alinanCek,bankaH,alacakSenetleri,ticariMal,binalar,tasitlar,demirbaslar):
    kasa=int(kasa)
    alinanCek=int(alinanCek)
    bankaH=int(bankaH)
    alacakSenetleri=int(alacakSenetleri)
    ticariMal=int(ticariMal)
    binalar=int(binalar)
    tasitlar=int(tasitlar)
    demirbaslar=int(demirbaslar)
    
    donenVarliklar=kasa+alinanCek+bankaH+alacakSenetleri+ticariMal
    print ("Dönen Varlıklar Toplamı:",donenVarliklar)
    
    duranVarliklar=binalar+tasitlar+demirbaslar
    print ("Duran Varlıklar Toplamı:",duranVarliklar)
    
    aktifToplami=donenVarliklar+duranVarliklar
    return aktifToplami



def pasif(bankaKredileri,saticilar,uzVadeliBankaKredileri,uzVadeliBorcSenedi,sermayeHesabi):
    bankaKredileri=int(bankaKredileri)
    saticilar=int(saticilar)
    uzVadeliBankaKredileri=int(uzVadeliBankaKredileri)
    uzVadeliBorcSenedi=int(uzVadeliBorcSenedi)
    sermayeHesabi=int(sermayeHesabi)

    
    kvyk=bankaKredileri+saticilar
    print("Kısa Vadeli Yabancı Kaynaklar Toplamı:",kvyk)
    
    uvyk=uzVadeliBankaKredileri+uzVadeliBorcSenedi
    print("Uzun Vadeli Yabancı Kaynaklar Toplamı:",uvyk)

    ozKaynaklar=sermayeHesabi
    print("Toplam Öz Kaynaklar:",ozKaynaklar)
    
    pasifToplami=kvyk+uvyk+ozKaynaklar
    return pasifToplami

    
#(modul_cagirma)
from bilancoHesabi import*
aktifler=aktif(20000,10000,5000,28000,65000,150000,25000,8000)
pasifler=pasif(42000,60000,35000,115000,59000)
if aktifler==pasifler:
    print("bilanço doğru hesaplanmıştır.","aktif toplamı:",aktifler,"pasif toplami:",pasifler)
else:
    print("bilanço yanlış hesaplanmıştır.","aktif toplamı:",aktifler,"pasif toplami:",pasifler)
	


#(grup_etkileşim_oranı) (modul)

def etkilesim(begeniSayisi,yorumSayisi,paylasimSayisi,icerikSayisi,takipciSayisi):
    begeniSayisi=int(begeniSayisi)
    yorumSayisi=int(yorumSayisi)
    paylasimSayisi=int(paylasimSayisi)
    icerikSayisi=int(icerikSayisi)
    takipciSayisi=int(takipciSayisi)  
    etkilesimOrani=(((begeniSayisi + yorumSayisi + paylasimSayisi)/icerikSayisi)/takipciSayisi) * 100
    print("etkileşim oranı:", etkilesimOrani)
    return
  

#(modul_cagirma)

from etkilesimOrani import*
i=0
grup=""
while (i<3):
    grup=input("grup adı:")
    begeni=input("aylık ortalama beğeni sayısı:")
    yorum=input("aylık ortalama yorum sayısı:")
    paylasim=input("aylık ortalama paylaşım sayısı:")
    icerik=input("aylık ortalama içerik sayısı:")
    takip=input("aylık ortalama takipçi sayısı:")    
    print(etkilesim(begeni,yorum,paylasim,icerik,takip))
    y=etkilesim(begeni,yorum,paylasim,icerik,takip)
    d=0.20
    if y >= d:
        print("etkileşim oranı yüksek")
    else:
        print("etkileşim oranı düşük")
    i=i+1






    
   

  






    

    





