*Pip package require
	# Pystray for trayicon
	-pip install pystray

	-python -m pip install --upgrade pip wheel setuptools virtualenv (Ensure you have the latest pip, wheel, and virtualenv for kivy)
	
	-python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
	-python -m pip install kivy_deps.angle==0.1.* (optional instead kivy_deps.glew)
		-glew and angle for OpenGG
		-sdl2 for control OpenGL
	
	-python -m pip install kivy_deps.gstreamer==0.1.* (opcional)
		-gstreame for audio and video
	
		-python -m pip install kivy==1.11.1
			-It's fails try "pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/"