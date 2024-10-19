from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.scrollview import ScrollView

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class ScrButton(Button):
    def __init__(self, screen, direction = 'left', goal = 'main',**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScreen(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen

        btn1 = ScrButton(self, goal = 'first', text="1")
        btn2 = ScrButton(self, goal = 'second', text="2")
        btn3 = ScrButton(self, goal = 'third', text="3")
        btn4 = ScrButton(self, goal = 'fourth', text="4")

        chose = Label(text = 'Выбери экран')

        horlay = BoxLayout(orientation = 'horizontal')
        verlay = BoxLayout(orientation = 'vertical', padding = 4, spacing = 4)

        verlay.add_widget(btn1)
        verlay.add_widget(btn2)
        verlay.add_widget(btn3)
        verlay.add_widget(btn4)

        horlay.add_widget(chose)
        horlay.add_widget(verlay)

        self.add_widget(horlay) # экран - это виджет, на котором могут создаваться все другие (потомки)


class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)

        esc_btn = ScrButton(self, direction = 'right', text="Назад")
        esc_btn.pos_hint={'center_x': 0.07, 'center_y': 0.94}
        esc_btn.size_hint=(0.07,0.05)

        funny_btn = ScrButton(self, goal = 'first', direction = 'right', text="Опа гангнам стайл")
        funny_btn.pos_hint={'center_x': 0.25, 'center_y': 0.19}
        funny_btn.size_hint=(0.4,0.3)

        dizzy_btn = ScrButton(self, goal = 'first', direction = 'right', text="я решил дилемму с поездом,\nнаправив его В ДЕТСКИЙ САД!")
        dizzy_btn.pos_hint={'x': 0.05, 'top': 0.69}
        dizzy_btn.size_hint=(None,None)
        dizzy_btn.size=(320,180)

        titanchannel_btn = ScrButton(self, goal = 'first', direction = 'right', text="КОСТИ, СКЕЛЕТЫ, КЛАДБИЩА, ЧЕРЕПА")
        titanchannel_btn.pos_hint={'right': 0.95, 'y': 0.39}
        titanchannel_btn.size_hint=(None,None)
        titanchannel_btn.size=(320,180)

        gamble_btn = ScrButton(self, goal = 'first', direction = 'right', text="Lets go gambling!\noh dang it\noh dang it\noh dang it")
        gamble_btn.pos_hint={'center_x': 0.75, 'top': 0.34}
        gamble_btn.size_hint=(0.4,0.3)

        self.add_widget(esc_btn)
        self.add_widget(funny_btn)
        self.add_widget(dizzy_btn)
        self.add_widget(titanchannel_btn)
        self.add_widget(gamble_btn)


class SecondScreen(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)

        esc_btn = ScrButton(self, direction = 'right', text="Назад")
        esc_btn.size_hint=(0.4,0.1)
        esc_btn.pos_hint={'center_x': 0.24, 'center_y': 0.08}

        tex_inpu = TextInput(text='Пофантазируй!', halign='left', focus=False, multiline=True)
        tex_inpu.size_hint=(0.41,0.07)
        tex_inpu.pos_hint={'x': 0.31, 'top': 0.47}

        sil_text = Label(text = 'silly text silly text bruh it must be same size as text input silly text'*5)
        sil_text.size_hint=(0.41,0.07)
        sil_text.pos_hint={'x': 0.31, 'top': 0.67}
        sil_text.text_size = (320,None)

        self.add_widget(esc_btn)
        self.add_widget(tex_inpu)
        self.add_widget(sil_text)


class ThirdScreen(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)

        esc_btn = ScrButton(self, direction = 'right', text="Вернись, вернись!3")
        esc_btn.size_hint=(0.4,0.1)
        esc_btn.pos_hint={'center_x': 0.24, 'center_y': 0.08}

        togel_buton = ToggleButton(text = 'huh', pos_hint={'center_x': 0.34, 'center_y': 0.38}, size_hint=(0.2,0.1))

        cwich = Switch(pos_hint={'center_x': 0.64, 'center_y': 0.38}, size_hint=(0.2,0.1))

        self.add_widget(esc_btn)
        self.add_widget(togel_buton)
        self.add_widget(cwich)


class FourthScreen(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        btn = ScrButton(self, direction = 'right', text="Вернись, вернись!4", size_hint=(0.2,0.1))

        screaming_text = Label(text = 'AAA AAAAAA AA AAAAAA AAA AAAA AAAAAAAA AAAAA AAAA AAAAAA AAA AAAA AAAA'*60)
        screaming_text.size_hint=(0.41,0.01)
        screaming_text.pos_hint={'x': 0.41, 'top': 0.67}
        screaming_text.text_size = (560,None)

        self.add_widget(btn)
        self.add_widget(screaming_text)


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScreen())
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourthScreen())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm


app = MyApp()
app.run()