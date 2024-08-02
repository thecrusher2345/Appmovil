# add_face_id_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from authservice import AuthService

class AddFaceIDScreen(Screen):
    def __init__(self, **kwargs):
        super(AddFaceIDScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.camera = Camera(resolution=(640, 480), play=True)
        capture_button = MDRaisedButton(text="Capture Face ID", on_release=self.capture_face_id)
        back_button = MDFlatButton(text="Back", on_release=self.goto_register)

        self.layout.add_widget(self.camera)
        self.layout.add_widget(capture_button)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def capture_face_id(self, instance):
        # Aquí capturamos y retornamos una representación simplificada del Face ID
        if self.camera.texture:
            face_id = self.camera.texture  # Usar la textura de la cámara como representación

            # Obtener el usuario y la contraseña temporales de la pantalla de registro
            username = self.manager.get_screen('register').username.text
            password = self.manager.get_screen('register').password.text

            # Registrar el usuario con el Face ID capturado
            if AuthService.register(username, password, face_id):
                self.show_dialog("Face ID Captured", "You can now log in with your credentials")
                self.manager.current = 'login'
            else:
                self.show_dialog("Capture Failed", "Face ID already in use")
        else:
            self.show_dialog("Capture Failed", "Face ID capture failed. Try again.")

    def goto_register(self, instance):
        self.manager.current = 'register'

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, 0.4),
            buttons=[MDRaisedButton(text="Close", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()
