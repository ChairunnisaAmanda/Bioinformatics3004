# Assignment 2
Question 1:
There are two sequence files in different formats as stated below:- 
1. seq.embl
2. seq.gcg

Write a script that performs the followings:
1) Ask user to enter the input file name (using the above files)
2) Once user entered the file name, the system will recognize the input file and display a messageas the followings:
  a. “The sequence file is in EMBL flat file format.” or b. “The sequence file is in GCG flat file format.”
3) Extract the sequence lines and print out it in a single line sequence 4) Calculate and print out the length of each sequence

Question 2:

Convert a sequence from EMBL file format (“seq.embl”) into a FASTA file format and store it into an external file with named ‘’embl2fasta.fa”.
The output file should be in the following format: 

• Header line with the identification no., scientific name of the organism and length of the sequence in bp unit. Each value is separated by the tab format

• Each line of the sequence is in 120 bp

Question 3:

Convert a sequence from GCG file format (“seq.gcg”) into a GENBANK file format and store it into an external file with named ‘’gcg2gb.genbank”.

The output file should be in the following format: 

• Information on the locus, source with the organism name, base count and origin for the sequence.

• The KEYWORDS and VALUES are separated by relevant white space

• Each line of the sequence is in 60 bp with the cut-off of 10 characters and separated by a white space

• Characters of the sequence are in upper case
