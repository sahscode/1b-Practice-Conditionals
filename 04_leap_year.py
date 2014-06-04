# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.
# Write a Python function is_leap_year that take as 
# input the parameter year and returns True if year 
# (an integer) is a leap year according to the Gregorian 
# calendar and False otherwise. The Wikipedia entry for 
# leap years contains a simple algorithmic rule for determining 
# whether a year is a leap year. Your main task will be to 
# translate this rule into Python.

###################################################
# Tests
# Student should not change this code.

def test(year):
	"""Tests the is_leapyear function."""
	if is_leap_year(year):
		print year, "is a leap year."
	else:
		print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
