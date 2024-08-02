from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.upload_button = Button(text='Upload File', size_hint_y=None, height=50, on_release=self.open_file_chooser)
        self.files_layout = BoxLayout(orientation='vertical')
        
        self.layout.add_widget(self.upload_button)
        self.layout.add_widget(self.files_layout)
        
        self.add_widget(self.layout)

    def open_file_chooser(self, instance):
        filechooser = FileChooserIconView()
        filechooser.bind(on_submit=self.upload_file)

        popup = Popup(title="Select a file", content=filechooser, size_hint=(0.9, 0.9))
        popup.open()

    def upload_file(self, filechooser, selection, touch):
        try:
            if selection:
                file_path = selection[0]
                file_name = file_path.split('/')[-1]
                
                file_label = Label(text=file_name, size_hint_y=None, height=40)
                self.files_layout.add_widget(file_label)
                
                # Aquí puedes agregar la lógica para almacenar el archivo
                print(f"File uploaded: {file_path}")
            
            filechooser.parent.parent.dismiss()  # Cierra el popup
        except Exception as e:
            print(f"Error uploading file: {e}")

    def display_message(self, message, duration=3):
        message_label = Label(text=message, size_hint=(0.8, 0.2))
        popup = Popup(title='Notification', content=message_label, size_hint=(0.5, 0.5), auto_dismiss=False)
        popup.open()
        
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: popup.dismiss(), duration)

if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.screenmanager import ScreenManager
    
    class MyApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(HomeScreen(name='home'))
            return sm

    MyApp().run()
