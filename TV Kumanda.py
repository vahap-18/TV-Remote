import time
import random

class Command:
    MAX_VOLUME = 31
    MIN_VOLUME = 0
    
    def __init__(self):
        self.state = "off"
        self.volume = 0
        self.channel_list = ["trt", "ntv", "dmax"]  # Küçük harfle başlatıldı
        self.current_channel = None
        self.favorite_channels = []
        self.channel_history = []

    def tv_on(self):
        if self.state == "on":
            print("TV zaten açık!")
        else:
            print("TV açıldı.")
            self.state = "on"

    def tv_off(self):
        if self.state == "off":
            print("TV zaten kapalı!")
        else:
            print("TV kapatıldı...")
            self.state = "off"

    def adjust_volume(self):
        while True:
            answer = input("Ses azalt: '<' \n Ses artır: '>' \n Çıkış: 'q' ")
            if answer == '<' and self.volume > self.MIN_VOLUME:
                self.volume -= 1
                print("Ses:", self.volume)
            elif answer == '>' and self.volume < self.MAX_VOLUME:
                self.volume += 1
                print("Ses:", self.volume)
            elif answer == 'q':
                print("Ses ayarlamasından çıkılıyor.")
                break
            else:
                print("Geçersiz girdi veya ses aralığı dışında!")

    def add_channel(self, channel_name):
        channel_name = channel_name.strip().lower()  # Küçük harfe dönüştürüldü
        if channel_name not in self.channel_list:
            self.channel_list.append(channel_name)
            print(f"Kanal '{channel_name}' eklendi.")
        else:
            print(f"Kanal '{channel_name}' zaten mevcut.")

    def remove_channel(self, channel_name):
        channel_name = channel_name.strip().lower()  # Küçük harfe dönüştürüldü
        if channel_name in self.channel_list:
            self.channel_list.remove(channel_name)
            print(f"Kanal '{channel_name}' silindi.")
        else:
            print(f"Kanal '{channel_name}' mevcut değil.")

    def random_channel(self):
        if self.channel_list:
            self.current_channel = random.choice(self.channel_list)
            print("Şu anki kanal:", self.current_channel)
            self.channel_history.append(self.current_channel)
        else:
            print("Hiç kanal yok.")

    def list_favorites(self):
        if self.favorite_channels:
            print("Favori Kanallar:", ", ".join(self.favorite_channels))
        else:
            print("Favori kanal yok.")

    def add_favorite(self, channel_name):
        channel_name = channel_name.strip().lower()  # Küçük harfe dönüştürüldü
        if channel_name in self.channel_list and channel_name not in self.favorite_channels:
            self.favorite_channels.append(channel_name)
            print(f"Kanal '{channel_name}' favorilere eklendi.")
        else:
            print(f"Kanal '{channel_name}' ya mevcut değil ya da zaten favorilerde.")

    def show_channel_history(self):
        if self.channel_history:
            print("Son izlenen kanallar:", ", ".join(self.channel_history))
        else:
            print("Kanal geçmişi yok.")

    def __str__(self):
        return f"TV durumu: {self.state}\nSes seviyesi: {self.volume}\nKanal listesi: {self.channel_list}\nŞu anki kanal: {self.current_channel}"

# Ana program
command = Command()
while True:
    print("""
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
    """)
    
    process = input("İşlem girin: ")

    if process == "q":
        print("Program sonlanıyor...")
        break
    
    elif process == "1":
        command.tv_on()

    elif process == "2":
        command.tv_off()

    elif process == "3":
        command.adjust_volume()

    elif process == "4":
        channel_name = input("Eklenecek kanalı girin: ")
        command.add_channel(channel_name)

    elif process == "5":
        channel_name = input("Silinecek kanalı girin: ")
        command.remove_channel(channel_name)

    elif process == "6":
        command.random_channel()

    elif process == "7":
        command.list_favorites()

    elif process == "8":
        channel_name = input("Favori kanalı girin: ")
        command.add_favorite(channel_name)

    elif process == "9":
        command.show_channel_history()

    elif process == "10":
        print(command)

    else:
        print("Geçersiz işlem!")
