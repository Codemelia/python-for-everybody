# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours the user inputs
# Do not worry about error checking the user input - assume the user types numbers properly.

# take input hours/rate from user
hrs = input("Enter hours:")
rate = input("Enter rate:")

# convert string inputs to float values
h = float(hrs)
r = float(rate)

# compute total pay and print
print("Pay:", h * r)