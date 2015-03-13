# Introduction to scener #

This module interacts with all hardware (or library like SDL, etc.). Its main tasks are:

**Send player events to _game logic_ through _wrapper_.** Read _updates_ from _game logic_ and draw it.

# Components #

Module contains the following elements:

**Object registry** ...

## Object registry ##

This registry contains all drawable elements (sprites) indexed by unique id (called **oid**). For each oid, one vector is stored. This vector contains references to all frames for the object.

Registry has many helpers, for example, it can to load any serie of srpites automatically (and performs vertical-flip).

Object registry can be modified in game time but it is a special feature. Normal use is populate it with all objects used in level and keep it unchanged until next level (if it is necessary).