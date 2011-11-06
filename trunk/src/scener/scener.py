#!/usr/bin/env python
#
import sdltools

# FIXME: constant or tile-dependand?
TILE_OVERLAP = 3

class InvalidScenerOperation(Exception):
    def __init__(self, msg):
        self.__str = msg

    def __str__(self):
        return repr(self.__str)

class Scener:
    def __init__(self, destination, object_registry):

        self.__scr = destination
        self.__sprites = object_registry

        self.__backg = None

        self.__map = None
        self.__tiles = None
        self.__map_mask = None

        self.__objects = {}

    def set_background(self, background):
        self.__backg = sdltools.load_image(background)

    def set_map(self, map_data):
        # Map data is a vector, first two values define size of map,
        # ramaining bytes is a 1-bit bitmap
        try:
            size_x = map_data[0]
            size_y = map_data[1]
            map_data = map_data[2:]
            map_data.reverse()
        except:
            raise InvalidScenerOperation('Invalid map data!')

        expected_bytes = int(size_x/8)
        if (size_x % 8 != 0):
            expected_bytes += 1
        expected_bytes *= size_y

        if len(map_data) < expected_bytes:
            raise InvalidScenerOperation('Invalid map, needs %i bytes but %i found' % (expected_bytes, len(map_data)))

        self.__map_mask = []
        for y in range(size_y):
            row = []
            bit = 0
            mask = map_data.pop()
            for x in range(size_x):
                row.append((mask >> bit) & 1)
                bit += 1
                if bit > 7 and (x < (size_x - 1)):
                    mask = map_data.pop()
                    bit = 0
            self.__map_mask.append(row)
        self.__rebuild_map()

    def set_tileset(self, tileset):
        if not self.__sprites.object_exists(tileset):
            raise InvalidScenerOperation('Tileset not registered: ' + tileset)
        self.__tiles = tileset
        self.__rebuild_map()

    def __rebuild_map(self):
        if ((self.__tiles is None) or (self.__map_mask is None)):
            return

        tile = self.__sprites.get_frame(self.__tiles, 0)
        tile_size_x, tile_size_y = tile.get_size()
        map_size_y = len(self.__map_mask)
        map_size_x = len(self.__map_mask[0])
        map_dimension = ((map_size_x * (tile_size_x - TILE_OVERLAP)) + 0,
                         (map_size_y * (tile_size_y - TILE_OVERLAP)) + 0)
        self.__map = sdltools.new_frame(map_dimension)

        # Draw down-top for keep drawing preference
        for y in range(len(self.__map_mask)):
            for x in range(len(self.__map_mask[y])):
                x_scr = x * (tile_size_x - TILE_OVERLAP)
                y_scr = ((map_size_y - 1) - y) * (tile_size_y - TILE_OVERLAP)
                if self.__map_mask[(map_size_y - 1) - y][x] == 1:
                    self.__map.blit(tile, (x_scr, y_scr))
                

    def add_object(self, oid, data):
        pass

    def modify_object(self, oid, data):
        pass

    def kill_object(self, oid, data):
        pass

    def __update_object(self, oid):
        pass

    def update(self, pos = (0, 0)):
        if not self.__backg is None:
            self.__scr.blit(self.__backg, pos)
        if not self.__map is None:
            self.__scr.blit(self.__map, pos)
        for object_id in self.__objects.keys():
            self.__scr.blit(self.__update_object(object_id),
                            self.__objects[object_id]['screen_position'])

        
