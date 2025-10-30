# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# takes in file name as input
# default input is mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
# open the file for reading    
handle = open(name)

# dictionary to map email address to count
count_map = {}

# loop through lines in file
for line in handle:
    
    # remove newlines
    line = line.rstrip()
    
    # if line starts with 'From '
    if line.startswith('From '):
        sender = line.split()[1] # retrieve email address
        count_map[sender] = count_map.get(sender, 0) + 1 # update count in dict
        
# store max count
max_count = 0

# store sender with max count
max_sender = ''

# loop through dict
for k in count_map:
    
    # retrieve curr count
    curr_count = count_map[k]
    
    # if count is larger than max count
    if curr_count > max_count:
        max_count = curr_count # update max count
        max_sender = k # update max sender
        
# print output
print(max_sender, max_count)