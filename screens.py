import pygame
from global_defs import background, size
from colors import *
pygame.font.init()
font=[pygame.font.Font(None,35),pygame.font.Font(None,25),pygame.font.Font(None,18)]
def menuscreen():
	srf_menutitle = font[0].render("Menue",True,red)
	background.blit(srf_menutitle, (100,size[1]/2))

class winscreen():
	def __init__(self,winner):
		#	wonfont.set_bold()
		text = winner + " has won"
		playerwon = font[0].render(text,True,red)
		background.fill(darkblue)
		background.blit(playerwon, (size[0]/2-50,size[1]/2))

class messagescreen():
	def __init__(self,text):
		playerwon = font[0].render(text,True,red)
		background.fill(darkblue)
		background.blit(playerwon, (size[0]/2-50,size[1]/2))
