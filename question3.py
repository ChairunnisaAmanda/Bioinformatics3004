# Assignment 2
# Question 3
# Chairunnisa Nur Amanda - S2014538

'''
PSEUDOCODE
- Open the input file to read
- Create an output file to write
- Declare the global variable
- Create a list to store each lines in the file
- For every line
    Extract the locus information
    Extract the name of the organism
    Extract the sequence
- Count each bases on the sequence
- Format the output file

'''


import re
import string

# declare global variable to store each value
locus = ""
organism_name = ""
sequence = ""

# open file named seq.gcg and assigned into a variable named input_file
input_file = open("seq.gcg", "r+")

# prepare the name of the output file and assigned into a variable named output_file
output_file = open("gcg2gb.genbank","w+")

# read all lines in the input file
lines = input_file.readlines()

# loop to read each items in lines
for line in lines:
    line = line.strip() # remove spaces at the beginning and at the end of the line

    # extract the locus information
    match_loc = re.match(r'[A-Z]+', line)
    
    # if match
    if match_loc:
        locus_obj = match_loc.group(0)
        # extract the value and write the format
        locus = "LOCUS       " + locus_obj

    # extract the organism name
    match_name = re.match(r'[a-z]+\.[a-z]+', line, re.I)

    # if match
    if match_name:
        name_obj = match_name.group(0)
        # extract the value and write the format
        organism_name = "  ORGANISM  " + name_obj
        
    # extract the sequence
    match_seq = re.match(r"\d+\s+(.+)", line)

    # if matched
    if match_seq:
            # extract on the sequence part only using group(1)
            seq_line = match_seq.group(1)

            # remove spaces and substitute it with empty string
            seq_line = re.sub(r" ","", seq_line)

            # concate all sequence parts into a single sequence line
            sequence += seq_line
            

# if sequence returns a value
if sequence:
    split_sequence = [] # to temporary stored the splitted sequence
    sequence_length = len(sequence)
    base_per_line = 60 # number of bases per line in sequence

    # split a single line into multiple lines, each consists of 60 bases
    for i in range(0, sequence_length, base_per_line):
        split_sequence.append(sequence[i:i+base_per_line])

    # formatting the information in the genbank file 
    print(locus + "\t" + str(sequence_length) + " bp\t" + "DNA\n")
    output_file.write(locus + "\t" + str(sequence_length) + " bp\t" + "DNA\n")
    
    print("SOURCE\n")
    output_file.write("SOURCE\n")
    
    print(organism_name + "\n")
    output_file.write(organism_name + "\n")

    
    # count the bases
    a = sequence.count('a')
    c = sequence.count('c')
    t = sequence.count('t')
    g = sequence.count('g')

    # formatting the output in the genbank file
    print("BASE COUNT   " + str(a) + " a\t" + str(c) + " c\t" + str(g) + " g\t" + str(t) + " t")
    output_file.write("BASE COUNT   " + str(a) + " a\t" + str(c) + " c\t" + str(g) + " g\t" + str(t) + " t\n")

    print("ORIGIN\n")
    output_file.write("ORIGIN\n" )
    
    # split the sequence with the cut-off of 10 characters and separated by a white space
    count = 0
    for line in split_sequence: 
        sub_sequence = []
        cut_off = 10
        for subseq in range (0, len(line), cut_off):
            sub_sequence.append(line[subseq:subseq+cut_off])

        sub_seq_string= ' '.join(sub_sequence)
        # put the number in front of each line of the sequence
        number = "%10d"%(1+count)
        sequence_line = number + ' ' + sub_seq_string.upper()

        # write the sequence line into the output file
        print(sequence_line)
        output_file.write(sequence_line + '\n')
        count = count + len(line)
        
    print('//')
    output_file.write('//')

    # close the file
    output_file.close()
