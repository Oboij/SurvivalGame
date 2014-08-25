__author__ = 'Simon, Eddie, Mikael'

import pygame
import GUI
import handleEvent
import player
quit = False
eventHandler = handleEvent.handleEvent()
gui = GUI.GUI()
screen = gui.frame
glenn = player.player(screen)
def main():
     global quit
     while  not quit:
        event()
        update()
        render()
        hans()


def render():
    gui.player()

def event():
    global quit
    quit = eventHandler.exitEvent()

def update():
    pass
def hans():
    glenn.draw()
main()