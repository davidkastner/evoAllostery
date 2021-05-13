library(DECIPHER)
fas <- "/Users/kastner/Desktop/v9.fasta"
seqs <- readAAStringSet(fas)
aligned <- AlignSeqs(seqs, iterations=4,refinements=10)
adjusted <- AdjustAlignment(aligned)
writeXStringSet(adjusted, file="/Users/kastner/Desktop/v9.an")