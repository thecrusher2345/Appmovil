from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.camera import Camera
import users_data

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.username = TextInput(hint_text='Username', multiline=False)
        self.password = TextInput(hint_text='Password', multiline=False, password=True)

        self.camera = Camera(play=True)
        self.capture_button = Button(text='Capture Face', on_release=self.capture_face)
        register_button = Button(text='Create Account', on_release=self.register)
        back_button = Button(text='Back to Login', on_release=self.go_to_login)

        layout.add_widget(Label(text='Register'))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.camera)
        layout.add_widget(self.capture_button)
        layout.add_widget(register_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def capture_face(self, instance):
        # Placeholder for actual face capture logic
        self.face_data = "face_data_placeholder"
        print("Face captured")

    def register(self, instance):
        username = self.username.text
        password = self.password.text
        if username and password and hasattr(self, 'face_data'):
            users_data.users[username] = {'password': password, 'biometric': self.face_data}
            self.manager.current = 'login'
        else:
            print("Username, password, and face capture are required")

    def go_to_login(self, instance):
        self.manager.current = 'login'
