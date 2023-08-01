# Assignment 2
# Question 2
# Chairunnisa Nur Amanda - S2014538

'''
- Open the input file to read
- Create an output file to write
- Read the file line by line and create a list to store each lines in the file
-   For line in lines:
	Extract the value of identification number
	Extract the value of organism name
	Extract the sequence
            Concate all the sequene parts into a single line
- Format the header and the sequence to have 120 characters per line and write the value into the output file
- Close the output file

'''

import re

# global variable
id_no = ""
organism_name = ""
sequence = ""

# open file named seq.embl and assigned into a variable named input_file
input_file = open("seq.embl", "r+")

# prepare the name of the output file and assigned into a variable named output_file
output_file = open("embl2fasta.fa", "w")

# read all lines in the input file
lines = input_file.readlines()

# loop to read each items in lines
for line in lines:

    # extract the value of identification number
    match_id = re.match(r'ID\s+([A-Z0-9]+)', line, re.I)

    # if match
    if match_id:
        # extract the value from group 1
        id_no = match_id.group(1)

    # extract the value of organism name
    match_name = re.match(r'OS\s+([a-zA-Z\s]+)', line, re.I)

    # if match
    if match_name:
        organism_name = match_name.group(1)

    # extract the sequence
    match_seq = re.match(r'\s+([a-zA-Z\s]+)\d+', line)
    
    #IF matched object found, it returns TRUE
    if match_seq:

        # extract on the sequence part only using group(1)
        seq_line = match_seq.group(1)

        # remove spaces and substitute it with empty string
        seq_line = re.sub(r" ","", seq_line)

        # concate all sequence parts into a single sequence line
        sequence += seq_line


# print and format the extracted values into a Fasta file format

# if sequence returns a value
if sequence:
    split_sequence = [] # to temporary stored the splitted sequence
    sequence_length = len(sequence)
    char_per_line = 120 # number of characters per line in sequence

    # split a single line of sequence into multiple lines, 120 characters per line
    for i in range(0, sequence_length, char_per_line):
        split_sequence.append(sequence[i:i+char_per_line])

    # formatting the header of the fasta file
    header = ">" + id_no.strip() + "\t" + organism_name.strip() + "\t" + str(sequence_length) + " bp"
    print(header)
    output_file.write(header + "\n") # write the header into the output file

    # sequence 120 characters per line
    for line in split_sequence:
        print(line)
        output_file.write(line.upper() + "\n") # write the sequence into the output file
    output_file.close()
    

