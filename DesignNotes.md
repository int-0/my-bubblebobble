# Introduction #

This is a simple overview about the project. I will try to explain my own idea about the project without any details, jus only a simple introduction.

# End-product parts #

Final product should contains software package and many artwork packages (at least one).

## Software Package ##

Software package is my engine. Engine is formed by three modules: game logic, wrapper and scener.

### Game Logic ###

This module runs the game internally. It handles all object games, receives external events (player actions) and emits _update_ requests.

### Scener ###

This module show all graphics and plays sounds (and bgm) in any external hardware. Also, it can capture external events (like joystick axes, etc).

### Wrapper ###

This module _connects_ game logic with scener. If adaptation is needed, it is performed in this module.