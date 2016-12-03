from kivy.app import App
from kivy.lang import Builder
from kivy.core.image import Image
from kivy.core.window import Window


kv = '''
BoxLayout:
	orientation: 'vertical'
	Camera:
		id: camera
		resolution: 1920, 1080
	BoxLayout:
		orientation: 'horizontal'
		size_hint_y: None
		height: '48dp'
		Button:
			markup: True
			text: '[b][color=#0000]start[/b][/color]'
			on_release: camera.play = True
		Button:
			text: 'Stop'
			on_release:
				camera.play = False
				app.save_picture(camera.texture)
		Button:
			text: 'PrintScr'
			on_release: app.print_scr()
'''


class CameraApp(App):
	
	def build(self):
		return Builder.load_string(kv)

	def save_picture(self, picture):
		img = Image(picture)
		img.save('foto01.png')
	
	def print_scr(self, *largs):
		outname = 'foto02.png'
		Window.screenshot(name=outname)
	
if __name__ == '__main__':
	CameraApp().run()



