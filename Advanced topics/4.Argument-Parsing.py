from Terminal import clear_terminal
import sys

clear_terminal()
# argv[0] is the name of the file, 1 is the first text we write in console and 2 is the second, etc
print(sys.argv[0])
# no [] would print everything you input.
clear_terminal()

#Usage: main.py FILENAME

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)
# python3 4.Argument-Parsing.py text.txt "Hello World"  

# to add optional arguments like -p for port, etc, we do this:
import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])  #if there is a : after f,m,etc it expects it

print(opts)
print(args)

#python3 4.Argument-Parsing.py -f text.txt -m  "Hello World"  -f and -m now putting it in opts
#reversing order but keeping -f before filename and -m before message still works the same
