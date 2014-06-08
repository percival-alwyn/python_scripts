# trim_fastq_len.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Trims fastq sequence and quality lengths from either end
# Use as follows:
# python trim_fastq_len.py filename.fastq <-L/-R> <trim by integer> > trimmedfilename.fastq

# import modules
import sys

# Get input file, trim end and trim back number
try:
    infile = sys.argv[1]
    trim_end = sys.argv[2]
    trim_by = int(sys.argv[3])
    if "R" in trim_end and "L" in trim_end:
        print("\nTo use trim_fastq_len.py trim one end at a time.\n")
        sys.exit()
        
# If no input file print help
except:
    print("\ntrim_fastq_len.py trims fastq sequence and quality lengths from either end.\n"
          "\nUse as follows: \npython trim_fastq_len.py filename.fastq <-L/-R> <trim by integer> > trimmedfilename.fastq")
    print("\nE.g\npython trim_fastq_len.py filename.fastq -L 50 > trimmedfilename.fastq\n")
    sys.exit()

# Open fastq file
f = open(infile)

# Iterate through lines in file adding headers and separaters while trimming sequence and quality score
trimmed = ""
counter = 0
for x in f:
    # Sequence and quality score lines
    if (counter - 1)% 2 == 0:
        # trim from right
        if "R" in trim_end.upper():
            trimmed += x.replace("\n", "")[:(trim_by * -1)] + "\n"
        # trim from left
        if "L" in trim_end.upper():
            trimmed += x.replace("\n", "")[trim_by:] + "\n"

    # Add header and separater
    else:
        trimmed += x
    counter += 1
        
f.close()
# Print to screen trimmed fastq
print(trimmed)
