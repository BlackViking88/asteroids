import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen,"white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)	
	
	def split(self, asteroids):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		new_velocity1 = self.velocity.rotate(random_angle)
		new_velocity2 = self.velocity.rotate(-random_angle)
		new_radius1 = self.radius - ASTEROID_MIN_RADIUS
		new_radius2 = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius1)
		new_asteroid1.velocity = new_velocity1 * 1.2
		new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius2)
		new_asteroid2.velocity = new_velocity2 * 1.2

		asteroids.add(new_asteroid1)
		asteroids.add(new_asteroid2)


		
		


	
