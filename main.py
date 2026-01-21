from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class WasishahApp(App):
    def build(self):
        # Screen ko black aur text ko neon green rakhein ge
        Window.clearcolor = (0, 0, 0, 1) 
        return Label(
            text='[ WASISHAH HACKER APP ]\nSYSTEM READY', 
            font_size='32sp', 
            color=(0, 1, 0, 1),
            bold=True
        )

if __name__ == '__main__':
    WasishahApp().run()
