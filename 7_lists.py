fibonacci = [0,1,1,2,3,5,8,13,21,34]
print(fibonacci)
fruit = ["apple","banana","orange","grapefruit","watermelon"]
print(fruit)
youtubers = ["Lukers","pewdiepie","Jacksepticeye","Sidemen"]
print(youtubers)

songs = []
songs.append("Cigarettes, juice WRLD")
songs.append("Licorice, purport")
songs.append("F**k the world, Brent Faiyas")
songs.append("no role model z, j Cole")
songs.append("real friends, Kayne west")

books = []
print("what are your 5 favorite books")
books.append(input("enter the name of book 1"))
books.append(input("enter the name of book 2"))
books.append(input("enter the name of book 3"))
books.append(input("enter the name of book 4"))
books.append(input("enter the name of book 5"))
print(books)

pizza = []
print("what pizza toppings do you want")
pizza.append(input("enter topping #1"))
if pizza[-1] == "":
	pizza.pop()

pizza.append(input("enter topping #2"))
if pizza[-1] == "":
	pizza.pop()

pizza.append(input("enter topping #3"))
if pizza[-1] == "":
	pizza.pop()

pizza.append(input("enter topping #4"))
if pizza[-1] == "":
	pizza.pop()

pizza.append(input("enter topping #5"))
if pizza[-1] == "":
	pizza.pop()

pizza.append(input("enter topping #6"))
if pizza[-1] == "":
	pizza.pop()

print(pizza)


fruitlist = ["apple","banana","orange","grapefruit","watermelon"]

fruit = input("name a fruit")
if fruit not in fruitlist:
	fruitlist.append(fruit)
else:
	print("that's already in the list")

fruit = input("name a fruit")
if fruit not in fruitlist:
	fruitlist.append(fruit)
else:
	print("that's already in the list")

fruit = input("name a fruit")
if fruit not in fruitlist:
	fruitlist.append(fruit)
else:
	print("that's already in the list")

fruit = input("name a fruit")
if fruit not in fruitlist:
	fruitlist.append(fruit)
else:
	print("that's already in the list")

fruit = input("name a fruit")
if fruit not in fruitlist:
	fruitlist.append(fruit)
else:
	print("that's already in the list")

print(fruitlist)

names = ["Liam","noah","olivia","emma"]

names.sort()
print(names)
names.reverse()
print(names)

prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
prime_numbers.reverse()
print(prime_numbers)

prime_num = len(prime_numbers)
print(prime_num)


verb = ["be","have","do","say","get"]
verb.sort()
print(verb)
