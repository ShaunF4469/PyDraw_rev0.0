#---necessary modules loaded below:---

import pygame
import os
import sys
import csv

pygame.init()

#---Function definitions:---
def etype():
        etype = 0
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                etype = 99  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                etype = 1
        clock.tick(60)
        return etype

def uiEvents():
    #-get type of event
    uiEvents().cat = etype()
    #-get positions and deltas for x & y
    uiEvents.xpos, uiEvents.ypos = pygame.mouse.get_pos()
    uiEvents.xdelta, uiEvents.ydelta = pygame.mouse.get_pos()
    
#---Global Variables:---
pygame.display.set_caption("EventsTracker")
size = (500, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#---Colors---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#---Init screen---
screen.fill(WHITE)

#---Main loop:---
#Loop until the user clicks the close button.
done = False
while not done:
    if uiEvents().cat == 99:
        print(uiEvents().cat)
        done = True

    # Limit to 60 frames per second
    clock.tick(60)

# --- Close the window and quit.
pygame.quit()