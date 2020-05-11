import pystray, os, sys, shutil
from PIL import Image

iconsPath = os.path.dirname(os.path.realpath(sys.argv[0]))+"\\images\\"

class Menu(pystray.Menu):
	PWD = "D:/Trabajo/GCloud/Regional/Web/"
	proyectName = "new_proyect"

	def __init__(self):
		items = self.getMenuItems()
		super().__init__(*items)

	def getWebSubMenu(self):
		phpDb = pystray.MenuItem("Without DataBase", self.cloneWebNoDb)
		phpNDb = pystray.MenuItem("With DataBase", self.cloneWebDb)
		return pystray.Menu(phpDb, phpNDb)
		
	def getMenuItems(self):
		exitOpt = pystray.MenuItem("Exit", self._close)
		settingOpt = pystray.MenuItem("Settings", self.testing)
		webOpt = pystray.MenuItem("Web", self.getWebSubMenu())

		return [webOpt, self.SEPARATOR, settingOpt, self.SEPARATOR, exitOpt]

	def getFullProyectPath(self): return self.PWD + self.proyectName+"/"

	#######################################################################
	#	Actions for de Menu																									#
	#######################################################################

	# Close the program
	def _close(self, instance):	instance.stop()

	# For Testing propuse only
	def testing(self, instance):	print(instance)

	# Clone the template for de non database branch
	def cloneWebDb(self, instance):
		# self.proyectName = input("Name of the new proyecto: ")
		print(self.getFullProyectPath())
		os.system("git clone -b webWithDb git@gitlab.com:churritzu/work-templates.git "+ self.getFullProyectPath())
		shutil.rmtree(self.getFullProyectPath() +".git/", ignore_errors=True)
		os.system("code "+ self.getFullProyectPath())

	# Clone the template for de non database branch
	def cloneWebNoDb(self, instance):
		# self.proyectName = input("Name of the new proyecto: ")
		print(self.getFullProyectPath())
		os.system("git clone -b webWithOutDb git@gitlab.com:churritzu/work-templates.git "+ self.getFullProyectPath())
		shutil.rmtree(self.getFullProyectPath() +".git/", ignore_errors=True)
		os.system("code "+ self.getFullProyectPath())
		
class TrayIcon(pystray.Icon):
	def __init__(self):
		super().__init__("Systray ObejaNegra", title = "Obeja Negra", menu=Menu())
		self.icon = Image.open(iconsPath+"favicon.ico")
		self.visible = True