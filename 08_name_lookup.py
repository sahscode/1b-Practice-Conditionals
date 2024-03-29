# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.
# Write a Python function name_lookup that takes a 
# string first_name that corresponds to one of 
# ("Joe", "Scott", "John" or "Stephen") and then returns 
# their corresponding last name ("Warren", "Rixner", "Greiner" or "Wong"). 
# If first_name doesn't match any of those strings, 
# return the string "Error: Not an instructor".


###################################################
# Tests
# Student should not change this code.

def test(first_name):
	"""Tests the name_lookup function."""
	
	print name_lookup(first_name)
	
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor
