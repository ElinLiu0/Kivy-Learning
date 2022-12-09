# 导入Kivy的APP类，它是所有Kivy应用的基类
from kivy.app import App
"""
Kiyy内置了丰富的控件(Widgets)：如
    - 按钮(Button)
    - 标签(Label)
    - 输入框(TextInput)
    - 复选框(Checkbox)
    - 滚动容器(Scorallable Container)等
"""
from kivy.uix.button import Button
# 引入BoxLayout布局类
from kivy.uix.boxlayout import BoxLayout
# 创建初始页类，需要继承自BoxLayout基类


class IndexPage(BoxLayout):
    # 初始化
    def __init__(self, **kwargs):
        super(IndexPage, self).__init__(**kwargs)
        # 创建一个按钮
        self.join = Button(text='Hello World')
        # 将按钮添加到布局中
        self.add_widget(self.join)
# 从App类中继承了Kivy应用的基本功能，如创建窗口、设置窗口的大小和位置等


class HelloWorld(App):
    # 实现TestApp类的build()方法，该方法返回一个用于显示的Widget
    def build(self):
        # 在Kivy的设定中，build()返回的是一个根组件（root widget）
        return IndexPage()


if __name__ == '__main__':
    # 启动应用
    HelloWorld().run()
