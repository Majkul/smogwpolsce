from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class City(Screen):
    text = "Wybierz swoje miasto lub najbliższe w twojej okolicy"
    krakow_text = "Kraków"
    jaswilt_text = "Jaświły"
    bialystok_text = "Białystok"
    lodz_text = "Łódź"
    wroclaw_text = "Wrocław"

    def on_enter(self):
        Clock.schedule_once(self.changeScreen)


    def changeScreen(self, dt):
        with open("hackheroes/data/id_stat.txt") as fobj:    
            for stat in fobj:
                i = ""
                i = str(stat.rstrip())
        if i != "None":
            self.manager.current = 'menu'
        else:
            pass

    def changeScreen2(self):
        self.manager.current = 'menu'
    
    def warszawa(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=807D3A1F7161"
        print(self.id)

    def krakow(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=2C3AE834DEC9"
        print(self.id)

    def wroclaw(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=DC4F2240BB41"
        print(self.id)

    def bialystok(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=2C3AE834DED1"
        print(self.id)

    def lodz(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=5CCF7FC131F1"
        print(self.id)

    def jaswily(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=6001944B3313"
        print(self.id)

    def katowice(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=A020A6295320"
        print(self.id)
    
    def szczecin(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=6001944BCBF4"
        print(self.id)

    def gdynia(self):
        self.id = "http://api.looko2.com/?method=Widget2&id=A020A6331663"
        print(self.id)

    def save_id_stat(self):
        with open("hackheroes/data/id_stat.txt", "w") as fobj:
            fobj.write(str(self.id))
        fobj.close()


class FirstScreen(Screen):
    text = "Podaj imie (bez polskich znaków):"
    def on_enter(self):
        Clock.schedule_once(self.changeScreen)


    def changeScreen(self, dt):
        with open("hackheroes/data/name.txt") as fobj:    
            for stat in fobj:
                i = ""
                i = str(stat.rstrip())
        if i != "None":
            self.manager.current = 'city'
        else:
            pass
    


    
    def submit_name(self):
        self.user_name = self.first_name_text_input.text
        with open("hackheroes/data/name.txt", "w") as fobj:
            fobj.writelines(str(self.user_name))
        fobj.close()