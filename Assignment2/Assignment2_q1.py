# SIV3004 Assignment 2
# Question 1
# Chairunnisa Nur Amanda -S2014538

'''
PSEUDOCODE
- Prompt user to input the file
- Open the file
- Readlines and stored it into a variable
- See file extension
- If file end with.embl it is a GCG format
    For line in lines
      Extract the pattern using RE
	If object found
	 put it into a single line
- Elif it end with .embl it is a EMBL format
    For line in lines
     Extract the pattern using RE
      If object found
	put it into a single line
- Print in single line
- Calculate and print the length of the sequence

'''

# import regular expression module
import re

# Prompt user to enter the file name
print("Enter the input file name:")
input_file = input()

# open the input file
file_open = open(input_file, "r")

lines = file_open.readlines()

# create a variable to store the sequences in a single line
single_seq = ""

# Recognise the file type and perform appropriate action
# if the file is .gcg 
if re.search(r"(.gcg)", input_file, re.I): # use re.search for.gcg in the file name
    print("\nThe sequence file is in GCG flat file format.")

    for line in lines: # read the file per lines
    
        ## pattern to match the sequence
        line = line.strip()
        # the match object in line is stored into variable m
        m = re.match(r"\d+\s+(.+)", line)

        #IF matched object found, it returns TRUE
        if m:

            # extract on the sequence part only using group(1)
            seq_line = m.group(1)

            # remove spaces and substitute it with empty string
            seq_line = re.sub(r" ","", seq_line)

            # concate all sequence parts into a single sequence line
            single_seq += seq_line


# if the file is .embl     
elif re.search(r"(.embl)", input_file, re.I): # use re.search for.embl in the file name
    print("\nThe sequence file is in EMBL flat file format.")
       
    for line in lines: # read the file per lines
        
        ## pattern to match the sequence
        m = re.match(r"\s+([a-zA-Z\s]+)\d+", line)

        #IF matched object found, it returns TRUE
        if m:

            # extract on the sequence part only using group(1)
            seq_line = m.group(1)

            # remove spaces and substitute it with empty string
            seq_line = re.sub(r" ","", seq_line)

            # concate all sequence parts into a single sequence line
            single_seq += seq_line

# output
print("\nSequence in a single line:")
print(single_seq)
# print sequence length, calculate using len()
print("\nSequence length: ", len(single_seq)) 

