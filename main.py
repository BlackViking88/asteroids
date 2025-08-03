import pygame
import sys
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots, updatable, drawable)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		updatable.update(dt)
		for each in asteroids:
			if each.collision(player):
				print("Game over!")
				sys.exit()

		for each in asteroids:
			for shot in shots:
				if each.collision(shot):
					shot.kill()
					each.split(asteroids)

		for draw_this in drawable:
			draw_this.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
	main()
