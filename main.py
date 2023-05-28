class MuzikAleti:
    def _init_(self, isim, sesKalitesi, notalarArasiUyum, calinabilirlik):
        self.isim = isim
        self.sesKalitesi = sesKalitesi
        self.notalarArasiUyum = notalarArasiUyum
        self.calinabilirlik = calinabilirlik

def benzerlik(alet1, alet2):
    sesKalitesiFark = alet1.sesKalitesi - alet2.sesKalitesi
    notalarArasiUyumFark = alet1.notalarArasiUyum - alet2.notalarArasiUyum
    calinabilirlikFark = alet1.calinabilirlik - alet2.calinabilirlik
    benzerlikDegeri = sesKalitesiFark * sesKalitesiFark + notalarArasiUyumFark * notalarArasiUyumFark + calinabilirlikFark * calinabilirlikFark
    return benzerlikDegeri

def kumeleme(aletler, aletSayisi, kumeSayisi):
    kumeler = aletler[:kumeSayisi]

    for i in range(aletSayisi):
        enKucukBenzerlik = benzerlik(aletler[i], kumeler[0])
        enYakinKume = 0

        for j in range(1, kumeSayisi):
            b = benzerlik(aletler[i], kumeler[j])
            if b < enKucukBenzerlik:
                enKucukBenzerlik = b
                enYakinKume = j

        print(f"{aletler[i].isim}, {enYakinKume + 1} numaralı kümeye sınıflandırıldı.")

aletSayisi = int(input("Kaç adet müzik aleti gireceksiniz? "))
aletler = []

for i in range(aletSayisi):
    isim = input(f"{i + 1}. müzik aletinin adını girin: ")
    sesKalitesi = float(input(f"{i + 1}. müzik aletinin ses kalitesi değerini girin (0-10 arası): "))
    notalarArasiUyum = float(input(f"{i + 1}. müzik aletinin notalar arası uyum değerini girin (0-10 arası): "))
    calinabilirlik = float(input(f"{i + 1}. müzik aletinin çalınabilirlik değerini girin (0-10 arası): "))

    alet = MuzikAleti(isim, sesKalitesi, notalarArasiUyum, calinabilirlik)
    aletler.append(alet)

kumeSayisi = int(input("\nKaç adet küme oluşturmak istiyorsunuz? "))

kumeleme(aletler, aletSayisi, kumeSayisi)
