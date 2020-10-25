from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from RootWidget import RootWidget
from City import City, FirstScreen
from Menu import SettingsScreen, MenuScreen


Window.clearcolor = (1, 1, 1, 1)

    
FirstScreen()        
 

City()
    
    
MenuScreen()


class ScreenCoTo(Screen):
    pass  


RootWidget()


SettingsScreen()


class WindowManager(ScreenManager):
    pass
    



kv = Builder.load_file("main.kv")

class TestApp(App):

    def build(self):
        
        return kv
    
       

if __name__ == "__main__":
    TestApp().run()