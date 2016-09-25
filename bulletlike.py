import pygame
from gy_math import pol2kart,gravity
from global_defs import *
from colors import *
class Bullet(pygame.sprite.Sprite):
	def __init__(self,world,playername,position,angle,v0):
		#self.canonid=canonid
		pygame.sprite.Sprite.__init__(self)
		self.world = world
		self.image = pygame.Surface([5,5])
		if playername == world.list_of_players[0]:
			self.color = violet
		elif playername == world.list_of_players[1]:
			self.color = yellow
		self.rect = pygame.draw.circle(self.image,self.color,[3,3],2)
		self.rect.center = position
		self.position = position
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
		self.v = list(pol2kart(angle,v0))
		self.mass = 0.1
	def update(self,masses = list()):
		self.position, self.v = gravity ( self.world,self.position, self.v, self.mass, delta_t = 1 )
		self.rect.center = self.position
		if abs(self.rect.center[0]) > 5000 or abs(self.rect.center[1]) > 5000:
			self.kill()

	def blit(self):
		background.blit(self.image, self.rect)
	def kill(self):
		self.remove(self.world.list_of_bullets)
		self.world.list_of_explosions.add(Explosion(self.position))

class Explosion(pygame.sprite.Sprite):
	def __init__(self,position):
		self.size = 30
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([self.size,self.size])
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
		self.rect = pygame.draw.circle(self.image,red,[int(self.size/2),int(self.size/2)],int(self.size/2))
		self.ttl = 5
		self.position = position
		self.rect.center = self.position
	def update(self):
		self.ttl-=1
		if self.ttl == 0:
			self.kill()
