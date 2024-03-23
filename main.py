from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data = ""

    def display_info(self):
        self.data = self.ids.metin_giris.text
        self.ids.etiket.text = self.data
        self.ids.metin_giris.text = ""

    # def btn_clicked(self):
    #     print(self.data)


class ProjectApp(App):
    pass


ProjectApp().run()
