# vcf_depth_filter.py
# Made by L. Percival-Alwyn, Twitter: LP_Alwyn
# Counts the number of SNP (not indel) varient positions given a minimum lowest depth and can make the depth and SNP only filtered .vcf also.
# Make a multiple .vcf file with per-sample read depth (-D flag) using samtools, as follows:
# samtools mpileup -uDf REFERENCE.fa BAM_FILE_1.bam | bcftools view -bvcg - >  BCF_FILE.bcf
# bcftools view BCF_FILE.bcf | perl /tgac/software/testing/samtools/0.1.19/src/samtools-0.1.19/bcftools/vcfutils.pl varFilter -d 5 > VCF_FILE.vcf
# Use vcf_depth_filter.py as follows:
# python vcf_depth_filter.py VCF_FILE.vcf 10 FILTERED_VCF_FILE.vcf or python VCF_depth_QC.py VCF_FILE.vcf 10

# import modules
import sys

data_lines_count = 0
correct_format_count = 0
depth_count = 0
filtered_vcf = ""
lowest_depth = 100000000000000000000 # A big number (lowest depth is not likely to be more than this)

format = 'GT:PL:DP:GQ'

# Get input file and depth
try:
    vcf_file = open(sys.argv[1])
    depth = int(sys.argv[2])
# If no input file or depth, print help)
except:
    print("\nvcf_depth_filter.py")
    print("Counts the number of SNP (not indel) varient positions given a minimum lowest depth and can make the depth and SNP only filtered .vcf also.")
    print("\nMake a multiple .vcf file with per-sample read depth (-D flag) using samtools, as follows:")
    print("samtools mpileup -uDf REFERENCE.fa BAM_FILE_1.bam | bcftools view -bvcg - >  BCF_FILE.bcf")
    print("bcftools view BCF_FILE.bcf | perl /tgac/software/testing/samtools/0.1.19/src/samtools-0.1.19/bcftools/vcfutils.pl varFilter -d 5 > VCF_FILE.vcf")
    print("\nUse vcf_depth_filter.py as follows:")
    print("python vcf_depth_filter.py VCF_FILE.vcf 10 FILTERED_VCF_FILE.vcf \n\nor\n\npython VCF_depth_QC.py VCF_FILE.vcf 20\n")
    sys.exit()

# Iterate through each of the vcf file
counter = 0
CHROM = False
for line in vcf_file:
    #When 'CHROM' (part of the data line headings) is present start to parse the file
    if CHROM == False:
        filtered_vcf += line
        if "#CHROM" == line[:6]:
            CHROM = True
            filtered_vcf += line
    else:
        # Only parse SNP on INDEL data lines
        if "DP=" in line.split()[7][:3]:
            data_lines_count += 1
            list_line = line.split()
            # 'GT:PL:DP:GQ' must be present (must have per-sample read depth (-D flag) when making multiple .bcf)
            if format in list_line[8]:
                correct_format_count += 1
                lowest_depth_of_line = 1000000000000000000000 # Another big number (lowest depth in data line is not likely to be more than this)
                # iterate through each depth position
                for x in list_line[9:]:
                    depth_pos = x.split(":")
                    if int(depth_pos[2]) < lowest_depth_of_line:
                        lowest_depth_of_line = int(depth_pos[2])
                # only count data lines and include data lines that have a minimum depth greather than the filter depth
                if lowest_depth_of_line >= depth:
                    depth_count += 1
                    filtered_vcf += line
                # record losest depth in file
                if lowest_depth_of_line < lowest_depth:
                    lowest_depth = lowest_depth_of_line

# IF 'GT:PL:DP:GQ\' is present, print stats
if correct_format_count > 0:
    print("\nvcf_depth_filter.py - Results")
    print("Number of SNP data lines: " + str(data_lines_count))
    print("Number of SNP data lines with format \'GT:PL:DP:GQ\': " + str(correct_format_count))
    print("Lowest depth before filtering: " + str(lowest_depth))
    print("Number of SNP data lines after filtering to a depth of " + str(depth) + ": " + str(depth_count))
    # If sys.argv[3] present write filtered output to name given in sys.argv[3]
    try:
        filtered_vcf_file = open(sys.argv[3], "w")
        filtered_vcf_file.write(filtered_vcf)
        filtered_vcf_file.close()
        print("Filtered output file \"" + sys.argv[3] + "\" has been made.\n")
    # If sys.argv[3] not present inform user that no output file was given
    except:
        print("No filtered output file made.\n")
        pass

# IF 'GT:PL:DP:GQ\' is not present, print stats and inform user that 'GT:PL:DP:GQ\' format is not present, then print samtools mpile up instructions.
else:
    print("\nvcf_depth_filter.py - Results")
    print("Number of SNP data lines: " + str(data_lines_count))
    print("Number of SNP data lines with format \'GT:PL:DP:GQ\': " + str(correct_format_count))
    print("Format \'GT:PL:DP:GQ\' must be  present.")
    print("\nMake a multiple .vcf file with per-sample read depth (-D flag) using samtools, as follows:")
    print("samtools mpileup -uDf REFERENCE.fa BAM_FILE_1.bam | bcftools view -bvcg - >  BCF_FILE.bcf")
    print("bcftools view BCF_FILE.bcf | perl /tgac/software/testing/samtools/0.1.19/src/samtools-0.1.19/bcftools/vcfutils.pl varFilter -d 5 > VCF_FILE.vcf")
    print("\nUse vcf_depth_filter.py as follows:")
    print("python vcf_depth_filter.py VCF_FILE.vcf 10 FILTERED_VCF_FILE.vcf \n\nor\n\npython VCF_depth_QC.py VCF_FILE.vcf 20\n")

# Close vcf file
vcf_file.close()
