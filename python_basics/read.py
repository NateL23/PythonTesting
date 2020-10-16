# reads in a files contents and prints it line by line
file = open('test.txt')

for line in file.readlines():
    print(line)

file.close()

# $ print(file.read(2))
#   read n number of characters by passing parameter, read all with no parameters
#   file read control will pause at the last character it read in

# $ print(file.readline())
# $ print(file.readline())
#   read in a single line at a time

# $ line = file.readline()
# $ while line != '':
# $     print(line)
# $     line = file.readline()
#   print line by line usine readline method
