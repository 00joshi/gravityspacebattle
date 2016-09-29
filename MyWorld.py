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
	def drawenvironment(self):
		background.fill(darkblue)
	def makeworld(self,level):
		self.done = False
		self.drawenvironment()
		if level ==1:
			self.list_of_planets = [Planet([6/10*size[0],4/7*size[1]],50),Planet([2/10*size[0],4/8*size[1]],80),Planet([4/10*size[0],3/8*size[1]],100)]
			player = canon(self,"Player 1",[1/10*size[0],1/8*size[1]],60)
			player2 = canon(self,"Player 2",[7/10*size[0],2/8*size[1]],60)
		elif level == 2:
			self.list_of_planets = [Star([size[0]/2,size[1]/2],200),Planet([1/5*size[0],4/5*size[1]],100),Planet([4/5*size[0],1/5*size[1]],150)]
			player = canon(self,"Player 1",[1/5*size[0],1/5*size[1]],60)
			player2 = canon(self,"Player 2",[4/5*size[0],4/5*size[1]],60)
		self.list_of_players = [player,player2]
		self.list_of_planets.append(player.base)
		self.list_of_planets.append(player2.base)
		
		for p in self.list_of_players:
			self.players.add(p)

		for p in self.list_of_planets:
			self.list_of_masses.append([p.position[0],p.position[1],p.mass])
		
	def update(self):
		self.drawenvironment()
		self.list_of_bullets.update(self.list_of_masses)
		self.list_of_explosions.update()
		self.players.update()
		if len(self.players)<2:
			self.done = True
#	return list_of_planets,list_of_players
