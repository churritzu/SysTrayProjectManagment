import pystray
from PIL import Image

class Menu(pystray.Menu):
	def __init__(self):
		items = self.getMenuItems()
		super().__init__(*items)

	def getWebSubMenu(self):
		phpDb = pystray.MenuItem("Without DataBase", self.printing)
		phpNDb = pystray.MenuItem("With DataBase", self.printing)
		return pystray.Menu(phpDb, phpNDb)
		
	def getMenuItems(self):
		exitOpt = pystray.MenuItem("Exit", self._close)
		settingOpt = pystray.MenuItem("Settings", self.printing)
		webOpt = pystray.MenuItem("Web", self.getWebSubMenu())

		return [webOpt, self.SEPARATOR, settingOpt, self.SEPARATOR, exitOpt]

	'''
		Actions for de Menu
	'''
	def _close(self, instance):	instance.stop()

	def printing(self, instance):	print(instance)
		
class TrayIcon(pystray.Icon):
	def __init__(self):
		super().__init__("Systray ObejaNegra", title = "Obeja Negra", menu=Menu())
		self.icon = Image.open("images/favicon.ico")
		self.visible = True