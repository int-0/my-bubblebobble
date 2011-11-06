#!/usr/bin/env python
#

import os
import sys

import pygame
from pygame.locals import *

# Expected location in repo
sys.path.append('../src/scener')

from objects import ObjectRegistry
from scener import Scener

def get_screen():
    return pygame.display.set_mode((640, 480), FULLSCREEN)

def encode_map(bitmap):
    size_y = len(bitmap)
    size_x = len(bitmap[0])
    encoded_map = [size_x, size_y]
    for row in bitmap:
        bit = 0
        mask = 0
        x = 0
        for column in row:
            x = x + 1
            mask = mask | (column << bit)
            bit += 1
            if bit > 7:
                #print x
                encoded_map.append(mask)
                mask = 0
                bit = 0
        if bit > 0:
            #print x
            encoded_map.append(mask)
    return encoded_map

def main():
    pygame.init()
    screen = get_screen()

    # Load map file
    sprites = ObjectRegistry()
    sprites.load_frame('tile', 'tile.png')

    # Make scener
    scene = Scener(screen, sprites)

    # Set background
    scene.set_background('background.png')

    # Set map
    level = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1],
        [1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    scene.set_tileset('tile')
    scene.set_map(encode_map(level))

    # Loop until quit
    do_quit = False
    while not do_quit:
        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                do_quit = True
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    do_quit = True
                    break

        # Draw Everything
        scene.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
