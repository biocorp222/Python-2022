#import all the functions from adventurelib
from adventurelib import *

#rooms
room.items = Bag()

space = Room(""" You are drifting in space. you see a spaceship""")
airlock = Room("""you are in an airlock""")
cargo = Room("""you are in the cargo bay """)
docking = Room(""" You are in the docking bay""")
hallway = Room(""" you are in the hallway with four exits """)
bridge = Room(""" you stand on the bridge of the ship. there is a dead body here""")
quarters = Room(""" You are in the crew quarters. There is a locker""")
mess_hall = Room("""you are in the Kitchen/dining area""")
escape_pods = Room("""you are in an escape pod """)

#room connections
docking.west = cargo
hallway.north = cargo
hallway.south = mess_hall 
hallway.north = airlock
hallway.west = bridge
bridge.south = escape_pods
mess_hall.west = quarters
quaters.north = airlock

#items
item.description = "" #make sure each item has a describtion
keycard = item("a red keycard","keycard","card","key","red keycard")
keycard.description = "You look at the kaycard and see that it is labelled Escape pods"

note = item("a scribbled note","note","paper","paper","code")
note.description = "you look at the note. the numbers 2,3,5,4 are scribbled"

#add items to rooms
quarters.items.add(note)

#Variables
current_room = space
inventory = Bag()
body_searched = False
used_keycard = False
#binds
@when("jump")
def jump():
	print("you jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else:
		print("There is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if  direction in current_room.exits():
		#checks if the current room list of exits
		#has the diorection the player wants to go
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
	#check i item is in room
	#take out of room 
	#put in inventory
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"you pickup {item}")
	else:
		print(f"you dont see a {item}")

@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	if current_room == bridge and body_searched == false:
		print("you search the body and a red keycard falls to the floor")
		current_room.items.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched == True:
		print("you already searched the body")
	else:
		print("There is no body here")


@when("use ITEM")
def use(item):
	if item == keycard and current_room == bridge:
		print("You ise teh keycard and the escape pod slides open")
		print("The escape pod stands open to the south")
		used_keycard = True 
		bridge.south = escape


@when("type code")
def escape_pod_win():
	if note in inventory: 
		if current_room == escape:
			print("you enter teh code and escape. You win"):
		else:
			print("")
		




#EVERRYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
    #start the main loop
main()