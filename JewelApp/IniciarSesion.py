from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Login(GridLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='Nombre de Usuario'))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Contraseña'))
        self.password=TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class JewelApp(App):
    def build(self):
        return Login()

if __name__=='__main__':
    JewelApp().run()


