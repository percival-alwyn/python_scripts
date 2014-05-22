# cutter_counter.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Records: genome size, %GC and number of sites of common restriction endonucleases

# python cutter_counter.py -fastq filename.fastq, or
# python cutter_counter.py -fasta filename.fasta


# import modules
import sys

# Get file type flag and input file
try:
  file_type = sys.argv[1]

  if file_type == "-fastq":
    every = 4
  if file_type == "-fasta":
    every = 2

  f = open(sys.argv[2])

# If no input file print help
except:
  print("\ncutter_counter.py records genome size, %GC and number of sites of common \nrestriction endonucleases\n"
        "\nUse as follows: \npython cutter_counter.py -fastq filename.fq")
  print("or\npython cutter_counter.py -fasta filename.fa\n")
  sys.exit()

# Make empty string to recieve sequences
justreads = ""

# Iterate through each line of fasta/q file and add sequence lines to the justreads variable
line_counter = 0
for x in f:
  if (line_counter - 1) % every == 0:
    justreads += x
  line_counter += 1

f.close()

# Make sure all characters are uppercase
justreads = justreads.upper()

# Calculate genome sizes with and without ambiguity
print "Length of seq = " + str(len(justreads.replace("\n","")))
print "Length of T+G+A+C seq (not counting ambiguity codes) " + str(justreads.count("G")+ justreads.count("C")+ justreads.count("A")+ justreads.count("T"))

# Calculate GC content with and without ambiguity
print "GC as % length of all reads " + str((justreads.count("G")+ justreads.count("C"))/float(len(justreads.replace("\n","")))*100)
print "GC as % A+T+G+C " + str(((justreads.count("G")+ justreads.count("C"))/(float(justreads.count("G")+ justreads.count("C")+ justreads.count("A")+ justreads.count("T")))*100))

# Count number of cutsites for each common cutter
print "AscI sites = " + str(justreads.count('GGCGCGCC'))
print "BamHI sites = " + str(justreads.count("GGATCC"))
print "BbvCl sites = " + str(justreads.count("CCTCAGC"))
print "BglII sites = " + str(justreads.count("AGATCT"))
print "EagI sites = " + str(justreads.count("CGGCCG"))
print "EcoRI sites = " + str(justreads.count("GAATTC"))
print "EcoRV sites = " + str(justreads.count("GATATC"))
print "HindIII sites = " + str(justreads.count("AAGCTT"))
print "NotI sites = " + str(justreads.count("GCGGCCGC"))
print "NsiI sites = " + str(justreads.count('ATGCAT'))
print "PacI sites = " + str(justreads.count('TTAATTAA'))
print "PstI sites = " + str(justreads.count('CTGCAG'))
print "SbfI sites = " + str(justreads.count('CCTGCAGG'))
print "Xho sites = " + str(justreads.count('CTCGAG'))
print "XmaI sites = " + str(justreads.count('CCCGGG'))
