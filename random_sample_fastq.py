# random_sample_fastq.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Randomly samples fastqs from a file of multiple fastqs
# Use as follows:
# python random_sample_fastq.py filename.fastq <sample number integer> > random.fastq

# import modules
import sys
import random

# Get input file and sample number
try:
    fastq_file = open(sys.argv[1])
    sample_number = int(sys.argv[2])

# If no input file or sample number, print help
except:
    print("\nrandom_sample_fastq.py randomly samples fastqs from a file of multiple fastqs.\n"
          "\nUse as follows: \npython random_sample_fastq.py filename.fastq <sample number integer> > random.fastq")
    print("\nE.g\npython random_sample_fastq.py filename.fastq 10000 > random.fastq\n")
    sys.exit()


# Read fastq file lines into list and close file
line_list = fastq_file.readlines()
fastq_file.close()

# Place very 4 lines (each fastq) as it's own element in fastq list
counter = 0
fastq_list = []
while counter < len(line_list):
    fastq_list.append(line_list[counter:counter+4])
    counter+=4

# Randomly sample fastq list
random_sample = random.sample(fastq_list, sample_number)

# Add every element in the list to a string
random_fastq_out = "" 
for x in random_sample:
    for y in x:
        random_fastq_out += y

# Remove EOL from last line and print
if random_fastq_out[-1:] == "\n":
    random_fastq_out = random_fastq_out[:-1] 

print(random_fastq_out)
