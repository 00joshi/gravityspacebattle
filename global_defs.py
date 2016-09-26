import pygame
#defs
#size=(1024,768)
pygame.display.init()
size = pygame.display.list_modes()[0]
print("Display set to " + str(size))
screen=pygame.display.set_mode(size,pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
pygame.display.set_caption("PyGravity")
pygame.key.set_repeat(10, 30)

# Game Constants
G	= 6.67*10**(-11) # Gravity
