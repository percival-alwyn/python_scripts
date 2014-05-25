Folder location for python scripts

22MAY2014 added lib_dist_from_sam.py
Creates library size/frequency distribution table from the infered size column of a .sam
Use as follows:
python lib_dist_from_sam.py yourfile.sam > yoursizedist.csv

22MAY2014 added cutter_counter.py
Records: genome size, %GC and number of sites of common restriction endonucleases
Use as follows:
python cutter_counter.py -fastq filename.fastq, or
python cutter_counter.py -fasta filename.fasta

24MAY2014 added fastq_glue.py
Joins fastq files together at sequences and quality scores, enabling triming from leftside sequence and qual score and takes the header from either the left or right side sequence.
Use as follows:
python fastq_glue.py leftsidefilename.fastq rightsidefilename.fastq <-L/-R> <trim left by interger> joinedfilename.fastq
E.g python fastq_glue.py leftsidefilename.fastq rightsidefilename.fastq -L 0 joinedfilename.fastq

25MAY2014 added fast_size_dist.py
Creates size/frequency distribution table from the fasta or fastq. Can be used to determine the size distribution of scaffolds and contig files (fasta) or can be used to calculate library size distribution or sequence length distribution from PacBio fastq files
Use as follows:
python fast_size_dist.py -fasta/-fastq yourfile.fasta/yourfile.fastq > yoursizedist.csv
E.g python fast_size_dist.py -fasta yourfile.fasta > yoursizedist.csv
