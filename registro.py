from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.camera import Camera
import cv2
import base64
import numpy as np
from database import save_user

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("No se puede abrir al camara")

        self.username = TextInput(hint_text='Username', multiline=False)
        self.password = TextInput(hint_text='Password', multiline=False, password=True)

        self.camera = Camera(play=True)
        self.capture_button = Button(text='Capture Face', on_release=self.capture_face)
        register_button = Button(text='Create Account', on_release=self.register)
        back_button = Button(text='Back to Login', on_release=self.go_to_login)

        layout.add_widget(Label(text='Registra tu usuario'))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.camera)
        layout.add_widget(self.capture_button)
        layout.add_widget(register_button)
        layout.add_widget(back_button)

        self.add_widget(layout)
        


    def capture_face(self, instance):
        texture = self.camera.texture
        if texture:
            camera_image = texture.pixels
            image_array = np.frombuffer(camera_image,np.uint8).reshape(texture.height, texture.width, 4)
            face_image = image_array[:,:,:3]
            
            _, buffer = cv2.imencode('.jpg', face_image)
            self.face_data = base64.b64encode(buffer).decode('utf-8')
            print("Face captured")

    def register(self, instance):
        username = self.username.text
        password = self.password.text
        if username and password and hasattr(self, 'face_data'):
            save_user(username, password, self.face_data)
            self.manager.current = 'login'
        else:
            print("Username, password, and face capture are required")

    def go_to_login(self, instance):
        self.manager.current = 'login'
