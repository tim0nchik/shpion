# описать экран ввода кол-во шпионов
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App



class SpiesInputScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        app = App.get_running_app()
        