# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

try:
    # take user input and open file for reading
    fname = input("Enter file name: ")
    fh = open(fname)

    # create empty list to store words from file
    lst = list()

    # loop through fh
    for line in fh:
        line = line.rstrip()
        curr_lst = line.split() # remove newlines and split into list

        # loop through list of words in curr line
        for word in curr_lst:
            if word not in lst : lst.append(word) # append to lst if not already in it

    lst.sort() # sort lst
    print(lst) # print sorted lst
    
# error handling
except:
    print("Something went wrong! Ensure your file is valid.")