# fast_size_dist.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Creates size/frequency distribution table from the fasta or fastq

# Can be used to determine the size distribution of scaffolds and contig files (fasta)
# or can be used to calculate library size distribution or sequence length distribution from PacBio fastq files

# python fast_size_dist.py -fasta/-fastq yourfile.fasta/yourfile.fastq > yoursizedist.csv

# E.g python fast_size_dist.py -fasta yourfile.fasta > yoursizedist.csv

# import modules
import sys

# Get input file, file format and outfile name
try:
    filetype = sys.argv[1]
    if filetype == "-fasta":
        every = 2
    if filetype == "-fastq":
        every = 4

    infile = open(sys.argv[2])

# If no input print help
except:
  print("\nfast_size_dist.py creates size/frequency distribution table from the fasta or fastq\n"
        "\nUse as follows: \npython fast_size_dist.py -fasta yourfile.fasta > yoursizedist.csv")
  print("or\npython fast_size_dist.py -fastq yourfile.fastq > yoursizedist.csv\n")
  sys.exit()

# Iterate through each line of fast file and add length of sequence to list 
list_of_sizes = []

counter = 0
for line in infile:
    # Only look at sequence lines
    if (counter -1) % every == 0:
        list_of_sizes.append(len(line.replace("\n","")))
    else:
        pass
    counter += 1

# Iterate through size list and add new sizes (key) to an array with freq (value) of one
# If size already in array add one to freq (value)
distribution_dictionary = {}
for x in list_of_sizes:
    if x not in distribution_dictionary:
        distribution_dictionary[x] = 1
    else:
        distribution_dictionary[x] += 1

# Iterate through two dimensional array (dictionary) adding size (key) then freq (value) to csv format
distribution_csv_format = "Length (bp),Frequency\n"
for dist in distribution_dictionary:
    distribution_csv_format += str(dist) + "," + str(distribution_dictionary[dist])+ "\n"

print distribution_csv_format
