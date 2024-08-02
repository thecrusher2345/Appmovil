from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import users_data

class BiometricLoginScreen(Screen):
    def __init__(self, **kwargs):
        super(BiometricLoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Biometric Authentication')
        self.camera = Camera(play=True)
        self.button = Button(text='Authenticate', on_release=self.authenticate)
        self.back_button = Button(text='Back to Login', on_release=self.go_to_login)

        layout.add_widget(self.label)
        layout.add_widget(self.camera)
        layout.add_widget(self.button)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def authenticate(self, instance):
        # Placeholder for actual biometric authentication logic
        face_data = "face_data_placeholder"
        for user, data in users_data.users.items():
            if data['biometric'] == face_data:
                self.show_message("Session started", "You are being redirected to the Home screen.")
                self.manager.current = 'home'
                return
        self.show_message("Authentication Failed", "Biometric authentication failed. Please try again.")

    def go_to_login(self, instance):
        self.manager.current = 'login'

    def show_message(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.8, 0.3),
                      auto_dismiss=True)
        popup.open()
