import csv 
import os

FILENAME = "ecoli_annotations.tsv"

input = open(FILENAME)
tsv_file = csv.reader(input, delimiter="\t")

unique_genes = []
operons = []

operon_name = ""
operon_count = 0

max_count = 0
max_operon = ""

for row in tsv_file:
    locus = row[6][:3]
    if locus not in unique_genes:
        unique_genes.append(locus)
    elif locus not in operons:
        operons.append(locus)

input = open(FILENAME)
tsv_file = csv.reader(input, delimiter="\t")

loci = []

for row in tsv_file:
    locus = row[6][:3]
    loci.append(locus)

max_operon = ""
max_count = 0

for operon in operons:
    if(loci.count(operon) > max_count):
        max_count = loci.count(operon)
        max_operon = operon

print(max_operon + ":" + str(max_count))

#print(max_count)
#print(max_operon)

input.close()