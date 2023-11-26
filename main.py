from Bio import SeqIO

# Parse the fasta file to produce each sequence and its reverse compliment.
nucleotide_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}


# Outputs the reverse compliment of a dna sequence.
def complement(string):
    compl = ''.join(nucleotide_dict.get(char, char) for char in string)
    return compl


file = SeqIO.read('rosalind.txt', 'fasta')
seq = str(file.seq)
rev = str(complement(file.seq))

# Will search each Fasta entry, and it's reverse compliment for common substrings.
for i in range(len(seq)):
    for j in range(i, len(seq)):
        m = seq[i:j + 1]
        rev_m = rev[i:j + 1]
        if 4 <= len(m) <= 12:
            if m == rev_m[::-1]:
                print(i + 1, len(m))
