########################
#IMPORTS
########################
from adventurelib import *


#######################
#DEFINE ROOMS
#######################
room.items = Bag()

front_garden = Room("You are in a field with long grass, you can see the sea to the east and a castle in the distance")
west_field = Room("you are in a field with the broken statues of the past Kngs and Queens of the castle")
east_field = Room("you see a path to the broken castle tower and the sea to the east")
front_yard = Room("you are in a field with flower bushes an green grass, theres a path to the castle front door")
ruined_tower = Room("you are surrouned by rubble and the walls are riddled wiht bullet holes, there are guns and a chest in the corner")
castle_door = Room("locked, you need a key")
courtyard = Room("theres a withered tree in the middle and some bushes and flowers surrounded the tree")
sleeping_quarters = Room("there are rows and roowsa of bunk-bedsalong with bedside tables and a creepy flickering light")
dining_room = room("there is a large table with many chairs surrounding it, there is also a set of drawers")
dungeon