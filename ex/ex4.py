cars = int(100) # had to add in a value to the integer, declaring it as an int.
space_in_a_car = int(4.0)
drivers = int(30)
passengers = int(90)
cars_not_driven = cars - drivers # regular math functions after variables being declared work
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", (cars), 'cars available.')
print ("There are only", (drivers), 'drivers available.')
print ("There will be", (cars_not_driven), 'empty cars today.')
print ("We can transport", (carpool_capacity), 'people today.')
print ("We have", (passengers), 'to carpool today.')
print ("We need to put about", (average_passengers_per_car), 'in each car.')
# had to adapt program to python 3, ("beginning", (everything in between), end '')