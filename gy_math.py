import math
from global_defs import G
def pol2kart(angle,v):
	x = v * math.cos(angle)
	y = -v * math.sin(angle)
	return x,y

def gravity ( world, pos = [0, 0], speed = [0, 0], mass = 1, delta_t = 1 ):
	pos = (pos[0] + speed[0] * delta_t, pos[1] + speed[1] * delta_t)
	f = [0,0]
	for m in world.list_of_masses:
		dist = math.sqrt ( ( m[0] - pos[0] )**2 + ( m[1] - pos[1] )**2 )
		f[0] += m[2] * mass * G * ( m[0] - pos[0] ) / dist**3
		f[1] += m[2] * mass * G * ( m[1] - pos[1] ) / dist**3
	speed = (speed[0] + delta_t * f[0] / mass, speed[1] + delta_t * f[1] / mass)
	return pos, speed
