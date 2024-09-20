# TV Kumandası Simülasyonu

Bu Python projesi, bir TV kumandasının temel işlevlerini simüle eder. Program, ses ayarı, kanal ekleme/silme, rastgele kanal seçme, favori kanallar ve kanal geçmişi gibi temel TV kontrol fonksiyonlarını sunar.

## Özellikler

- **TV Açma/Kapama**: TV'yi açabilir veya kapatabilirsiniz.
- **Ses Ayarlama**: Ses seviyesini artırabilir veya azaltabilirsiniz (0-31 arası).
- **Kanal Ekleme/Silme**: İstediğiniz kanalı ekleyip silebilirsiniz. Program büyük/küçük harf duyarsızdır, yani `NTV` ile `ntv` aynı kabul edilir.
- **Rastgele Kanal**: Mevcut kanal listesinden rastgele bir kanal seçer.
- **Favori Kanal Listesi**: Kanalları favori listenize ekleyebilir ve favori kanalları listeleyebilirsiniz.
- **Kanal Geçmişi**: Son izlenen kanalları görüntüleyebilirsiniz.
- **TV Durumu**: TV'nin o anki durumunu (açık/kapalı), ses seviyesini, mevcut kanal listesini ve izlenen son kanalı görüntüleyebilirsiniz.

### Gereksinimler

- Python 3.x

### Kurulum

1. Projeyi yerel makinenize klonlayın:

   ```bash
   git clone https://github.com/kullaniciadi/tv-remote-simulation.git
   ```

2. Python dosyasını çalıştırın:

   ```bash
   python tv_remote.py
   ```

### Kullanım

Program çalıştırıldığında aşağıdaki menü karşınıza çıkacaktır:

```
    1. TV aç
    2. TV kapat
    3. Ses ayarla
    4. Kanal ekle
    5. Kanal sil
    6. Rastgele kanal
    7. Favori kanallar
    8. Favori ekle
    9. Kanal geçmişi
    10. TV bilgisi
    Çıkmak için "q" yazın
```

İstediğiniz seçeneği girerek ilgili işlemi gerçekleştirebilirsiniz.

### TV Kumandası İşlevleri

1. **TV Aç/Kapat**: TV'nin açık olup olmadığını kontrol eder. TV açık değilse, açar. Kapalı değilse, kapatır.
2. **Ses Ayarlama**: `<` tuşu ile sesi kısabilir, `>` tuşu ile sesi artırabilirsiniz. `q` ile ses ayarlama modundan çıkabilirsiniz.
3. **Kanal Ekleme**: Birden fazla kanal ekleyebilirsiniz. Kanalları eklerken aralarına virgül koyarak birden fazla kanal girebilirsiniz.
4. **Kanal Silme**: Eklediğiniz kanallardan birini silebilirsiniz.
5. **Rastgele Kanal Seçme**: Kanal listenizdeki kanallardan rastgele birini seçer ve o kanalı gösterir.
6. **Favori Kanal Listesi**: Favori listenize kanal ekleyebilir ve mevcut favori kanallarınızı listeleyebilirsiniz.
7. **Kanal Geçmişi**: Daha önce izlediğiniz kanalların listesini görüntüleyebilirsiniz.
8. **TV Durumu**: TV'nin mevcut durumu (ses seviyesi, kanal listesi, izlenen kanal) hakkında bilgi alabilirsiniz.

## Özelleştirme

### Büyük/Küçük Harf Duyarsızlığı

Kanal isimleri kullanıcı tarafından nasıl girilirse girilsin (büyük veya küçük harf), program tüm kanalları küçük harfe çevirir ve bu şekilde işler. Böylece, `TRT` ve `trt` aynı kanal olarak kabul edilir.

### Favori Kanallar

İstediğiniz kanalları favori listenize ekleyebilirsiniz. Aynı kanalı birden fazla kez ekleyemezsiniz, ve eklenen kanal listeye küçük harf olarak kaydedilir.

### Kanal Geçmişi

Program, izlediğiniz kanalları takip eder ve bu kanalları kanal geçmişinde listeler. Rastgele kanal seçiminde veya manuel seçimde izlenen her kanal geçmişe eklenir.

## Katkıda Bulunma

Projeye katkıda bulunmak için:

1. Bu projeyi forklayın.
2. Yeni bir branch oluşturun: `git checkout -b yeni-ozellik`
3. Değişikliklerinizi commitleyin: `git commit -m 'Yeni özellik ekle'`
4. Branch'inize push yapın: `git push origin yeni-ozellik`
5. Bir pull request oluşturun.
