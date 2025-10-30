# 8.5 Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.

try:
    # take user input
    fname = input("Enter file name: ")

    # defaults file to mbox-short.txt if no filename given
    if len(fname) < 1:
        fname = "mbox-short.txt"

    # opens file for reading
    fh = open(fname)

    # count to sum up lines starting with From
    count = 0

    # loop through fh
    for line in fh:
        if not line.startswith("From:") : continue # skip iteration if line does not start with From:

        count += 1 # update count if line starts with From:

        line = line.rstrip() # remove newlines
        curr_lst = line.split() # split line string into list

        email = curr_lst[1] # extract second word in list
        print(email) # print every email address

    print("There were", count, "lines in the file with From as the first word")

# error handling
except:
    print("Something went wrong! Ensure your file is valid.")