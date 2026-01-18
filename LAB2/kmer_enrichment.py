def read_fasta(f):
  sequence = []
  with open(f,'r') as g:
    for i in g.readlines():
      if i.startswith('>'):
        continue
      else:
        sequence.append(i)
  return ''.join(sequence)

def Signal_Checker(genome,L,k,step):
  freq = []
  coords = []
  for i in range(0,len(genome)-L,step): #Checking all windows
    window = genome[i:i+L]
    kmer_w = {} # Kmer count dictionary for current window
    for j in range(len(window)-k):
      curr_k = window[j:j+k]
      if curr_k in kmer_w:
        kmer_w[curr_k] +=1
      else:
        kmer_w[curr_k] = 1
    m =  max(kmer_w.values()) # Frequency of most frequent kmer in this window
    x = i + (L//2) # Position of most frequent kmer in this window
    freq.append(m)
    coords.append(x)
  return freq,coords

genome = read_fasta('genomic.fa')
k = 8
L = 5000
step = 500
freq, coords = Signal_Checker(genome,L,k,step)

import matplotlib.pyplot as plt

plt.figure(figsize=(15,12))
plt.plot(coords,freq)
plt.xlabel('K-mer position')
plt.ylabel('K-mer Count')

plt.show()
