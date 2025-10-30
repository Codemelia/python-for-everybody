# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# takes in file name as input
# default input is mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
# open the file for reading    
handle = open(name)

# initialise a dict to store hour and count
count_map = {}

# loop through lines in file
for line in handle:
    
    # strip newlines
    line = line.rstrip()
    
    # if line starts with 'From '
    if line.startswith('From '):
        hour = line.split()[5][:2] # retrieve hour
        count_map[hour] = count_map.get(hour, 0) + 1 # update dict
        
# retrieve list of tuples from dict and sort
tuple_list = list(count_map.items())
tuple_list.sort()

# loop through list and print
for t, c in tuple_list:
    print(t, c)