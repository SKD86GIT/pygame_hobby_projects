import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Set up display screen
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Set window title
pg.display.set_caption("OOPs Game Window Example")

ufo_01 = pg.image.load("assets/ufo.png")
UFO_MOVE_X = (600-64)//2
UFO_MOVE_Y = (400-64)//2+160
UFO_MOVE_X_CHANGE = 0

# Load and display UFO image at the center of the screen
def display_ufo(X, Y):
    screen.blit(ufo_01, (X, Y)) 

def set_X(X, UFO_MOVE_X_CHANGE):
    X += UFO_MOVE_X_CHANGE
    if X >= (WIDTH-64):
        X = (WIDTH-64)     
    elif X <=0:
        X = 0
    return X

def handl_events(e, UFO_MOVE_X_CHANGE, running):
    # Event handling
    for event in e:
        # Quit event
        if event.type == pg.QUIT:
            running = False
        
        # Escape key to quit
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        
        
        if event.type == pg.KEYDOWN:
            # Move UFO right with right arrow key
            if event.key == pg.K_RIGHT:
                UFO_MOVE_X_CHANGE += 1
            # Move UFO left with left arrow key
            if event.key == pg.K_LEFT:
                UFO_MOVE_X_CHANGE -= 1


        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                UFO_MOVE_X_CHANGE = 0
            if event.key == pg.K_LEFT:
                UFO_MOVE_X_CHANGE = 0
    return UFO_MOVE_X_CHANGE, running


# Main game loop
running = True
while running:
    screen.fill((2, 5, 65))
    event_list = pg.event.get()

    UFO_MOVE_X_CHANGE, running = handl_events(event_list, UFO_MOVE_X_CHANGE, running)


    # Update UFO position
    UFO_MOVE_X = set_X(UFO_MOVE_X, UFO_MOVE_X_CHANGE)


    display_ufo(UFO_MOVE_X, UFO_MOVE_Y)
    pg.display.update()

pg.quit()

