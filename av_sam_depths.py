# av_sam_depths.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Calculates average depth from a depth files created using samtools depth
# Make depth files using samtools, as follows:
# samtools depth filename.sorted.bam > filename_depth.txt (see wrappers)
# Use av_sam_depths.py as follows:
# Make list of depth files using ls *_depth.txt > depth_list.txt
# python av_sam_depths.py depth_list.txt > average_depth.txt

# import modules
import sys

# Get input file
try:
    depth_files_list_file = open(sys.argv[1])

# If no input file print help
except:
  print("\nav_sam_depths.py calculates average depth from depth files created using samtools depth.\n"
        "\nUse as follows:\nMake list of depth files using ls *_depth.txt > depth_list.txt\n\n"
        "then run the command\n\npython av_sam_depths.py depth_list.txt > average_depth.txt\n")
  sys.exit()

# Save list of files to memory (so the input file isn't open too long)
depth_files_list = depth_files_list_file.readlines()

# Close input file
depth_files_list_file.close()

# Iterate through each of the depth files in the depth files list
for depth_file_name in depth_files_list:
    try:
        # Open depth file
        depthfile = open(depth_file_name.replace("\n",""))
        total_depth = 0
        counter = 0
        # Iterate through each line of each depth file
        for line in depthfile:
            # Split each line by white space
            line_as_list = line.split()
            # Add depth from column 3
            total_depth += int(line_as_list[2])
            # Keep count of number of depths
            counter += 1
        # Print average depth to screen for each file
        print(depth_file_name.replace("\n","") + "    Depth = %.2f" % float(total_depth/float(counter)))

    # If no depth (empty file), print warning
    except ZeroDivisionError:
        print(depth_file_name.replace("\n","") + "    This file has no depth!")

    # Close depthfile
    depthfile.close()

