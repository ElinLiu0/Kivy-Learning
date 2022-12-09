# 虽然Kivy不支持中文，但是我们可以使用Unicode编码来实现中文的显示
from kivy.core.text import LabelBase
from kivy.lang import Builder  # 导入kv语言解析器
from kivy.uix.boxlayout import BoxLayout  # 引入BoxLayout布局类
from kivy.app import App  # 导入Kivy的APP类，它是所有Kivy应用的基类


def turn_to_unicode(text):
    res = ''
    for i in text:
        res += '\\u' + hex(ord(i)).upper().replace('0X', '\\u')
    return res


# 从Chap1\HelloWorld_with_kvfile.py中复制的源码

Builder.load_file('你好世界.kv')  # 读取kv文件

# 此时，当前Python源代码中的控件类与kv文件中的控件类已经绑定，可以直接使用kv文件中的控件类
# 只有当kv文件内Layout的ID与Python源代码中的类名相同时，才能使用kv文件中的控件类
# 比如这里的IndexPage类，其ID为IndexPage，所以可以使用kv文件中的IndexPage类
# 对应KV的源码为：
"""
<IndexPage>:
    Button:
        text: '你好，世界'
"""
# 但是这时我们如果直接调用TestApp类来运行程序，会发现文字出现方块乱码
# 这时我们需要使用kivy.core.text.LabelBase.register()方法来注册字体

LabelBase.register('Roboto', 'C:\Windows\Fonts\msyhl.ttc')


class IndexPage(BoxLayout):
    def __init__(self, **kwargs):
        super(IndexPage, self).__init__(**kwargs)


class TestApp(App):
    def build(self):
        return IndexPage()


if __name__ == '__main__':
    # 读取kv文件
    TestApp().run()
