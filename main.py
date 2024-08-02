from kivy.config import Config
Config.set('input', 'wm_pen', 'none')
from database import create_db


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from registro import RegisterScreen
from biologin import BiometricLoginScreen
from home import HomeScreen

class MyApp(App):
    def build(self):
        create_db()
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(BiometricLoginScreen(name='biometric_login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    MyApp().run()
