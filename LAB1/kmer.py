#!/usr/bin/env python3

import sys

def read_fasta_single_seq(fasta_file):
    seq = []
    with open(fasta_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            seq.append(line)
    return "".join(seq)

def count_unique_kmers(seq, k=3):
    kmers = set()
    for i in range(len(seq) - k + 1):
        kmers.add(seq[i:i+k])
    return len(kmers)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <seq.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequence = read_fasta_single_seq(fasta_file)

    kmer_count = count_unique_kmers(sequence, k=3)
    print(kmer_count)
