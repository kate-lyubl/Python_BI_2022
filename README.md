# Python_BI_2022. Pandas and visualization challenge

This homework contains two files: homework.ipynb (Jupiter notebook) and pandas_assignment_and_visualization.py (python script for notes).

Task 1. Working with real data (20 points)
In bioinformatics, you often have to work with tabular data (gff, bed, vcf, etc.), but it is quite difficult to do various advanced operations in the terminal, and this is where pandas comes to the rescue.
The attached files contain an annotation of the ribosomal RNA of some metagenomic dataset in the GFF format (rrna_annotation.gff), as well as a file with the alignment of the metagenomic assembly to the same dataset in the BED 6 format (alignment.bed).

- Write read_gff and read_bed6 functions to read the appropriate formats. They should return dataframes as in the example (picture Example1), but the names of the columns can be anything.

- The attribute column carries too much redundant information and is not convenient to use, leave only the data on the rRNA type in it in one short line (16S, 23S, 5S).

- Make a table where for each chromosome (in fact, these are not chromosomes, but reference genomes), the amount of rRNA of each type is shown. Build a barplot displaying this data (rRNA_barplot image)

- Next is the most interesting. We want to know how much rRNA was successfully assembled during the assembly process. To do this, you can use the bedtools intersect program and intersect these two files. As a result, only rRNA records will be saved, the interval of which overlapped with the contig interval in the alignment, which means that this gene is in the assembly. But forget bedtools! We actually have a pandas here! So let's get the same result in it. Output a table containing the original records about rRNA completely included in the assembly (not a fragment), as well as a record about the contig in which this RNA got. The final table should look something like this (picture Example2). Please note that several rRNAs can fall into one contig.

Task 2. Chart customization (20 points)

To visualize differential gene expression data, you can use a special type of graph - volcano plot. On the X axis, logFC (Logarithmic Fold Change) is plotted on it - how many times the gene expression has changed in powers of two (logFC=-8 - the gene expression has changed 2^-8 times). The Y-axis plots the level of significance of these changes as the negative logarithm of the p-value (adjusted for multiple comparisons).

In this task, you need to reproduce the graph volcano_plot.png (attached to the task) as accurately as possible. To do this, use the data file diffexpr_data.tsv.gz (pandas can open .gz files, so it is not necessary to decompress them). The data is already pre-processed, there is no need to count p-value and take logarithms, just use the logFC and log_pval columns. If necessary, you can group the data or take subsets, but in the end, the chart should have exactly the values ​​from these columns.
