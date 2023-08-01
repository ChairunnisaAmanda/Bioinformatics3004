# Exercise 6
# No 1

import string
import re

loc = ""
defi = ""
acc = ""
ver = ""
seq = []

fIn = open("bioinfoData/1_simpleFormat_Fasta.txt", "r+")

fOut = open("outGenbank.gb","w+")

lines = fIn.readlines()

for line in lines:
    line = line.strip() # to remove spaces at the beginning and at the end of the string

    head = re.match(r'>(.*)', line, re.IGNORECASE)

    
    if head:
        headerLine = head.group(1)
        terms = headerLine.split('|') # terms is in list data type, has 5 elements
        match3 = re.match (r'(.+)\..+', terms[3], re.I)
        if match3:
            accObj = match3.group(1) 
            acc = 'ACCESSION    ' + accObj

        match4 = re.match(r'(\w+)\s+(.+)', terms[4], re.I) 
        if match4:
            locObj = match4.group(1) 
            defObj = match4.group(2) 

            loc ='LOCUS        ' + locObj
            defi = 'DEFINITION   ' + defObj

        ver = 'VERSION      '+terms [3] +' '+ terms[0].upper() + ':'+ terms[1]

    else:
        seq.append(line.strip())

if seq: 
    print(loc + '\n' + defi + '\n'+ acc + '\n' + ver)
    fOut.write(loc + '\n' + defi + '\n' + acc + '\n' + ver)

    seqLine = ''.join (seq)
    split_sequence = []
    sequence_length = len(seqLine)
    base_per_line = 60 # number of bases per line in sequence

    # split a single line into multiple lines, each consists of 60 bases
    for i in range(0, sequence_length, base_per_line):
        split_sequence.append(seqLine[i:i+base_per_line])
    

    a=seqLine.count('A')
    c=seqLine.count('C')
    g=seqLine.count('G')
    t=seqLine.count('T')
    print('BASE COUNT   ' + str (a) + 'a\t' + str(c) + 'c\t' + str(g) + 'g\t' + str(t) +' t')
    fOut.write('BASE COUNT  '+ str (a) +' a\t' + str(c)+'c\t' + str(g) + 'g\t' + str(t) + 't' +' \n')

    print( 'ORIGIN   '); fOut.write('ORIGIN ' + '\n')

    cnt = 0
    for i in split_sequence: 
        tempSubseq = []
        cutoff = 10
        for subseq in range (0, len (i), cutoff):
            tempSubseq.append(i[subseq:subseq+cutoff])

        subSeqs= ' '.join(tempSubseq) 
        num = "%10d"%(1+cnt)
        lineSeq = num + ' ' + subSeqs
        print(lineSeq); fOut.write(lineSeq + '\n')
        cnt = cnt + len(i)
    print('//'); fOut.write('//')
