#the first two lines setup the context
#of the program and an initial state of 
#the order_complete variable to false
#as well as an empty list for toppings
print("Hi, welcome to ice cram maker")
order_complete = False
toppings_list = []

#the loop hegins here and will complete 
#when order_complete is no longer false
while order_complete == False:
	toppping = input("what topping - push enter to finish")
	if toppping == "":
		print("order done")
		order_complete = true