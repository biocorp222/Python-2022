########################
#IMPORTS
########################
from adventurelib import *
from playsound import *
import webbrowser
#######################
#DEFINE ROOMS
#######################
Room.items = Bag()
front_garden = Room("You are in a field with long grass, you can see a path to the castle left")
west_field = Room("you are in a field with the broken statues of the past Kngs and Queens of the castle\nthe path continues to the north")
front_yard = Room("you are in a field with flower bushes youcan search and green grass, theres a path to the castle front door to the east")
ruined_tower = Room("you are surrouned by rubble and the walls are riddled wiht bullet holes, there is a chest in the corner")
castle_door = Room("Castle Door.  locked, you need a key\nthere is a castle tower to the east")
courtyard = Room("theres a withered tree in the middle and some bushes and flowers surrounded the tree")
sleeping_quarters = Room("you need a light source to be able to see in this room")
dining_room = Room("there is a large table with many chairs surrounding it, there is also a set of drawers\nthere is also a lock on the bottom draw\n""you will need a code""")
dungeon = Room("This is a dungeon. you will need a light")
##########################
#ROOM CONNECTIONS
##########################
front_garden.west = west_field
west_field.north = front_yard
front_yard.east = castle_door
ruined_tower.west = castle_door	
courtyard.west = dining_room
courtyard.east = sleeping_quarters
##########################
#ITEMS
##########################
Item.description = ""

paper = Item("paper","papers")
paper.description = "there is a code ghdfe \n can be used in the dining_room "

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
body_searched = False
bush = False
code = ""
##########################
#Binds
##########################

@when("look at paper")
@when("paper")
def look_paper():
	if "paper" in inventory:
		print("there is a code ghdfe \n can be used in the dining room ")
	else:
		print("you dont have paper")



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

@when("search bushes")
@when("search bush")
@when("bushes")
@when("bush")
def check_bush():
	global bush
	if current_room == front_yard and bush == False:
		print("you check the bushes and see a paper ")
		bush == True
		front_yard.items.add(paper)
	elif current_room == front_yard and bush == True:
		print("you have already opened the bushes")
	else:
		print("there are no bushes here ")

@when("code")
def code():
	if current_room == dining_room:
		passcode = (input("what is the code"))
		if passcode == "ghdfe":
			url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
			webbrowser.register('chrome',
				None,
				webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
			webbrowser.get('chrome').open(url)
		else:
			print("incorrect code")
	else:
		print("cant do that")




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
		


@when("no")
def no():
	url = 'https://www.youtube.com/watch?v=sntGta76v6Y'
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
	webbrowser.get('chrome').open(url)




@when("lantern")
@when("light")
def use_lantern():
	if current_room == sleeping_quarters and draws_checked == True:
		print("you see a BOOKCASE in the corner and some rows of beds")
	if current_room == dungeon and draws_checked == True:
		print("you see knives and a fresh dead body in the corner")
		sleeping_quarters.north = ""
	elif current_room == dungeon and draws_checked == False:
		print("you do not have a lantern")
	elif current_room == sleeping_quarters and draws_checked == False:
		print("you do not have a lantern")
	else:
		print("you cant use that here")

@when("search body")
def Body():
	if current_room	== dungeon and body_searched == False:
		print("you see a fresh stab wound in his abdamin and hear a noice behind you like a door creaking")
		print("you check the man's pockets and find a note saying 'you need to find the key'")
		print("you look around the room and see a chest covered and has a key hole ")
		print("you realise yu have athe key that your father gave you before he left and check if it works")
		print("the chest creaks open and reveals a sword marked with carvings")
		print("you realise you need to find and exit")

@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

def main():
	print("Prelogue")
	print("You were ten when your Father left, he was archaeologist.")
	print("you are now 21 and have decided to track his adveture and it has lead you to a remote part of asia")
	print(current_room)
	start()
    

main()