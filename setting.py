from tkinter import Tk
from tkinter import Label

class SettingsApp(Tk):
	def __init__(self):
		super().__init__()
		myLabel = Label(self, text="Hello Tkinter")
		myLabel.pack()

if __name__ == "__main__":
	SettingsApp().mainloop()
	# pass