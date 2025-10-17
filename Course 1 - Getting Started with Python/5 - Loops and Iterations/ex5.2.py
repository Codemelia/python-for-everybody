# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

# initialise largest and smallest
largest = float('-inf')
smallest = float('inf')

# while loop
while True:
    
    # take input from user
    num = input("Enter a number: ")
    
    # if user input is done, exit loop and print final statements
    if num == "done":
        break
        
    # try/except block    
    try:
        n = int(num) # goes to except if unsuccessful (ie. input is invalid number)
        
        # assign largest/smallest by respective conditions
        if n > largest:
            largest = n
        elif n < smallest:
            smallest = n
    except:
        print("Invalid input") # graceful handling of exception
        continue # continue to next iteration of loop
    
# print max and min numbers
print("Maximum is", largest)
print("Minimum is", smallest)