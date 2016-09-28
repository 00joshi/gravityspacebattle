import pygame
from global_defs import background, size
from colors import *
def menuscreen():
	wonfont = pygame.font.Font(None,35)
	menutitle = pygame.font.Font(None,35)
	menuitem = pygame.font.Font(None,25)
	srf_menutitle = wonfont.render("Menue",True,red)
	background.blit(srf_menutitle, (100,size[1]/2))
	return bar
class winscreen():
	def __init__(self,winner):
		wonfont = pygame.font.Font(None,35)
		#	wonfont.set_bold()
		text = winner + " has won"
		playerwon = wonfont.render(text,True,red)
		background.fill(darkblue)
		background.blit(playerwon, (size[0]/2-50,size[1]/2))

class messagescreen():
	def __init__(self,text):
		wonfont = pygame.font.Font(None,35)
		#	wonfont.set_bold()
		playerwon = wonfont.render(text,True,red)
		background.fill(darkblue)
		background.blit(playerwon, (size[0]/2-50,size[1]/2))
