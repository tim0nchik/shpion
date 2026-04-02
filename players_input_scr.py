# описать экран киви с вводом игроков
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App



class PlayersInputScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        app = App.get_running_app()
        text = Label(text  = 'выберите кол-во игроков:')
        button1 = Button(text = '3')
        button2 = Button(text = '4')
        button3 = Button(text = '5')
        button4 = Button(text = '6')
        hbl = BoxLayout(orientation = 'vertical')
        hbl.add_widget(text)
        hbl.add_widget(button1)
        hbl.add_widget(button2)
        hbl.add_widget(button3)
        hbl.add_widget(button4)
        self.add_widget(hbl)
        def but1():
            app.players_count = 3
            self.manager.current = 'scr2'
        button1.on_press = but1
