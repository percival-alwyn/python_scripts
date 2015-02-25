# random_tag_rmdup.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Removes duplicate reads from single end reads with random tags
# Takes two .fastq files:
#   1) Read_1.fastq
#   2) Random_tag.fastq
# Use random_tag_rmdup.py as follows to remove duplicates using random tags:
# python random_tag_rmdup.py Read_1.fastq Random_tag.fastq Read_1_rmdup_output.fastq duplicate_frequency_output.txt r
# Use random_tag_rmdup.py as follows to remove duplicates without using random tags:
# python random_tag_rmdup.py Read_1.fastq Random_tag.fastq Read_1_rmdup_output.fastq duplicate_frequency_output.txt

# import modules
import itertools
import sys

# Get input files
try:
    read_1_file = open(sys.argv[1])
    random_tag_file = open(sys.argv[2])
    read_1_rmdup_output = open(sys.argv[3], "w")
    duplicate_frequency_output = open(sys.argv[4], "w")

# If no input files print help
except:
  print("\nrandom_tag_rmdup.py removes duplicate reads from single end reads with random tags.\n"
        "\nTakes two .fastq files:\n1) Read_1.fastq\n2) Random_tag.fastq\n"
        "\nUse as follows to remove duplicates using random tags:"
        "\npython random_tag_rmdup.py Read_1.fastq Random_tag.fastq Read_1_rmdup_output.fastq duplicate_frequency_output.txt r\n"
        "\nUse as follows to remove duplicates without using random tags:"
        "\npython random_tag_rmdup.py Read_1.fastq Random_tag.fastq Read_1_rmdup_output.fastq duplicate_frequency_output.txt\n\n")
  sys.exit()

# set R to "R" to remove duplicates using random tags or set R to "Not R" to remove duplicates without using random tags
try:
    R = sys.argv[5].upper()
except:
    R = "Not R"

# Set up a dictionary of seen reads and set up a dictionary of read frequencies
seen_dict = {}
duplicate_frequency_dict = {}

# Set up a string to contain each fastq and a line counter
each_fq = ""
line_counter = 0
seen = False

# Zip files together and iterate through both at the same time
for each_R1_fq_line, each_random_fq_line in itertools.izip(read_1_file, random_tag_file):
    # if sequence line
    if (line_counter -1) % 4 == 0:
        # if using random tags cat random tag to sequence
        if R == "R":
            combined = each_R1_fq_line.replace("\n","") + each_random_fq_line.replace("\n","")
        # if not using random tags do not combine with sequence
        else:
            combined = each_R1_fq_line.replace("\n","")
        # If not in seen dictionary then add and set seen to False and add to fastq string
        if combined not in seen_dict:
            seen_dict[combined] = 1
            seen = False
            each_fq += each_R1_fq_line
        # If in seen dictionary then set seen to True and add to duplicate frequency table
        elif combined in seen_dict:
            seen = True
            spaced = each_R1_fq_line.replace("\n","") + " " + each_random_fq_line.replace("\n","")
            if spaced not in duplicate_frequency_dict:
                duplicate_frequency_dict[spaced] = 1
            else:
                duplicate_frequency_dict[spaced] +=1
    # if last line in fastq
    elif (line_counter -3) % 4 == 0:
        # if sequence and tag is a duplicate reset fastq to blank
        if seen == True:
            each_fq = ""
        # if sequence and tag is unique write to read 1 output file
        else:
            each_fq += each_R1_fq_line
            read_1_rmdup_output.write(each_fq)
            each_fq = ""
    # All other lines
    else:
        each_fq += each_R1_fq_line
    
    line_counter +=1

# sort frequency dictionary by alphabetical order 
for x in sorted(duplicate_frequency_dict.keys()):
    # write write to duplicate frequency file
    duplicate_frequency_output.write(x + " " + str(duplicate_frequency_dict[x]) + "\n")

# Close all files
read_1_file.close()
random_tag_file.close()
read_1_rmdup_output.close()
duplicate_frequency_output.close()
