import kivy
from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.core.image import Image

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 500)

LabelBase.register(name = "Asman", fn_regular = "ASMAN.ttf")

class Layout(FloatLayout):
    None

class MainApp(App):
    title = "ScoreScanner"
    def build(self):
        return Layout()

if __name__ == '__main__':
    MainApp().run()