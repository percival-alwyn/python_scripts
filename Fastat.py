# Fastat.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Prints to screen basic statistics about .fasta files

# python Fastat.py yourfile.fa > Basic_stats.txt

# import modules
import sys

# input file
try:
    infile = open(sys.argv[1])
except:
    # If no input file print help
    print("\nFastat.py prints to screen basic statistics about .fasta files\n")
    print("Use as follows:\npython Fastat.py yourfile.fa > Basic_stats.txt\n")
    sys.exit()

# Make list of all lines in file 
all_lines = infile.readlines()

# Close .fa file
infile.close()

all_nucleotides = ""
seq_lens_list = []
longest = False
shortest = False
counter = 0

# Iterate through each line of .fa list 
for line in all_lines:
    # Only look at sequence lines
    if (counter - 1) %2 == 0:
        # Make sure no windows EOL are present
        if "\r" in line:
            print("Windows EOL present! Run EOL conversion.")
            sys.exit()
        # Add concatenate sequences
        all_nucleotides += line.replace("\n","")
        # Add sequnce lengths
        seq_lens_list.append(len(line.replace("\n","")))
        # Add longest sequence header and length to list
        if longest == False:
            longest = [all_lines[counter-1].replace("\n",""),len(line.replace("\n",""))]
        else:
            if len(line.replace("\n","")) > longest[1]:
                longest = [all_lines[counter-1].replace("\n",""),len(line.replace("\n",""))]
        # Add shortest sequence header and length to list
        if shortest == False:
            shortest = [all_lines[counter-1].replace("\n",""),len(line.replace("\n",""))]
        else:
            if len(line.replace("\n","")) < shortest[1]:
                shortest = [all_lines[counter-1].replace("\n",""),len(line.replace("\n",""))]
    # Count all lines present
    counter += 1

# Print stats to screen
print("Total number of sequences = " + str(counter/2))
print("Total nucleotides = " + str(len(all_nucleotides)))
unambig = (all_nucleotides.upper().count("A") + all_nucleotides.upper().count("C") +
           all_nucleotides.upper().count("G") + all_nucleotides.upper().count("T"))
print("Total unambiguous nucleotides (TGAC) = " + str(unambig))
print("Percentage GC (Total) = " + str(((all_nucleotides.upper().count("C") + all_nucleotides.upper().count("G")) /
                                float(len(all_nucleotides))) * 100))
print("Percentage GC (Unambiguous) = " + str(((all_nucleotides.upper().count("C") + all_nucleotides.upper().count("G")) /
                                float(unambig)) * 100))
print("Largest contig/scaffold name = " + str(longest[0]) + " length = " + str(longest[1]))
print("Shortest contig/scaffold name = " + str(shortest[0]) + " length = " + str(shortest[1]))
print("Mean contig/scaffold size = " + str(sum(seq_lens_list)/float(len(seq_lens_list))))

# Calculate N50 and print to screen
seq_lens_list.sort()
n_copies_of_itself = []
for each_len in seq_lens_list:
    for times in range(each_len):
        n_copies_of_itself.append(each_len)

if len(n_copies_of_itself) % 2 != 0:
       n50 = n_copies_of_itself[int(len(n_copies_of_itself)) / 2]

if len(n_copies_of_itself) % 2 == 0:
    n50 = (n_copies_of_itself[(int(len(n_copies_of_itself)) / 2) - 1] +
           n_copies_of_itself[(int(len(n_copies_of_itself)) / 2)]) / float(2)

print("N50 = " + str(n50))
