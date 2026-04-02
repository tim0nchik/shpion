from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from players_input_scr import PlayersInputScreen
from spies_input_scr import SpiesInputScreen


class MyApp(App):
    players_count = 0
    spies_count = 0
    word = ''
    def build(self):
        scrm = ScreenManager() 
        scrm.add_widget(PlayersInputScreen(name = 'scr1'))
        scrm.add_widget(SpiesInputScreen(name = 'scr2'))
        return scrm



app = MyApp()
app.run()