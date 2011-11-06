#!/usr/bin/env python
#

import os
import sdltools

class InvalidObject(Exception):
    def __init__(self, msg):
        self.__str = msg

    def __str__(self):
        return repr(self.__str)

class ObjectRegistry:
    def __init__(self):
        self.__registry = {}

    def object_exists(self, oid):
        return self.__registry.has_key(oid)

    def __check_oid_exists(self, oid):
        if not self.object_exists(oid):
            raise InvalidObject('Undefined oid: ' + str(oid))

    def get_frame(self, oid, frame_number):
        self.__check_oid_exists(oid)
        if frame_number >= self.__registry[oid]:
            raise InvalidObject('Frame out of range: ' + str(frame_number))
        return self.__registry[oid][frame_number]

    def unregister_object(self, oid):
        if not self.object_exists(oid):
            return
        del(self.__registry[oid])

    def number_of_frames(self, oid):
        self.__check_oid_exists(oid)
        return len(self.__registry[oid])

    def add_frame(self, oid, frame):
        if not self.object_exists(oid):
            self.__registry[oid] = []
        self.__registry[oid].append(frame)

    def load_frame(self, oid, filename):
        frame = sdltools.load_image(filename)
        self.add_frame(oid, frame)

    # Helper to make flips sprites
    def add_frame_vflip(self, oid, frame):
        self.add_frame(oid, sdltools.vflip_frame(frame))

    # Helper to load sprite-sheets
    def load_sprites(self, oid, basename):
        for sprite_file in sdltools.get_filenames(basename):
            if not os.path.exists(sprite_file):
                break
            self.load_frame(oid, sprite_file)

    # Helper to load vfliped sprite-sheets
    def load_sprites_vflip(self, oid, basename):
        for sprite_file in sdltools.get_filenames(basename):
            if not os.path.exists(sprite_file):
                break
            self.add_frame_vflip(oid, sdltools.load_image(sprite_file))
