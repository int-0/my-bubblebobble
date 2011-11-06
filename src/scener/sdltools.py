#!/usr/bin/env python
#

import pygame
from pygame.locals import *

def load_image(fullname):
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image.convert_alpha()

def get_filenames(basename):
    for frame_n in range(1, 100):
        filename = basename + '%02d' % frame_n + '.png'
        yield filename

def vflip_frame(frame):
    return pygame.transform.flip(frame, 1, 0)

def hflip_frame(frame):
    return pygame.transform.flip(frame, 0, 1)

def new_frame(size):
    return pygame.Surface(size, SRCALPHA)
