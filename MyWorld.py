import pygame
from playerlike import *
from starlike import *
from random import randrange
class MyWorld():
	# Lists
	def __init__(self):
		self.list_of_explosions = pygame.sprite.Group()
		self.list_of_bullets = pygame.sprite.Group()
		self.list_of_masses = list()
		self.list_of_planets = pygame.sprite.Group() #list()
		self.list_of_players = list()
		self.players = pygame.sprite.Group()
		self.done = True
	def drawenvironment(self):
		background.fill(darkblue)
	def makeworld(self,level):
		self.done = False
		self.drawenvironment()
		if level == 0:
			psize = randrange(50,100)
			list_of_players = [canon(self,"Player 1",[randrange(100,size[0],100),randrange(100,size[1],100)],psize),canon(self,"Player 2",[randrange(100,size[0],100),randrange(100,size[1],100)],psize)]
			for i in range(10):
				iplanet = Planet([randrange(100,size[0]-100,100),randrange(100,size[1]-100,100)],randrange(10,150))
				if pygame.sprite.spritecollide(iplanet,self.list_of_planets, True, pygame.sprite.collide_circle):
					i-=1
				self.list_of_planets.add(iplanet)
				if pygame.sprite.spritecollide(player.base,self.list_of_planets, True, pygame.sprite.collide_circle):
					i-=1
				if pygame.sprite.spritecollide(player2.base,self.list_of_planets, True, pygame.sprite.collide_circle):
					i-=1

		if level ==1:
			self.list_of_planets = [Planet([6/10*size[0],4/7*size[1]],50),Planet([2/10*size[0],4/8*size[1]],80),Planet([4/10*size[0],3/8*size[1]],100)]
			self.list_of_players = [canon(self,"Player 1",[1/10*size[0],1/8*size[1]],60),canon(self,"Player 2",[7/10*size[0],2/8*size[1]],60)]
		elif level == 2:
			self.list_of_planets = [Star([size[0]/2,size[1]/2],200),Planet([1/5*size[0],4/5*size[1]],100),Planet([4/5*size[0],1/5*size[1]],150)]
			list_of_players = [canon(self,"Player 1",[1/5*size[0],1/5*size[1]],60), canon(self,"Player 2",[4/5*size[0],4/5*size[1]],60)]
		for player in list_of_players: 
			self.list_of_planets.add(player.base)
		
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
