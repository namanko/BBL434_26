import sys

def fasta_records(fasta_file):
    with open(fasta_file, "r") as f:
        c = 0
        for line in f:
            if line.startswith('>'):
                c+=1
    return c

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <seq.mfa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    count = fasta_records(fasta_file)
    print(count)
