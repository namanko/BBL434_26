import matplotlib.pyplot as plt

def read_fasta(f):
  sequence = []
  with open(f,'r') as g:
    for i in g.readlines():
      if i.startswith('>'):
        continue
      else:
        sequence.append(i)
  return ''.join(sequence)

def GCSkew(genome,L,step):
  totalskew = []
  pos = []
  currskew = 0
  for i in range(0,len(genome)-L, step):
    window = genome[i:i+L]
    numG = 0
    numC = 0
    for base in window:
      if base == 'G':
        numG +=1
      elif base == 'C':
        numC +=1
    if numG==numC==0:
      totalskew.append(0)
    else:
      currskew += (numG-numC)/(numG+numC)
      totalskew.append(currskew)
      pos.append(i +  (L//2))
  return pos, totalskew

genome = read_fasta('genomic.fa')
L = 5000
step = 500
positions, GCskew = GCSkew(genome,L,step)

plt.figure(figsize=(13,12))
plt.plot(positions,GCskew)
plt.xlabel('Genome position')
plt.ylabel('GC Skew')
plt.title('GC Skew Plot')

plt.show()
