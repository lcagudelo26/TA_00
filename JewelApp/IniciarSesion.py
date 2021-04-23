from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size= (360,600)

Builder.load_file('IniciarSesion.kv')

class IniciarSesionApp(App):

    def button2_press(self):
         self.root.ids['text_label'].text = 'Contraseña incorrecta'


app = IniciarSesionApp()
app.run()