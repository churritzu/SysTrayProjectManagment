import pystray, os, sys
from PIL import Image
from Modules.Clone import Clone
from setting import SettingsApp

iconsPath = os.path.dirname(os.path.realpath(sys.argv[0]))+"\\images\\"

class Menu(pystray.Menu):
	def __init__(self):
		items = self.getMenuItems()
		super().__init__(*items)

	def getWebSubmenu(self):
		phpDb = pystray.MenuItem("Without DataBase", self._cloneWebNoDb)
		phpNDb = pystray.MenuItem("With DataBase", self._cloneWebDb)
		return pystray.Menu(phpDb, phpNDb)
		
	def getMenuItems(self):
		exitOpt = pystray.MenuItem("Exit", self._close)
		settingOpt = pystray.MenuItem("Settings", self._settings)
		webOpt = pystray.MenuItem("Web", self.getWebSubmenu())

		return [webOpt, self.SEPARATOR, settingOpt, self.SEPARATOR, exitOpt]

	#######################################################################
	#	Actions for de Menu																									#
	#######################################################################

	# Close the program
	def _close(self, instance):	instance.stop()

	# Settings
	def _settings(self, instance): 
		print("Settings...")
		SettingsApp().run()

	# Clone Options
	def _cloneWebDb(self, instance): Clone("webWithDb").clone()
	def _cloneWebNoDb(self, instance): Clone("webWithOutDb").clone()

	# For Testing propuse only
	def _testing(self, instance):	print(instance)

class TrayIcon(pystray.Icon):
	def __init__(self):
		super().__init__("Systray ObejaNegra", title = "Obeja Negra", menu=Menu())
		self.icon = Image.open(iconsPath+"favicon.ico")
		self.visible = True