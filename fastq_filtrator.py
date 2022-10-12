def filter_gc(read, gc_bounds):
    if isinstance(gc_bounds, tuple):
        return gc_bounds[0] <= count_gc(read) <= gc_bounds[1]
    else:
        return count_gc(read) <= gc_bounds


def count_gc(read):
    gc = [nuc for nuc in read if nuc in ["G", "C"]]
    return len(gc) / len(read) * 100


def filter_quality(quality, quality_threshold):
    mean_quality = sum([ord(c) for c in quality]) / len(quality)
    return mean_quality >= quality_threshold


def filter_length(read, length_bounds):
    if isinstance(length_bounds, tuple):
        return length_bounds[0] <= len(read) <= length_bounds[1]
    else:
        return len(read) <= length_bounds


def write_file(filename, list_name):
    with open(filename, "w") as file:
        for (head, read, separator, quality) in list_name:
            file.write(f"{head}\n")
            file.write(f"{read}\n")
            file.write(f"{separator}\n")
            file.write(f"{quality}\n")


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100),
         length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False):
    failed_reads = []
    passed_reads = []

    with open(input_fastq) as file:
        lines = file.readlines()
    heads = [item[:-1] for item in lines[::4]]
    reads = [item[:-1] for item in lines[1::4]]
    separators = [item[:-1] for item in lines[2::4]]
    qualities = [item[:-1] for item in lines[3::4]]

    for (head, read, separator, quality) in zip(heads, reads, separators, qualities):
        if filter_gc(read, gc_bounds) and \
                filter_quality(quality, quality_threshold) and \
                filter_length(read, length_bounds):
            passed_reads.append((head, read, separator, quality))
        else:
            failed_reads.append((head, read, separator, quality))
    write_file(filename=f"{output_file_prefix}_passed.fastq", list_name=passed_reads)

    if save_filtered:
        write_file(filename=f"{output_file_prefix}_failed.fastq", list_name=failed_reads)


