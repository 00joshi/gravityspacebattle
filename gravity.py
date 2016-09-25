#!/usr/bin/env python3
import pygame
import math
import time
from starlike import Planet
from colors import *
from global_defs import *
from bulletlike import *
from playerlike import *
from gy_math import gravity, pol2kart
from inputs import HandleEvents, FindSticks
from MyWorld import MyWorld


pygame.init()
FindSticks()
global list_of_masses
#print pygame.font.get_fonts()

done=False
clock=pygame.time.Clock()

def menuscreen():
	wonfont = pygame.font.Font(None,35)
	menutitle = pygame.font.Font(None,35)
	menuitem = pygame.font.Font(None,25)
	srf_menutitle = wonfont.render("Menue",True,red)
	background.blit(srf_menutitle, (100,size[1]/2))
	return bar
def winscreen(winner):
	wonfont = pygame.font.Font(None,35)
#	wonfont.set_bold()
	text = winner + " has won"
	playerwon = wonfont.render(text,True,red)
	background.blit(playerwon, (size[0]/2-50,50))
	
def drawenvironment():
	background.fill(darkblue)


###
#list_of_planets,list_of_players = makeworld(1)

ThisWorld = MyWorld()
ThisWorld.makeworld(1)

for p in ThisWorld.list_of_players:
	ThisWorld.players.add(p)

for p in ThisWorld.list_of_planets:
	ThisWorld.list_of_masses.append([p.position[0],p.position[1],p.mass])

while done == False:
	HandleEvents(ThisWorld)
	ThisWorld.list_of_bullets.update(ThisWorld.list_of_masses)
	ThisWorld.list_of_explosions.update()
	drawenvironment()
	for epl in ThisWorld.list_of_explosions:
		pygame.sprite.spritecollide(epl, ThisWorld.players, True, pygame.sprite.collide_circle)
	for p in ThisWorld.list_of_planets:
		pygame.sprite.spritecollide(p, ThisWorld.list_of_bullets, True, pygame.sprite.collide_circle)
		p.update()
	ThisWorld.players.update()
	ThisWorld.players.draw(background)
	ThisWorld.list_of_bullets.draw(background)
	ThisWorld.list_of_explosions.draw(background)
	if len(ThisWorld.players) == 1:
		done = True
		winscreen(ThisWorld.players.sprites()[0].id)
	screen.blit(background, (0,0))
	clock.tick(20)
	pygame.display.flip()
	if done == True:
		time.sleep(1)
