from kivy.app import App
from kivy.uix.label import Label

# kivy.require('1.11.1')

class SettingsApp(App):
	def build(self):
		return Label(text="Hola Mundo")

if __name__ == "__main__":
		SettingsApp().run()