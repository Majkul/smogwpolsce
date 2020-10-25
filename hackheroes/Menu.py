from kivy.uix.screenmanager import ScreenManager, Screen
from PIL import Image
import requests
from io import BytesIO
from kivy.clock import Clock
from RootWidget import RootWidget
class MenuScreen(Screen):
    jakosc_text = "Jakość powietrza w Polsce"
        
    def on_enter(self):
        Clock.schedule_once(self.nameid)

    def nameid(self, td):
        with open("hackheroes/data/id_stat.txt") as fobj:
            for stat in fobj:
                self.img = str(stat.rstrip())
        fobj.close()
        self.img_id.source = ""
        self.img_id.source = self.img

        with open("hackheroes/data/name.txt") as fobj:    
            for stat in fobj:
                i = str(stat.rstrip())
            
        fobj.close()
        
        rgb_return = RootWidget.colorid(self.img)

        print(rgb_return)
        self.wiadomosc_load.text = ""
        if rgb_return == [0.1, 0.5, 0.545, 1]:
            self.wiadomosc_load.text = f"Cześć {i}, stan powietrza jest bardzo dobry, warto by było z tego skorzystać, może jakiś spacer?"
        
        elif rgb_return == [0.01, 0.495, 0.23, 1]:
            self.wiadomosc_load.text = f"Cześć {i}, stan powietrza jest dobry, warto by było z tego skorzystać, może jakiś spacer?"
        
        elif rgb_return == [1, 0.86, 0, 1]:
            self.wiadomosc_load.text = f"Cześć {i}, stan powietrza jest akceptowalny, może jakiś krótki spacer?"

        elif rgb_return == [0.85, 0.65, 0, 1]:
            self.wiadomosc_load.text = f"Cześć {i}, stan powietrza jest dostateczny, lepiej nie wychodź na długo z domu."
        
        elif rgb_return == [0.885, 0.02, 0.01, 1]:
            self.wiadomosc_load.text = f"Cześć {i}, stan powietrza jest zły, jeśli nie musisz nie wychodź z domu."
        
        elif rgb_return == [0.615, 0.02, 0.105, 1]:
            self.wiadomosc_load.text = f"Cześć {i}, stan powietrza jest bardzo zły, lepiej nie wychodź z domu i zablokuj dostawanie się powietrza do środka"
        
        else:
            pass


class SettingsScreen(Screen):

    def info(self):
        with open("hackheroes/data/name.txt") as fobj:    
            for stat in fobj:
                self.imie = ""
                self.imie_info.text = "Imię: " + str(stat.rstrip())
        fobj.close()
        with open("hackheroes/data/id_stat.txt") as fobj:    
            for stat in fobj:
                self.city = ""
                self.city = str(stat.rstrip())
        fobj.close()
        if self.city == "http://api.looko2.com/?method=Widget2&id=807D3A1F7161":
            self.city = "Warszawa"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=2C3AE834DEC9":
            self.city = "Kraków"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=DC4F2240BB41":
            self.city = "Wrocław"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=2C3AE834DED1":
            self.city = "Białystok"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=5CCF7FC131F1":
            self.city = "Łódź"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=6001944B3313":
            self.city = "Jaświły"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=A020A6295320":
            self.city = "Katowice"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=6001944BCBF4":
            self.city = "Szczecin"
        elif self.city == "http://api.looko2.com/?method=Widget2&id=A020A6331663":
            self.city = "Gdynia"
        self.city_info.text = "Miasto: " + self.city
    def res_name(self):
        with open("hackheroes/data/name.txt", "w") as fobj:
            fobj.write("None")
        fobj.close()

    def res_city(self):
        with open("hackheroes/data/id_stat.txt", "w") as fobj:
            fobj.write("None")
        fobj.close()
