# Python_BI_2022

Here is a program for working with .fastq files. This program can:

- filter reads by GC content

- filter reads by quality

- filter reads by length

- save satisfying the criteria reads

The given parameters are:

- __input_fastq__: input file path

- __output_file_prefix__: prefix of the output file

- __gc_bounds__: interval of the GC content

- __length_bounds__: interval of the read's length

- __quality_threshold__: low boundary of the mean read quality

- __save_filtered__: save filtered read
