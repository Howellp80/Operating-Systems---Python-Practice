#!/bin/python3
#
# Program Py
# Parker Howell
# 10/15/17
# CS344 - Operating Systems
# Description - Program will create 3 files in the current directory and
#               add to each a string of 10 random characters from the 
#               lowercase alphabet. The contents of the 3 files will then
#               be printed to the screen. Finally two random integers
#               between 1 - 42 inclusive will be generated and they and their 
#               product will be displayed. 
#

import random



###############################################################################
# makeStrings
# crates 3 strings of 10 random lowercase characters and returns them
###############################################################################
def makeStrings():
	stringArr = []
	# create 3 strings
	for num in range(0, 3):
		#print ("In array loop ", num)
		#randString will store each string as its made
		randString = ""
		# generate 10 random numbers
		for number in range(0, 10):
			#print ("in string loop")
			# 97 - 122 is ascii a-z. randrange goes up 
			# to, but excludes the top of the range- 123
			randInt = random.randrange(97, 123 )
			#print (randInt)
			# convert the int to a char
			randChar =  chr(randInt)
			#print (randChar)
			# add the char to the string
			randString +=  randChar
		#print ("randString: ", randString)
		
		# add the trailing newline to the string
		randString += "\n"

		# add the string to the array
		stringArr.append(randString)
			
	# return array with 3 random strings	
	return stringArr




###############################################################################
# saveStings
# writes the 3 stings to files in the current directory
###############################################################################
def saveStrings(stringArr):
	#print ("in saveStrings")
	# creates an array of file names to save our strings to
	files = []
	for num in range(0, 3):
		files.append("file" + str(num + 1) + ".txt")
		#print (files[num])
		
		# as we make filenames, write the corresponding string to it
		# "with" will automatically close the opened file
		# "open" will create the file if it doesnt exist
		# "w" is the write option
		with open(files[num], "w") as f:
			f.write(stringArr[num])




###############################################################################
# printStrings
# prints the 3 stings to the console
###############################################################################
def printStrings(stringArr):
	#print ("in printStrings")
	for num in range(0, 3):
		# end="" removes the default newline from the print command
		print(stringArr[num], end="")
	
	


###############################################################################
# genInts
# generates 2 random ints between 1 - 42 inclusive and returns them
###############################################################################
def genInts():
	#print("in genInts")
	# randrange excludes the top of the range- 43
	int1 = random.randrange(1, 43)
	int2 = random.randrange(1, 43)
	#print(int1, int2)
	
	return int1, int2




###############################################################################
# prodInts
# calculates and returns the product of 2 ints
###############################################################################
def prodInts(int1, int2):
	#print("in prodInts")
	product = int1 * int2

	return product




###############################################################################
# printInts
# prints the passed in arguments to the console
###############################################################################
def printInts(int1, int2, int3):
	#print ("in printInt")
	print(int1)
	print(int2)
	print(int3)




###############################################################################
# main
# controls the basic flow of program
# creates random strings, saves them to files
# prints the strings
# creates random ints and multiplies them
# prints the random ints and their product
###############################################################################
def main():	
	#print ("in main")
	stringArr = makeStrings();
	#print (stringArr)
	saveStrings(stringArr);
	printStrings(stringArr);
	int1, int2 = genInts();
	int3 = prodInts(int1, int2);
	printInts(int1, int2, int3);




###############################################################################
# calls main
###############################################################################
if __name__ == "__main__":
	main()








