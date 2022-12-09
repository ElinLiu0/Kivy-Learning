from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file('float_layout.kv')


class FloatLayoutWidget(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    FloatLayoutApp().run()
