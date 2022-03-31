'''
# Python3 code to demonstrate
# yield keyword

# generator to print even numbers
def print_even(test_list) :
	for i in test_list:
		if i % 2 == 0:
			yield i

# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print ("The original list is : " + str(test_list))

# printing even numbers
print ("The even numbers in list are : ", end = " ")
for j in print_even(test_list):
	print (j, end = " ")






# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
	i = 1

	# An Infinite loop to generate squares
	while True:
		yield i*i				
		i += 1 # Next execution resumes
				# from this point	

# Driver code
for num in nextSquare():
	if num > 100:
		break
	print(num)
'''




# Python3 code to demonstrate yield keyword

# Checking number of occurrence of
# geeks in string

# generator to print even numbers
def print_even(test_string) :
	for i in test_string:
		if i == "geeks":
			yield i

# initializing string
test_string = " The are many geeks around you, \
			geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0
print ("The number of geeks in string is : ", end = "" )
test_string = test_string.split()

for j in print_even(test_string):
	count = count + 1

print (count)
