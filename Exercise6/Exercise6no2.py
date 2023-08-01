# Exercise 6
# No 2

import string
import re
import csv

fIn = open("EV.csv", "r+")

fOut = open("output.csv","w+")

csvreader = csv.reader(fIn)



for row in fIn:
    terms = row.split(',')
    # extract the value of identification number
    match_geneid = re.findall(r'.+', terms[1], re.I)

    # if match
    if match_geneid:
        # extract the value
        id_no = match_geneid
        print(id_no)
        fOut.writelines(id_no)
        fOut.write(",")

    # extract the value of tissue name
    match_tissue = re.findall(r'.+', terms[7], re.I)
    if match_tissue:
        # extract the value
        tissue = match_tissue
        print(tissue)
        fOut.writelines(tissue)
        fOut.write(",")

    # extract the value of the expression value
    match_ev = re.findall(r'.+', terms[8],re.I)
    if match_ev:
        # extract the value
        ev = match_ev
        print(ev)
        fOut.writelines(ev)
        fOut.write("\n")

fOut.close()