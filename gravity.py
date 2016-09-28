#!/usr/bin/env python3
import pygame

from GravityGame import GravityGame
from inputs import FindSticks

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
FindSticks()


Game = GravityGame()
Game.run()
print("Good Bye")
pygame.quit()
