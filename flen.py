#!/usr/bin/env python3

import sys

def fasta_length(fasta_file):
    seq = []
    with open(fasta_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            seq.append(line)
    return len("".join(seq))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <seq.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    length = fasta_length(fasta_file)
    print(length)
