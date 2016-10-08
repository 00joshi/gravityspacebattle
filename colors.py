#Define Colors
black	= (0,0,0)
white	= (255,255,255)
green	= (0,255,0)
red	= (255,0,0)
grey	= (128,128,128)
blue	= (0,0,255)
yellow	= (255,255,0)
violet	= (255,0,255)
darkblue = (0,0,33)


class ColorCollection(object):
	colors = [red, green, grey, yellow, violet]
	def init():
		self.colors = [red, green, grey, yellow, violet]
	def pop(self):
		return(self.colors.pop())
	def reset(self):
		self.colors.clear()
		self.colors.extend([red, green, grey, yellow, violet])
