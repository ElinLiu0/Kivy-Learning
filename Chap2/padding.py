from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('padding.kv')


class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PaddingApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == '__main__':
    PaddingApp().run()
