import pygame
import time
from MyWorld import MyWorld
from screens import winscreen,messagescreen
from inputs import HandleEvents
from global_defs import *

class GravityGame():
	def __init__(self):
		self.clock=pygame.time.Clock()
		self.ThisWorld = MyWorld()
		self.ThisWorld.makeworld(0)
	def run(self):
		while self.ThisWorld.done == False:
			HandleEvents(self.ThisWorld)
			self.ThisWorld.update()
			for epl in self.ThisWorld.list_of_explosions:
				pygame.sprite.spritecollide(epl, self.ThisWorld.players, True, pygame.sprite.collide_circle)
			for p in self.ThisWorld.list_of_planets:
				pygame.sprite.spritecollide(p, self.ThisWorld.list_of_bullets, True, pygame.sprite.collide_circle)
				p.update()
			self.ThisWorld.players.draw(background)
			self.ThisWorld.list_of_bullets.draw(background)
			self.ThisWorld.list_of_explosions.draw(background)
			screen.blit(background, (0,0))
			self.clock.tick(20)
			pygame.display.flip()
		if len(self.ThisWorld.players)<2:
			# assuming we have some winner now that the game is over
			wscreen = winscreen(self.ThisWorld.players.sprites()[0].id)
		else:
			messagescreen("Cancelled by User")
		screen.blit(background, (0,0))
		pygame.display.flip()
		time.sleep(5)
		
