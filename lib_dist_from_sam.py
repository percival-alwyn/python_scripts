# lib_dist_from_sam.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Creates library size/frequency distribution table from the infered size column of a .sam

# python lib_dist_from_sam.py yourfile.sam > yoursizedist.csv

# import modules
import sys

# input file
try:
    in_file = open(sys.argv[1])

except:
    # If no input file print help
    print("\nCreates library size/frequency distribution table\n"
          "from the infered size column of a .sam")
    print("\nUse as follows:\npython lib_dist_from_sam.py yourfile.sam > yoursizedist.csv\n\n")
    sys.exit()

distlist = []

counter = 0
# Iterate through each line of .sam file and add sizes to a list 
for x in in_file:
    # Only look at lines of.sam table
    if len(x.split()) > 10:
        # Only look at reads flagged as mapped in correct orientation and within insert size
        if x.split()[1] == "99":
            distlist.append(x.split()[8])
            counter += 1
        elif x.split()[1] == "147":
            distlist.append(str(int(x.split()[8])*-1)) # reads in opposite direction therefore -ve
            counter += 1
        elif x.split()[1] == "83":
            distlist.append(str(int(x.split()[8])*-1)) # reads in opposite direction therefore -ve
            counter += 1
        elif x.split()[1] == "163":
            distlist.append(x.split()[8])
            counter += 1

in_file.close()

# Iterate through sizes list and add new sizes (key) to an array with freq (value) of one
# If size already in array add one to freq (value)
dupdic = {}
for x in distlist:
    if x not in dupdic:
        dupdic[x] = 1
    else:
        dupdic[x] += 1

# Iterate through two dimensional array (dictionary) printing size (key) then freq (value)
size_freq_output = "Size, Frequency\n"
for x in dupdic.keys():
    size_freq_output += (x + "," + str(dupdic[x])) + "\n"
    
print(size_freq_output)
