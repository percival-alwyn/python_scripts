# fastasizefilter.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Filters FASTA formats by a specified sequence size
# Use as follows:
# python fastasizefilter.py in_file.fa out_file.fa <keep greater than size>

# import modules
import sys

# input file
try:
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], "w")
    size = int(sys.argv[3])
except:
    # If inputs do not open and convert to integers print help
    print("\nfastasizefilter.py filters FASTA formats by a specified sequence size\n")
    print("Use as follows:\npython fastasizefilter.py in_file.fa out_file.fa <keep greater than size>\n")
    sys.exit()

# for each fasta check length is above specified size and save to outfile
fasta = ""
counter = 0
for line in infile:
    if counter % 2 == 0:
        fasta += line
    else:
        if len(line.replace("\n","")) < 100:
            fasta = ""
        else:
            fasta += line
            outfile.write(fasta)
            fasta = ""
    counter += 1

# close files
infile.close()
outfile.close()
