from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window


Window.clearcolor = (216/255, 216/255, 216/255,1)
Window.size= (360,600)


class CargandoApp(App):
    def build(self):
        layout= BoxLayout(orientation='vertical')
        img = Image(source="IconoJewelApp.png", size_hint=(0.75, 0.75), pos_hint={'center_x':0.5})
        layout.add_widget(img)
        return layout

app = CargandoApp()
app.run()