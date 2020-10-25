from kivy.uix.screenmanager import ScreenManager, Screen
from PIL import Image
import requests
from io import BytesIO

class RootWidget(Screen):
    
    krakow_text = "Kraków"
    jaswily_text = "Jaświły"
    bialystok_text = "Białystok"
    lodz_text = "Łódź"
    wroclaw_text = "Wrocław"
    powrot_text = "Powrót"

    def colorid(id):
    
        response = requests.get(id)
        red_image = Image.open(BytesIO(response.content))
        red_image_rgb = red_image.convert("RGB")
        rgb_pixel_value = red_image_rgb.getpixel((10,10))
        rgb_return=[]
        for x in rgb_pixel_value:
            rgb_return.append(x/200)
        rgb_return.append(1)
        if rgb_return == [1.09, 0.955, 0.0, 1]:
            rgb_return = [1, 0.86, 0, 1]
        elif rgb_return == [1.095, 0.84, 0, 1]:
            rgb_return = [0.85, 0.65, 0, 1]
        else:
            pass
        return rgb_return
      
    
    warszawacolorid = colorid("http://api.looko2.com/?method=Widget2&id=807D3A1F7161")
    krakowcolorid = colorid("http://api.looko2.com/?method=Widget2&id=2C3AE834DEC9")
    wroclawcolorid = colorid("http://api.looko2.com/?method=Widget2&id=DC4F2240BB41")
    bialystokcolorid = colorid("http://api.looko2.com/?method=Widget2&id=2C3AE834DED1")
    lodzcolorid = colorid("http://api.looko2.com/?method=Widget2&id=5CCF7FC131F1")
    jaswilycolorid = colorid("http://api.looko2.com/?method=Widget2&id=6001944B3313")
    katowicecolorid = colorid("http://api.looko2.com/?method=Widget2&id=A020A6295320")
    szczecincolorid = colorid("http://api.looko2.com/?method=Widget2&id=6001944BCBF4")
    gdyniacolorid = colorid("http://api.looko2.com/?method=Widget2&id=A020A6331663")


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

    
        
        
 

    def text(self):
        rgb_return = RootWidget.colorid(self.id)
        print(rgb_return)
        if rgb_return == [0.1, 0.5, 0.545, 1]:
            self.label_wid.text = "Stan powietrza jest bardzo dobry, nie stanowi zagrożenia zdrowia. Warunki są sprzyjające aktywnościom na wolnym powietrzu."
        
        elif rgb_return == [0.01, 0.495, 0.23, 1]:
            self.label_wid.text = "Stan powietrza jest dobry, stanowi brak lub niskie zagrożenie zdrowia. Zalecany jest spacer lub jogging."
        
        elif rgb_return == [1, 0.86, 0, 1]:
            self.label_wid.text = "Stan powietrza jest akceptowalny. Zanieczyszczenia mogą stanowić zagrożenie osobom chorym, starszym, dzieciom i kobietom w ciąży."

        elif rgb_return == [0.85, 0.65, 0, 1]:
            self.label_wid.text = "Stan powietrza jest  dostateczny. Zanieczyszczenia stanowią zagrożenie, szczególnie osobom chorym, starszym, dzieciom i kobietom w ciąży. Osoby takie powinny ograniczyć przebywanie na wolnym powietrzu."
        
        elif rgb_return == [0.885, 0.02, 0.01, 1]:
            self.label_wid.text = "Stan powietrza jest zły.  Stanowi silne zagrożenie osobom chorym, starszym, dzieciom i kobietom w ciąży. Takim osobom odradza się przebywanie na wolnym powietrzu. Zdrowe osoby powinny ograniczyć wysiłek na wolnym powietrzu."
        
        elif rgb_return == [0.615, 0.02, 0.105, 1]:
            self.label_wid.text = "Stan powietrza jest bardzo zły i ma negatywny wpływ na zdrowie. Wszelki pobyt na wolnym powietrzu należy ograniczyć do absolutnego minimum. Osoby chore, starsze, dzieci i kobiety w ciąży powinny bezwględnie unikać pobytu na zewnątrz. Zanieczyszczenia mogą prowadzić do chorób układu oddechowego, odpornościowego i krązeniowego."
        
        else:
            pass
        