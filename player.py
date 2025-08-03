import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y, shots_group_param, updatable, drawable):
		super().__init__(x, y, PLAYER_RADIUS)
		self.position = pygame.Vector2(x, y)
		self.rotation = 0
		self.shots = shots_group_param
		self.updatable = updatable
		self.drawable = drawable
		self.timer = 0

	# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def shoot(self):
		if self.timer > 0:
			return
		new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		self.timer = PLAYER_SHOOT_COOLDOWN
		self.shots.add(new_shot)
		new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED 
		self.updatable.add(new_shot)
		self.drawable.add(new_shot)

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

		if self.timer > 0:
			self.timer -= dt
			self.timer = max(self.timer, 0)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
