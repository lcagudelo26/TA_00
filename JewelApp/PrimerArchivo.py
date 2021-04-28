import kivy

from kivy.app import App
from kivy.uix.label import Label
# definicion de la clase base de la aplicacion
class aplicacion(App):
  # esta etiqueta es la raiz widget de la aplicacion
    def build(self):
        return Label(text='Bienvenidos a Jewel App')
#iniciamos la clase de aplicacion (run) esto inicia y comienza a ejecutar la aplicacion 
if __name__ =='__main__':
    aplicacion().run()