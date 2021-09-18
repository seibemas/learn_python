print ("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
	print ("There's a giant bear here eating a cheese cake. What do you do?")
	print ("1. Take the cake.")
	print ("2. Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print ("The bear eats your face off. Better luck next time!")
	elif bear == "2":
		print ("The bear eats your legs off. Better luck next time!")
	else:
		print ("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
	print ("You stare into the endless abyss at Cthulhu's retina.")
	print ("1. Hello darkness my old friend.")
	print ("2. M'kphu Th'lek Ba.")
	print ("3. Mighty fine eye you got there sir.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print ("Your body and mind survive powered by the words of Cthulhu. Nice work!")
	else:
		print ("Fear and insanity rot your eyes into a pool of muck. Yikes!")

else:
	print ("You stumble around and fall on a knife and die. Whoopsie!")