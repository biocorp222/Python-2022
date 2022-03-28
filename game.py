########################
#IMPORTS
########################
from adventurelib import *

#######################
#DEFINE ROOMS
#######################
Room.items = Bag()
front_garden = Room("You are in a field with long grass, you can see the sea to the east and a castle in the distance")
west_field = Room("you are in a field with the broken statues of the past Kngs and Queens of the castle")
east_field = Room("you see a path to the broken castle tower and the sea to the east")
front_yard = Room("you are in a field with flower bushes an green grass, theres a path to the castle front door")
ruined_tower = Room("you are surrouned by rubble and the walls are riddled wiht bullet holes, there are guns and a chest in the corner")
castle_door = Room("Castle Door.  locked, you need a key")
courtyard = Room("theres a withered tree in the middle and some bushes and flowers surrounded the tree")
sleeping_quarters = Room("you need a light source to be able to see in this room")
dining_room = Room("there is a large table with many chairs surrounding it, there is also a set of drawers")
dungeon = Room("This is a dungeon. you will need a light")
##########################
#ROOM CONNECTIONS
##########################
front_garden.east = east_field
front_garden.west = west_field
east_field.north = ruined_tower
west_field.north = front_yard
front_yard.east = castle_door
ruined_tower.west = castle_door	

courtyard.west = dining_room
courtyard.east = sleeping_quarters
sleeping_quarters.north = dungeon

##########################
#ITEMS
##########################
Item.description = ""

key = Item("key", "keys")
key.description = "you look at the key and see that 'castle doors' is etched into it"

lantern = Item("lantern","light","torch")
lantern.description = "it is a lantern,it emmits light to be able to see things in dark rooms"


##########################
#VARIABLES
##########################
current_room = front_garden
chest_open = False
draws_checked = False
inventory = Bag()
used_key = False
##########################
#Binds
##########################


@when("open chest")
@when("chest")
def open_chest():
	global chest_open
	if current_room == ruined_tower and chest_open == False:
		print("you open the chest and see a key")
		chest_open = True 
		ruined_tower.items.add(key)
	elif current_room == ruined_tower and chest_open == True:
		print("you have already opened the chest")
	else:
		print("there is no chest here ")

@when("check drawers")
@when("drawers")
def open_draws():
	global draws_checked
	if current_room == dining_room and draws_checked == False:
		print("you open the drawers and see a lantern")
		draws_checked = True 
		dining_room.items.add(lantern)
	elif current_room == dining_room and draws_checked == True:
		print("you have already opened the drawers")
	else:
		print("there are no drawers here ")


@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if  direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}")
		print(current_room)
	else:
		print("you cant go that way")

@when("look")
def look():
	print(current_room)
	print("there are exits to the ",current_room.exits())
	if len(current_room.items) > 0:
		for item in current_room.items:
			print(item)

@when("get ITEM")
@when("take ITEM")
@when("pickup ITEM")
def get_item(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"you pickup {item}")
	else:
		print(f"you dont see a {item}")

@when("use ITEM")
def use(item):
	if item == "key" and current_room == castle_door:
		print("you use the key and the door opens")
		used_key = True 
		castle_door.north = courtyard



@when("bookcase")
def bookcase():
	if current_room == sleeping_quarters:
		print("you move the book case a see a stair case")
		sleeping_quarters.north = dungeon
		sleeping_quarters.west = ""

@when("use lantern")
@when("use light")
def use_lantern():
	if current_room == sleeping_quarters and draws_checked == True:
		Print("you see a BOOKCASE in the corner and some rows of beds")
	elif current_room == dungeon and draws_checked == True:
		print("you see knives and a fresh dead body in the corner")
	elif current_room == dungeon or sleeping_quarters and draws_checked == False:
		print("you do not have any source of light")
	else:
		Print("you cant do that here")



@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)




def main():
	print(current_room)
	start()
    

main()







