from kivy.app import App
# Girdlayout sive para realizar matrices de cajas de texto 
from kivy.uix.gridlayout import GridLayout
# Label es una etiqueta para un elemento en una interfaz de usuario 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# Widget para facil acceso a funciones 
from kivy.uix.widget import Widget
# ObjectProperty devuelve informacion 
from kivy.properties import ObjectProperty
# Builder es un patron de diseño creacional 
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size= (360,600)
# aqui podemos registrarnos en la aplicaccion 
Builder.load_file('Registrarse.kv')

class RegistrarseApp(App):

    def button2_press(self):
      # aviso de que la cuenta fue creada con exito 
        self.root.ids['text_label'].text = 'Cuenta creada correctamente'


app = RegistrarseApp()
app.run()