import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius

	
