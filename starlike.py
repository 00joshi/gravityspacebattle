# StarLike
import pygame
from colors import *
from global_defs import background
class Planet(pygame.sprite.Sprite):
	def __init__(self,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([size,size])
		self.rect = pygame.draw.circle(self.image,blue,[int(size/2),int(size/2)],int(size/2))
		self.rect.center = position
		self.radius=size/2
		self.position = position
		self.mass = 10**9*size**3
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
	def update(self):
		background.blit(self.image, self.rect)

class Star(Planet):
	def __init__(self,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([size,size])
		self.rect = pygame.draw.circle(self.image,yellow,[int(size/2),int(size/2)],int(size/2))
		self.rect.center = position
		self.radius=size/2
		self.position = position
		self.mass = 10**9*size**3*1.0
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
