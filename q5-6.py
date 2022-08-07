from collections import abc
import csv 
import os
import numpy as np
import re

FILENAME = "protein_test.tsv"

input = open(FILENAME)
tsv_file = csv.reader(input, delimiter="\t")

raw_proteins = []
proteins = []

for row in tsv_file:
    raw_proteins.append(row[0])

for word in raw_proteins:
    for x in word.replace('-',' ').split():
        if("ase" in x):
            x="".join(c for c in x if c.isalpha())
            proteins.append(x[:(x.find("ase")+3)])

proteins.sort()

protein_name = proteins[0]
protein_count = 0
output = []

for x in proteins:
    if protein_name == x:
        protein_count += 1
    else:
        output.append([protein_name, protein_count])
        protein_name = x
        protein_count = 1

for x in output:
    print(x)

with open('q5-6.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(["Protein Name", "Protein Count"])

    # write multiple rows
    writer.writerows(output)

print(len(proteins))
print(len(raw_proteins))
