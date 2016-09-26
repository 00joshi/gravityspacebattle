import pygame
from global_defs import *
from playerlike import *

def FindSticks ():
	print("Found " + str(pygame.joystick.get_count()) + " Joysticks")
	joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

	for stick in joysticks:
		stick.init()
		print("Axis:" + str(stick.get_numaxes()))
		print("Buttons:" + str(stick.get_numbuttons()))

def HandleEvents (World):
#	global list_of_players
	list_of_players = World.list_of_players
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				World.done = True
			if event.key == pygame.K_SPACE:
				list_of_players[0].shoot()
			elif event.key == pygame.K_UP:
				list_of_players[0].turnleft()
			elif event.key == pygame.K_DOWN:
				list_of_players[0].turnright()
			elif event.key == pygame.K_LEFT:
				list_of_players[0].moveleft()
			elif event.key == pygame.K_RIGHT:
				list_of_players[0].moveright()
			elif event.key == pygame.K_PLUS:
				list_of_players[0].faster()
			elif event.key == pygame.K_MINUS:
				list_of_players[0].slower()
			else: print(event.key)
		elif event.type == pygame.JOYAXISMOTION:
			if joysticks[0].get_axis(0) > 0.7:
				list_of_players[1].moveright()
			elif joysticks[0].get_axis(0) < -0.7:
				list_of_players[1].moveleft()
			elif joysticks[0].get_axis(1) > 0.7:
				list_of_players[1].turnleft()
			elif joysticks[0].get_axis(1) < -0.7:
				list_of_players[1].turnright()
		elif event.type == pygame.JOYBUTTONDOWN:
			if joysticks[0].get_button(0):
				list_of_players[1].shoot()
			elif joysticks[0].get_button(4):
				list_of_players[1].slower()
			elif joysticks[0].get_button(6):
				list_of_players[1].faster()
