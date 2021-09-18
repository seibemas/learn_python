#i = 0
#numbers = []

#while i < 6:
#	print ("At the top i is %d" % i)
#	numbers.append(i)

#	i = i + 1
#	print ("Numbers now: ", (numbers))
#	print ("At the bottom i is %d" % i)

#print ("The numbers: ")

#for num in numbers:
#	print (num)


def buildList(num):
	numList = []
	i = 0
	while i < num:
		numList.append(i)
		i += 1
		print ("i: %d, " % i)
		print ("list: ", (numList))

buildList(6)