import pystray, os, sys
from PIL import Image
from Modules.Clone import Clone

mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))
iconsPath = mainPath+"\\images\\"

class Menu(pystray.Menu):
	def __init__(self):
		items = self.getMenuItems()
		super().__init__(*items)

	def getWebSubmenu(self):
		phpDb = pystray.MenuItem("Without DataBase", lambda: self._clone('webWithOutDb'))
		phpNDb = pystray.MenuItem("With DataBase", lambda: self._clone('webWithDb'))
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
		os.system("python "+mainPath+"\\setting.py")

	# Clone Options
	def _clone(self, branch): Clone(branch).clone()

	# For Testing propuse only
	def _testing(self, instance):	print(instance)

class TrayIcon(pystray.Icon):
	def __init__(self):
		super().__init__("Systray ObejaNegra", title = "Obeja Negra", menu=Menu())
		self.icon = Image.open(iconsPath+"favicon.ico")
		self.visible = True