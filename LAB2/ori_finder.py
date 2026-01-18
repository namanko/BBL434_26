def read_fasta(f):
  sequence = []
  with open(f,'r') as g:
    for i in g.readlines():
      if i.startswith('>'):
        continue
      else:
        sequence.append(i.strip())
  return ''.join(sequence)


def OriFinder(genome,L,k,step):
  freqKmer, posKmer  = Signal_Checker(genome,L,k,step)
  posSkew, gcSkew = GCSkew(genome,L,step)

  mfK = max(freqKmer)
  mposK = posKmer[freqKmer.index(mfK)]

  ms = min(gcSkew)
  mposS = posSkew[gcSkew.index(ms)]

  if mposK>mposS:
    lower = mposS - (L//2)
    upper = mposK + (L//2)
  else:
    lower = mposK - (L//2)
    upper = mposS + (L//2)
  return mposS, mposK

genome = read_fasta('genomic.fa')
k = 8
L = 5000
step = 500

ori_loc, enriched_coord =  OriFinder(genome,L,k,step)
print('='*50)
print('Ori location (via Cumulative min GC Skew)')
print(f'Coordinate: {ori_loc} bp')
print('='*50)
print('Most enriched region (Overrepresented kmer)')
print(f'Center Coordinate: {enriched_coord} bp')
print('='*50)
