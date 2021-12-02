from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window


Window.clearcolor = [65/255, 154/255, 255/255, 1]
Window.title = "MyDi"
Window.size = (400, 600)


class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('WindowManager.kv')

class MyApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()
