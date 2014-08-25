__author__ = 'Simon, Eddie, Mikael'

import pygame

class handleEvent:
    #def __init__(self):


    def exitEvent(self):

        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if  key[pygame.K_ESCAPE]:

                return True

        return False

    def Event(self):

