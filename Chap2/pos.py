from kivy.app import App  # 导入App类
from kivy.uix.floatlayout import FloatLayout  # 导入FloatLayout类
from kivy.lang import Builder  # 导入Builder类

Builder.load_file('pos.kv')  # 加载kv文件

"""
请注意：
1. 本例中，kv文件中的FloatLayout的pos属性的值是(100, 100)。
2. Button2的pos_hint属性的值是{'center_x': 0.5, 'center_y': 0.5}。
但是这些值都是以窗口控件的左下角为0,0基点进行计算，第一种方式是计算出来的像素数
值，第二种方式是计算出来的百分比，该百分比的计算公式为：
    - [窗口组件的宽度 * pos_hint[0]的值] / 100
    - [窗口组件的高度 * pos_hint[1]的值] / 100
"""


class PosFloat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PosApp(App):
    def build(self):
        return PosFloat()


if __name__ == '__main__':
    PosApp().run()
