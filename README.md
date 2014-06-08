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

01JUN2014 added Fastat.py
Prints to screen basic statistics about .fasta files.
Use as follows:
python Fastat.py yourfile.fa > Basic_stats.txt

02JUN2014 added fastq_2_fasta.py
Converts fastq to fasta
Use as follows:
python fastq_2_fasta.py filename.fastq > filename.fasta

03JUN2014 added av_sam_depths.py
Calculates average depth from a depth files created using samtools depth
Make depth files using samtools, as follows:
samtools depth filename.sorted.bam > filename_depth.txt (see wrappers)

Use av_sam_depths.py as follows:
Make list of depth files using ls *_depth.txt > depth_list.txt
python av_sam_depths.py depth_list.txt > average_depth.txt

08JUN2014 added trim_fastq_len.py
Trims fastq sequence and quality lengths from either end
Use as follows:
python trim_fastq_len.py filename.fastq <-L/-R> <trim by integer> > trimmedfilename.fastq

