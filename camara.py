# camera_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.camera = Camera(play=True, resolution=(640, 480))
        capture_button = MDRaisedButton(text="Capture", on_release=self.capture)
        back_button = MDFlatButton(text="Back", on_release=self.goto_previous)

        layout.add_widget(self.camera)
        layout.add_widget(capture_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def capture(self, instance):
        # Captura de una imagen de la cámara
        if self.camera.texture:
            # Aquí puedes guardar la imagen o procesarla
            print("Image captured")
        else:
            self.show_dialog("Capture Failed", "No image captured. Try again.")

    def goto_previous(self, instance):
        self.manager.current = 'previous_screen'

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, 0.4),
            buttons=[MDRaisedButton(text="Close", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()
