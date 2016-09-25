import pygame
#defs
size=(1024,768)
screen=pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
pygame.display.set_caption("PyGravity")
pygame.key.set_repeat(10, 30)

# Game Constants
G	= 6.67*10**(-11) # Gravity
