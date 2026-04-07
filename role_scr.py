# описать экран с выдадчей ролей 
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from random import sample, choice
from data import data

class RoleScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.current = 0
        self.button = Button(text = 'показать карту')
        self.add_widget(self.button)
        
    def on_pre_enter(self, *args):
        app = App.get_running_app()
        random_data = choice(data)
        self.spies = sample(range(app.players_count), app.spies_count)
        def role():
            if self.current >= app.players_count:
                self.manager.current = 'scr1'
                self.current = 0
            if self.button.text == 'показать карту':
                if self.current in self.spies:
                    self.button.text = 'шпион'
                else:
                    self.button.text = random_data
                self.current +=1
            else:
                self.button.text = 'показать карту'
        self.button.on_press = role