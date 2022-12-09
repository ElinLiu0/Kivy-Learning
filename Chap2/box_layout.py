from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout  # 导入BoxLayout类
from kivy.graphics import Rectangle, Color  # 导入Rectangle类和Color类


class Widget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色
        with self.canvas:
            Color(1, 1, 1, 1)
            # 创建一个矩形
            self.rect = Rectangle(pos=self.pos, size=self.size)
            # 将矩形的位置和大小绑定到布局的位置和大小上
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 添加两个按钮
        self.add_widget(Button(text='Button 1'))
        self.add_widget(Button(text='Button 2'))

    def update_rect(self, instance, value):
        # 更新矩形的位置和大小
        self.rect.pos = self.pos
        self.rect.size = self.size


class BoxLayoutApp(App):  # 继承自App类
    def build(self):    # 重写build()方法
        return Widget()  # 返回一个Widget对象


if __name__ == '__main__':
    BoxLayoutApp().run()  # 运行程序
