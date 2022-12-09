from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("box.kv")


class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BoxLayoutApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == "__main__":
    BoxLayoutApp().run()
