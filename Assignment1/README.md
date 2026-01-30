# The Challenge - Universal Plasmid Maker
The aim of this coding challenge is to make a plasmid that can work in an unknown organism.
We are given two inputs:
1. Input.fa : Fasta file containing DNA sequence of organism/plasmid.
2. Design.txt : Text file containing Restriction Enzyme Sites and Antibiotic Markers to be incorporated in the plasmid

# Plasmid Design 
Before starting to code, it is important to make a structural design of the plasmid. Based on concepts taught in class and the paper by Prof. Preeti, I concluded that these are the following things that should be present in a plasmid:
1. Origin of Replication - Used the Ori of the organism itself so that its replication machinery can be used to replicate the plasmid as well. If we use a plasmid specific ori, other replication machinery is required in the plasmid (eg RepA, RepB, RepC proteins).
2. Antibiotic markers - These are useful for antibiotic selection, when we want only the organisms containing the plasmid having that specific marker, to grow.
3. Multiple Cloning Site - A collection of all Restriction Enzyme sites, present exactly once.
4. Origin of Transfer - This is useful for conjugative transfer of plasmid.
5. Spacers - Since we are not aware of the exact sequences, there is a chance of formation of RE sites at junctions, thus I added spacers in between all of these and also between all RE sites in the MCS.
   
# The Code and Its Logic
Starting with the Ori, I applied cumulative GC Skew to find a window where the Ori could be present. I am assuming a single Ori for simplicity.
To further narrow down this window (5000 bases long) I did an AT% analysis to determine long contiguous sequences which generally point to DNA Unwinding Regions. I took the region 300 bp upstream and downstream of the midpoint of the longest contiguous window as my potential ori.

Having found a potential Ori, I moved on to merge all antibiotic markers in one string. I did not feel the need for spacers as promoter and terminator regions are already present.

After that I constructed the multiple cloning site by adding RE sites with 2-4 bp AT spacers. 

Finally I added the OriT of plasmid R1162 based on the research paper.

I added spacers in between all of these key components. All 20-50 bp random AT spacers.

# Output
I ran a final checker function to make sure RE sites are not present anywhere other than the MCS, and that they occur only once inside it. In case the sites show up in the OriC or OriT, it shows an error. For the antibiotic region, It tries all possible combinations until one with no RE sites at junctions is formed. If such a candidate is not found, it shows an error. I also ensure that each RE site occurs exactly once in the MCS, otherwise an errors pops up.
If all checks pass, the final plasmid is stored in output.fa.

# Notes
1. Finding the exact ori purely computationally is quite challenging and requires more than just information about its sequence. GC Skew is good at narrowing down to windows where Oris might be present. Even it can fail in case of certain genomes where the skew is not as apparent.
2. After getting a window from GC Skew, the problem arises as to which factor to use for narrowing down further. I have used one such factor of contiguous AT rich sequences. 
3. A better algorithm could ensure a weighted sum of various parameters such as AT richness, kmer enrichment, DnaA boxes etc.





