# Test 2 - SIV3004
# Chairunnisa Nur Amanda - S2014538

'''
Pseudocode
- get the input file name from the user
- define the function to extract LOCUS, Accession, and the sequence from genbank file
    - use regular expression to extract the information
    - use another function to display the information in FASTA format
- define the function to extract ID, AC, and the sequence from swissprot file
    - create a list to store the information for each sequences
    - split the file to process each entry
    - use regular expression to extract the information
    - use another function to display the information in FASTA format
- define the function to format the genbank output in a FASTA format
    - format the header and print
    - split the sequence using a function
    - print the line for the sequence
- define the function to format the swissprot output in a FASTA format
    - for every item in each lists
    - format the header and print
    - split the sequence using a function
    - print the line for the sequence
- define the function to split the sequence into 100 characters per line
    - for every 100 characters of the sequence
        - append it into a list
    - print the list
- open the file and read line by line
    - using regular expression check if the file start with "LOCUS" it is a genbank file
    - using regular expression check if the file start with "ID" it is a swissprot file
    - process the file using respective function to get the output

'''

import re

def main():
    # Prompt user to enter the file name
    filename = input("Enter the input file name: ")

    # open the input file
    input_file = open(filename, "r")
    line = input_file.readline()

    
    if re.match(r"^LOCUS", line, re.I): # use re.match to find "LOCUS" in the first line
        print("\nThe sequence file is in GENBANK file format.\n")
        output = readGB(filename) # process the file using defined function for genbank

    if re.match(r"^ID", line, re.I): # use re.match to find "ID" in the first line
        print("\nThe sequence file is in SWISSPROT file format.\n")
        output = readSP(filename) # process the file using defined function for swissprot

    return output # display the output


def readGB(filename): # function for reading the genbank file and extract the information
    input_file = open(filename, "r")

    sequence = "" # create a string to store the sequence
    lines = input_file.readlines() # to read the file line by line

    for line in lines:
        line = line.strip() # to remove spaces at the beginning and at the end of the string

        # use re.match to extract the value of LOCUS    
        matchLocus = re.match(r'LOCUS\s+(.+)', line, re.IGNORECASE) 
                #IF match
        if matchLocus:
            # extract the value from group(1) and assign it into a variable named locus
            locus = matchLocus.group(1) 

        # use re.match to extract the value of accession
        matchAccession = re.match(r'ACCESSION\s+(.+)', line, re.IGNORECASE) 
                #IF match
        if matchAccession:
            # extract the value from group(1) and assign it into a variable named acc
            acc = matchAccession.group(1) 


        # use re.match to extract sequence lines
        matchSeq = re.match(r"\d+\s+(.+)", line) 
            #IF match
        if matchSeq:
            # extract the value from group(1) and assign it into a variable named seqline
            seqline= matchSeq.group(1) 
            seqline = re.sub(r" ","", seqline) # to remove ' ' and replace with ' ' using re.sub function
            sequence += seqline # concatenate seqline to sequence
    fasta = GBtoFasta(sequence, locus, acc) #call the function to display the output in fasta format
    return fasta 

def GBtoFasta(sequence, locus, acc): # function to format the output in fasta
    header = ">" + locus + "\t" + " | " + acc # format the header
    print(header)
    
    # call the function to split the sequence in 100 characters per line
    for line in seq_split(sequence,100): 
        print(line)

def readSP(filename): # function for reading the swissprot file and extract the information
    input_file = open(filename, "r+")
    files = input_file.read() # read the input file

    # create a list to store the value of id, ac, and the sequence of each entry
    idlist = []
    aclist = []
    seqlist = []
    
    files = re.split(r'//',files) # split the file to each entry
    for file in files:
        file = re.split(r'\n', file) # split the file into list per lines
        sequence = [] # create a list to store the value of sequence of an entry

        for line in file:

            # use re.match to extract the value of ID
            matchID = re.match(r'ID(.+)\.', line, re.IGNORECASE) 
            #IF match
            if matchID:
                # extract the value from group(1) and assign it into a variable named id
                id = matchID.group(1) 
                idlist.append(id) # append id into idlist

            # use re.match to extract the value of AC
            matchAC = re.match(r'AC(.+)\;', line, re.IGNORECASE)
            #IF match
            if matchAC:
                # extract the value from group(1) and assign it into a variable named ac
                ac = matchAC.group(1) 
                aclist.append(ac) # append id into aclist

            # use re.match to extract the sequence
            matchSeq = re.match(r"\s+(.+)", line)
            #IF match
            if matchSeq:
                # extract the value from group(1) and assign it into a variable named seqline
                seqline= matchSeq.group(1) 
                seqline = re.sub(r" ","", seqline) # to remove ' ' and replace with ' ' using re.sub function
                sequence.append(seqline) # append seqline into sequence
                
        sequencejoin = ""
        sequencejoin = sequencejoin.join(sequence) # join the sequence for each entry into a string
        seqlist.append(sequencejoin) # append sequencejoin into seqlist

    fasta = SPtoFasta(idlist,aclist, seqlist) #call the function to display the output in FASTA
    return fasta


def SPtoFasta(idlist, aclist, seqlist): # function to format the output in fasta
    
    for i in range(len(idlist)): # for each item in the list
        header = ">" + (idlist[i]).strip() + "|" + aclist[i] # format the header
        print(header)
        sequence = seq_split(seqlist[i],100) # split the sequence into 100 characters per line
        for line in sequence:
            print(line)
        print("\n")

def seq_split(sequence,char_per_line): # function to split the sequence into n characters per line
    split_sequence = [] # list to store n characters per item
    sequence_length = len(sequence)
    # split a single line of sequence into multiple lines, n characters per line
    for i in range(0, sequence_length, char_per_line):
        split_sequence.append(sequence[i:i+char_per_line]) # append n characters into the list
    return split_sequence
 
main()
