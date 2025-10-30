# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
try:
    # take file name input and open for reading
    fname = input("Enter file name: ")
    fh = open(fname)

    # initialise count and sum variables
    count, total = 0, 0

    # loop through fh
    for line in fh:
        line = line.rstrip() # strip newlines
        
        if not line.startswith("X-DSPAM-Confidence:"):
            continue # skip if line does not meet criteria

        # extract float values from lines that meet criteria
        fl = float(line[line.find('.') - 1:])

        # count and sum up lines that meet criteria    
        count += 1
        total += fl

    # print average which is total / count
    print("Average spam confidence:", total / count)
except:
    print("Something went wrong! Ensure you have the correct file.")