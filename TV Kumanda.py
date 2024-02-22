import time
import random

print("""
███████████████████████████████████████
█───█─█─████────█───█─███─█────█───█───█
██─██─█─████─██─█─███──█──█─██─██─██─███
██─██─█─████────█───█─█─█─█─██─██─██───█
██─██───████─█─██─███─███─█─██─██─██─███
██─███─█████─█─██───█─███─█────██─██───█
███████████████████████████████████████
Author: A.Vahap Doğan
      
TV kumandaları mantığında yapılmış bir python console programı.
	""")

class Command:
    """
    TV kontrolünü sağlayan bir sınıf.
    """
    def __init__(self, state="off", volume=0, channel_list=["TRT", "NTV", "DMAX"]):
        """
        Command sınıfının yapıcı metodu.
        state: TV'nin açık veya kapalı olduğunu belirten bir dize.
        volume: TV'nin ses seviyesini belirten bir tamsayı.
        channel_list: TV'nin kanal listesini tutan bir liste.
        """
        self.state = state
        self.volume = volume
        self.channel_list = channel_list
        self.channel = None

    def tv_on(self):
        """
        TV'yi açma metodudur.
        """
        if self.state == "on":
            print("TV is already on!")
        else:
            print("TV is on.")
            self.state = "on"

    def tv_off(self):
        """
        TV'yi kapama metodudur.
        """
        if self.state == "off":
            print("TV is already off!")
        else:
            print("TV is off...")
            self.state = "off"

    def adjust_volume(self):
        """
        Ses seviyesini ayarlama metodudur.
        """
        while True:
            answer = input("Volume down : '<' \n Volume up : '>' \n Exit : 'q'")
            if answer == '<':
                if self.volume != 0:
                    self.volume -= 1
                    print("Volume :", self.volume)
            elif answer == '>':
                if self.volume != 31:
                    self.volume += 1
                    print("Volume :", self.volume)
            elif answer == 'q':
                print("Exiting volume adjustment.")
                break
            else:
                print("Invalid input!")

    def add_channel(self, channel_name):
        """
        Yeni bir kanal eklemek için metod.
        channel_name: Eklenmek istenen kanalın adı.
        """
        print("Channel is being added....")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("Channel is added.")

    def random_channel(self):
        """
        Rastgele bir kanal seçme metodudur.
        """
        random_channel_index = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[random_channel_index]
        print("Current channel :", self.channel)

    def __len__(self):
        """
        Kanal listesinin uzunluğunu döndüren metod.
        """
        return len(self.channel_list)

    def __str__(self):
        """
        Objenin dizesel temsilini döndüren metod.
        """
        return f"TV status: {self.state}\nTV volume: {self.volume}\nChannel list: {self.channel_list}\nCurrent channel: {self.channel}"

# Ana program
command = Command()
print(
    """
    1. TV on
    2. TV off
    3. Volume
    4. Channel add
    5. Status channel
    6. Random channel
    7. TV data
    Enter "q" for exit
    """)
while True:
    process = input("Enter process : ")

    if process == "q":
        print("Program is finishing...")
        break
    
    elif process == "1":
        command.tv_on()

    elif process == "2":
        command.tv_off()

    elif process == "3":
        command.adjust_volume()

    elif process == "4":
        channel_names = input("Separate channels to be added with ','")
        channel_list = channel_names.split(",")

        for add_channel in channel_list:
            command.add_channel(add_channel)
    
    elif process == "5":
        print("Channel number.", len(command))
    
    elif process == "6":
        command.random_channel()

    elif process == "7":
        print(command)

    else:
        print("Invalid process!")
