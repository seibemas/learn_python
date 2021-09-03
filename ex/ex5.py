my_name = "Mason R. Seibert"
my_age = int(27) # really, I am 27.
my_height = int(61) # inches
my_weight = int(250) # pounds
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Dark Brown"
my_total = my_age + my_height + my_weight

#print ("Let's talk about", (my_name), '.')
#print ("He's", (my_height), 'inches tall.')
#print ("He's", (my_weight), 'pounds heavy.')
#print ("That isn't too heavy.")
#print ("He has", (my_eyes), 'eyes and', (my_hair), 'hair.')
#print ("His teeth are usually", (my_teeth), 'depending on the coffee and smokes.')

#print ("If I add", (my_age), ",", (my_height), ', and', (my_weight), 'I get', (my_total),'.')

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Not too heavy actually.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# multiple calls to % need to be in parenthesis
# and within the parenthesis for print, after quotes.