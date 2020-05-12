import os, shutil

class Clone:
	PWD = "D:/Trabajo/GCloud/Regional/Web/"
	proyectName = "new_proyect"

	def __init__(self, branch=""):
		self.branch = branch
		
	def getFullProyectPath(self): return self.PWD + self.proyectName+"/"

	def clone(self):
		# self.proyectName = input("Name of the new proyecto: ")
		os.system("git clone -b "+ self.branch +" git@gitlab.com:churritzu/work-templates.git "+ self.getFullProyectPath())
		shutil.rmtree(self.getFullProyectPath() +".git/", ignore_errors=True)
		os.system("code "+ self.getFullProyectPath())
