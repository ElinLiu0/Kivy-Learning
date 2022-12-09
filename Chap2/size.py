from kivy.app import App  # 导入App类
from kivy.uix.floatlayout import FloatLayout  # 导入FloatLayout类
from kivy.lang import Builder  # 导入Builder类

Builder.load_file('size.kv')  # 加载kv文件


class SizeFloat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SizeApp(App):
    def build(self):
        return SizeFloat()


if __name__ == '__main__':
    SizeApp().run()
