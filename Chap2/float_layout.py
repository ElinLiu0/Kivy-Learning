from kivy.app import App  # 导入App类
from kivy.uix.button import Button  # 导入Button类
from kivy.uix.floatlayout import FloatLayout  # 导入FloatLayout类
from kivy.graphics import Rectangle, Color  # 导入Rectangle类和Color类


class FloatLayoutApp(App):  # 创建FloatLayoutApp类，继承自App类
    def build(self):  # 重写build()方法

        def update_rect(instance, value):  # 定义update_rect()方法
            instance.rect.pos = instance.pos  # 将instance.rect.pos属性的值设置为instance.pos属性的值
            instance.rect.size = instance.size  # 将instance.rect.size属性的值设置为instance.size属性的值

        fl = FloatLayout()  # 创建FloatLayout对象
        with fl.canvas:  # 对Layout对象的canvas属性进行上下文管理
            Color(0, 1, 0, 0.5, mode='rgba')
            fl.rect = Rectangle(pos=fl.pos, size=fl.size)
            # 因为fl.rect是一个Rectangle对象，所以可以通过fl.rect.pos和fl.rect.size属性来设置其位置和大小
            # 因此，当fl.pos或fl.size属性的值发生变化时，fl.rect.pos和fl.rect.size属性的值也会发生变化
            # 使用bind()方法可以将fl.pos和fl.size属性的值绑定到fl.rect.pos和fl.rect.size属性上
            # 实现持久化
            fl.bind(pos=update_rect, size=update_rect)
        # 创建Button对象
        btn = Button(text='Button', size_hint=(.3, .2), pos=(100, 100))

        # 将按钮天添加到布局内
        fl.add_widget(btn)
        return fl


if __name__ == '__main__':
    FloatLayoutApp().run()
