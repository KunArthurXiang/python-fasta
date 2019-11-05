import sys

def read_fasta(filename):
    """
    Read a FASTA format sequence from the names file
    """
    seq =''
    f=open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            seq=seq+line
    f.close()
    return seq

print(read_fasta(sys.argv[1]))






