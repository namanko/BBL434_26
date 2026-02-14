# The Challenge - Affined Gap Sequence Alignment Tool
The aim of this coding challenge is to make a local sequence alignment tool using the affine gap method of gap opening and gap extension.
We are given three inputs:
1. seq1.fasta : Fasta file containing DNA sequence 1
2. seq2.fasta : Fasta file containing DNA sequence 2
3. scoring.csv : CSV file containing gap opening penalty (row 1), gap extension penalty (row 2) and scoring matrix in the order of ACGT (row 3 to 6)

# Underlying Logic and Code
This problem is solved using dynamic programming and backtracking. We initialize three matrices Middle (Match/Mismatch) -> M, Upper (Deletion) -> X and  Lower (Insertion) -> Y.
We start from the first element of M, and intialize first column of Y and first row of X as:

`Y[i][0] = gap_opening_penalty + (i-1)*gap_extension_penalty`

`X[0][j] = gap_opening_penalty + (j-1)*gap_extension_penalty`

After initialization, we score all points as:

`s = score(base1,base2)`

`M[i][j] = max(M[i-1][j-1],X[i-1][j-1],Y[i-1][j-1]) + s`

`X[i][j] = max(M[i][j-1] + gap_opening_penalty, X[i][j-1] + gap_extension_penalty)`

`Y[i][j] = max(M[i-1][j] + gap_opening_penalty, Y[i-1][j] + gap_extension_penalty)`

Final score is maximum of last elements of M, X and Y.

Now we backtrack:
Starting from the final base, we compare the scores of the previous element depending on which matrix we are in and simultaneously add bases/gaps to the alignments.
   
# Output
The code prints an alignment score, and the two sequences aligned beneath it.
