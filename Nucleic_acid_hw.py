trans_code = {"A": "U",
              "a": "u",
              "C": "G",
              "c": "g",
              "G": "C",
              "g": "c",
              "T": "A",
              "t": "a"}

comp_DNA_code = {"A": "T",
                 "a": "t",
                 "C": "G",
                 "c": "g",
                 "G": "C",
                 "g": "c",
                 "T": "A",
                 "t": "a"}

comp_RNA_code = {"A": "U",
                 "a": "u",
                 "C": "G",
                 "c": "g",
                 "G": "C",
                 "g": "c",
                 "U": "A",
                 "u": "a"}

rev_code = {"A": "T",
            "a": "t",
            "C": "G",
            "c": "g",
            "G": "C",
            "g": "c",
            "U": "A",
            "u": "a"}


def transcribe(seq):
    out = []
    if validate(seq):
        for nuc in seq:
            out.append(trans_code[nuc])
    return ''.join(out)


def reverse(seq):
    out = ""
    if validate(seq, is_dna(seq)):
        out = seq[::-1]
    return out


def complement(seq):
    out = []
    dna = is_dna(seq)
    if validate(seq, dna):
        if dna:
            for nuc in seq:
                out.append(comp_DNA_code[nuc])
        else:
            for nuc in seq:
                out.append(comp_RNA_code[nuc])
    return ''.join(out)


def reverse_transcribe(seq):
    out = []
    if validate(seq, dna=False):
        for nuc in seq:
            out.append(rev_code[nuc])
    return ''.join(out)


def validate(seq, dna=True):
    allowed_dna = "agct"
    allowed_rna = "agcu"
    if dna:
        for nuc in seq.lower():
            if nuc not in allowed_dna:
                print("This is not DNA!")
                return False
    else:
        for nuc in seq.lower():
            if nuc not in allowed_rna:
                if nuc not in allowed_dna:
                    print("This is not DNA or RNA!")
                else:
                    print("This is not RNA!")
                return False
    return True


def is_dna(seq):
    code = "agct"
    for nuc in seq.lower():
        if nuc not in code:
            return False
    return True


while True:
    print("Choose one of the command: transcribe, reverse, complement, "
          "reverse complement, reverse transcription, or exit\n")
    command = input()
    if command == "exit":
        break
    elif command == "transcribe":
        sequence = input("Input DNA sequence:")
        output = transcribe(sequence)
    elif command == "reverse":
        sequence = input("Input DNA or RNA sequence:")
        output = reverse(sequence)
    elif command == "complement":
        sequence = input("Input DNA or RNA sequence:")
        output = complement(sequence)
    elif command == "reverse complement":
        sequence = input("Input DNA or RNA sequence:")
        output = reverse(complement(sequence))
    elif command == "reverse transcription":
        sequence = input("Input RNA sequence:")
        output = reverse_transcribe(sequence)
    else:
        print("Invalid command")
        continue
    print("\nOutput: ", output)



