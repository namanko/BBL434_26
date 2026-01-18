def read_fasta(f):
  sequence = []
  with open(f,'r') as g:
    for i in g.readlines():
      if i.startswith('>'):
        continue
      else:
        sequence.append(i)
  return ''.join(sequence)

def KmerCountDict(text,k):
  kmer_en = {}
  for i in range(len(text)-k):
    if text[i:i+k] in kmer_en:
      kmer_en[text[i:i+k]] +=1
    else:
      kmer_en[text[i:i+k]] = 1
  return kmer_en

def FindClumps(text,L,k,t):
  ClumpList = []
  for i in range(len(text)-L):
    window =  text[i:i+L]
    kmer_dict = KmerCountDict(window,k)

    for j in kmer_dict:
      if kmer_dict[j] >= t:
        if j not in ClumpList:
          ClumpList.append(j)
  return ClumpList

genome = read_fasta('genomic.fa')
k = 8
t = 3
L = 1000

print(len(FindClumps(genome,L,k,t)))
