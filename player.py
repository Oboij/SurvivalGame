__author__ = 'Simon'
import pygame
class player():
    x = 300
    y = 400
    width = 50
    height = 50
    screen = 0
    color = (255, 230, 50)

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()