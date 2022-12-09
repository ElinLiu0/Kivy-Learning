from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('box_vertical.kv')


class BoxVertical(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BoxVerticalApp(App):
    def build(self):
        return BoxVertical()


if __name__ == '__main__':
    BoxVerticalApp().run()
