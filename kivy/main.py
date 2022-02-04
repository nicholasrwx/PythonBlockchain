from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder


Builder.load_file('kivy.kv')


class FunkyButton(Button):
    pass


class KivyApp(App):
    def build(self):
        return FunkyButton(
            pos=(100, 100),
            size_hint=(None, None),
            size=(500, 500)
        )


if __name__ == '__main__':
    KivyApp().run()
