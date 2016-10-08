#!/usr/bin/env python3
import pygame
from pygame.locals import *
import menu
import sys
import colors
from GravityGame import GravityGame
from inputs import FindSticks

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()

from global_defs import screen

#surface = pygame.display.set_mode((854, 480))
screen.fill((51, 51, 51))

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
FindSticks()

menu = menu.Menu()
menu.init(['Start', 'Options', 'Quit'], screen)  # necessary
#menu.move_menu(0, 0)  # optional
menu.draw()  # necessary

pygame.key.set_repeat(199, 69)  # (delay,interval)
pygame.display.update()
while 1:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_UP:
				# here is the Menu class method
				menu.draw(-1)
			if event.key == K_DOWN:
				# here is the Menu class method
				menu.draw(1)
			if event.key == K_RETURN:
				# here is the Menu class method 
				if menu.get_position() == 0:
					Game = GravityGame()
					Game.run()
					menu.draw()
					pygame.display.update()
				if menu.get_position() == 2:
					pygame.display.quit()
					sys.exit()
			if event.key == K_ESCAPE:
				pygame.display.quit()
				sys.exit()
			pygame.display.update()
		elif event.type == QUIT:
			pygame.display.quit()
			pygame.quit()
			#sys.exit()
	pygame.time.wait(8)
print("Good Bye")


