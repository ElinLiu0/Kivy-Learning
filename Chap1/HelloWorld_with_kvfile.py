from kivy.app import App  # 导入Kivy的APP类，它是所有Kivy应用的基类
from kivy.uix.boxlayout import BoxLayout  # 引入BoxLayout布局类
from kivy.lang import Builder  # 导入kv语言解析器

Builder.load_file('HelloWorld.kv')  # 读取kv文件

# 此时，当前Python源代码中的控件类与kv文件中的控件类已经绑定，可以直接使用kv文件中的控件类
# 只有当kv文件内Layout的ID与Python源代码中的类名相同时，才能使用kv文件中的控件类
# 比如这里的IndexPage类，其ID为IndexPage，所以可以使用kv文件中的IndexPage类
# 对应KV的源码为：
"""
<IndexPage>:
    Button:
        text: 'Hello World'
"""


class IndexPage(BoxLayout):
    def __init__(self, **kwargs):
        super(IndexPage, self).__init__(**kwargs)


class TestApp(App):
    def build(self):
        return IndexPage()


if __name__ == '__main__':
    # 读取kv文件
    TestApp().run()
