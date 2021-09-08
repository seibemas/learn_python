#v imports argv from system.
from sys import argv

#v define argv
script, input_file = argv

#v this function prints the whole file.
def print_all(f):
	print (f.read())

#v this function enables rewind of files, seek goes to beginning of file.
def rewind(f):
	(f.seek(0))

#v this function prints lines 1 by 1
def print_a_line(line_count, f):
	print (line_count, (f.readline()))

#v defines current_file as the input_file and opens it.
current_file = open(input_file)

print ("First let's print the whole file:\n")

#v prints whole file defined.
print_all(current_file)

print ("Now let's rewind, kind of like a tape.\n")

#v rewinds file to line 1.
rewind(current_file)

print ("Let's print three lines:\n")

#v current_line is line one.
current_line = 1

#v prints one line, current_line from current_file.
print_a_line(current_line, current_file)

#v takes current_line and adds 1.
current_line = current_line + 1

#v prints one line, current_line (2 in this case), from current_file (input file).
print_a_line(current_line, current_file)

#v takes current_line + 1, and adds + 1 making it line 3.
current_line = current_line + 1

#v prints one line, current_line (3 in this case), from the current_file (input file).
print_a_line(current_line, current_file)
