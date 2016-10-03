import pygame
import math
from colors import *
from global_defs import *
from gy_math import pol2kart, gravity
from starlike import Planet
from bulletlike import *
class canon(pygame.sprite.Sprite):
	def __init__(self,world,id,position,basesize):
		pygame.sprite.Sprite.__init__(self)
		self.world = world
		self.id = id
		self.image = pygame.Surface([10,10])
		self.dead=0
		self.image.fill(red)
		self.angle=0.0*math.pi
		if position[0] > size[0]/2:
			self.angle=1*math.pi
		self.v0 = 20
		self.locfcenterpol = self.angle
		self.locfcenter = pol2kart(self.angle,basesize/2)
		self.position = position[0]+self.locfcenter[0],position[1]+self.locfcenter[1]
		self.rect = self.image.get_rect()
		self.player = self
		self.rect.center = self.position
		self.list_of_bullets = list()
		self.sound_shot = pygame.mixer.Sound('sounds/pew.wav') # Creative Commons by https://www.freesound.org/people/ani_music/
		self.sound_kill = pygame.mixer.Sound('sounds/kill.wav') # Creative Commons by https://www.freesound.org/people/Veiler/sounds/264031/
		self.sound_exp = pygame.mixer.Sound('sounds/explosion.wav') # Creative Common-0 https://www.freesound.org/people/wubitog/sounds/200466/
		pygame.mixer.init()
		self.base = Planet(position,basesize)
	def turnleft(self):
		self.angle += 0.0125*math.pi
	def turnright(self):
		self.angle -= 0.0125*math.pi
	def faster(self):
		if self.v0<40:
			self.v0 *= 1.025
	def slower(self):
		self.v0 /= 1.025
	def moveleft(self):
		self.locfcenterpol += 0.05*math.pi
		self.angle += 0.05*math.pi
	def moveright(self):
		self.locfcenterpol -= 0.05*math.pi
		self.angle -= 0.05*math.pi
	def update(self):
		self.locfcenter = pol2kart(self.locfcenterpol,self.base.radius)
		self.position = self.base.position[0]+self.locfcenter[0], self.base.position[1]+self.locfcenter[1]
		self.rect.center = self.position
		self.drawcanon()
		self.drawpreview ( )
	def drawcanon(self):
		self.rohr = pygame.Surface([100,100])
		self.dx, self.dy = pol2kart(self.angle,20)
		self.rohrrect = pygame.draw.line(self.rohr,red,[50,50],[self.dx+50,self.dy+50])
		self.rohr.set_colorkey((0,0,0))
		self.rohr.convert_alpha()
		background.blit(self.rohr,[self.position[0]-50,self.position[1]-50])
	def drawpreview ( self ):
		self.snapshot = pygame.Surface ( [3, 3] )
		self.snapshot.fill ( (96, 96, 96) )
		pos, v = self.position , pol2kart ( self.angle, self.v0 )
		for i in range ( 15 ): # length of preview
			pos, v = gravity ( self.world,pos, v, mass = 1, delta_t = 1 )
			background.blit ( self.snapshot, pos )
	def kill(self):
		self.remove(self.world.players)
		self.dead=1
		self.sound_kill.play()
	def shoot(self):
		if self.dead == 0:
			self.sound_shot.play()
			self.world.list_of_bullets.add ( Bullet ( self.world, self.player, self.position, self.angle, self.v0 ) )
