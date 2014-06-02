# fastq_2_fasta.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Converts fastq to fasta
# python fastq_2_fasta.py filename.fastq > filename.fasta

# import modules
import sys

# Get input file
try:
  infile = open(sys.argv[1])

# If no input file print help
except:
  print("\nfastq_2_fasta.py converts fastq to fasta\n"
        "\nUse as follows:\npython fastq_2_fasta.py filename.fastq > filename.fasta\n")
  sys.exit()

# Iterate through each line of the .fastq file
counter = 0
for lines in infile:
    # Add header
    if counter % 4 == 0:
        print(">" + lines[1:].replace("\n",""))
    # Add sequence
    elif (counter - 1) % 4 == 0:
        print(lines.replace("\n",""))
    counter += 1

# Close .fastq file
infile.close()
