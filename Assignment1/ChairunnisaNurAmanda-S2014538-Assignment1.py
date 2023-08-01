# SIV3004 Assignment 1
# Chairunnisa Nur Amanda - S2014538

'''
Pseudocode
- prompt user to input the file name
- open the file to read
- make a dictionary with header and sequence
- if the line start with >, it is a header (key)
- else (sequences), is a value
- remove the whitespace character so the sequence is displayed in one line
- repeat for next sequence
- put all the value (sequence) into a list
- count sequence length using len
- display the result

'''

# Prompt user to enter the file name
input_file = input("Enter the input file name: ")
# open the input file
file_txt = open(input_file, "r")

# insert the header and sequence to a dictionary
sequences = {}
for line in file_txt: #read line by line
    if line[0] == ">": # put header as a key
        header = line.strip()
    else: # put the line except the header as a value
        if header not in sequences:
            sequences[header] = "" # define that the value is a string
        sequences[header] += line.strip() # remove the whitespace character

# convert the value in sequences dictionary into a list
sequence_list = list(sequences.values())

# print the sequences and the length
print("The sequences:")
for seq in sequence_list:
    # print the sequence in one line
    print(seq)
    # count the sequence length using len
    print("Sequence length:", len(seq), "\n")

