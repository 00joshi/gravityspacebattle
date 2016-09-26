import pygame
from playerlike import *
from starlike import *
class MyWorld():
	# Lists
	def __init__(self):
		self.list_of_explosions = pygame.sprite.Group()
		self.list_of_bullets = pygame.sprite.Group()
		self.list_of_masses = list()
		self.list_of_planets = list()
		self.list_of_players = list()
		self.players = pygame.sprite.Group()
		self.done = True
	def makeworld(self,level):
		self.done = False
		if level ==1:
			self.list_of_planets = [Planet([600,400],50),Planet([200,400],80),Planet([400,250],100)]
			player = canon(self,"Player 1",[50,100],40)
			player2 = canon(self,"Player 2",[700,200],40)
			self.list_of_players = [player,player2]
			self.list_of_planets.append(player.base)
			self.list_of_planets.append(player2.base)
#	elif level == 2:
#		list_of_planets = [Star([size[0]/2,size[1]/2],100),]
#		player = canon("Player 1",[50,100],40)
#		player2 = canon("Player 2",[700,200],40)
#		list_of_players = [player,player2]
#	return list_of_planets,list_of_players
