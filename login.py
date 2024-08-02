from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import users_data

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.username = TextInput(hint_text='Username', multiline=False)
        self.password = TextInput(hint_text='Password', multiline=False, password=True)

        login_button = Button(text='Login', on_release=self.login)
        biometric_button = Button(text='Login with Biometrics', on_release=self.biometric_login)
        register_button = Button(text='Create an Account', on_release=self.go_to_register)

        layout.add_widget(Label(text='Login'))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_button)
        layout.add_widget(biometric_button)
        layout.add_widget(register_button)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username.text
        password = self.password.text
        if username in users_data.users and users_data.users[username]['password'] == password:
            self.show_message("Session started", "You are being redirected to the Home screen.")
            self.manager.current = 'home'
        else:
            self.show_message("Incorrect session", "Invalid username or password. Please try again.")

    def biometric_login(self, instance):
        self.manager.current = 'biometric_login'

    def go_to_register(self, instance):
        self.manager.current = 'register'

    def show_message(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
