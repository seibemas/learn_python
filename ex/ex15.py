from sys import argv
# argv with 2 arguments prompted at shell. v
script, filename = argv
# define filename input on shell as txt, open it.
txt = open(filename)
# print said filename
print ("Here's your file %r:" % filename)
# read command to 'open' the file and print it on the shell.
print (txt.read())
# prompt for the filename again.
print ("Type the filename again:")
# define the input as file_again.
file_again = input("> ")
# open the input as txt_again.
txt_again = open(file_again)
# read command to 'open' the input defined as file_again, and print it on the shell.
print (txt_again.read())