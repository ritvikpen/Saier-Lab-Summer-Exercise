from collections import abc
import csv 
import os
import numpy as np

FILENAME = "ecoli_annotations.tsv"

input = open(FILENAME)
tsv_file = csv.reader(input, delimiter="\t")

raw_proteins = []
proteins = []

for row in tsv_file:
    protein_name = row[11]
    strand = row[4]
    if "ase" in protein_name:
        for word in protein_name.split(" "):
            if ("ase" in word):
                raw_proteins.append(word)
                proteins = list(set(raw_proteins))

print(len(proteins))
print(len(raw_proteins))

for word in proteins:
    print(word)
