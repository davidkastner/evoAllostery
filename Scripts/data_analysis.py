# Import packages and dependencies
import os
import time
import matplotlib.pyplot as plt
import math
import numpy as np
import copy
import scipy.cluster.hierarchy as sch
from scipy.stats import scoreatpercentile
from pysca import scaTools as sca
import colorsys
import mpld3
import pickle as pickle
from optparse import OptionParser

# The files will need some where to go so we will create an output folder
# if not os.path.exists('../output/'):
#     os.makedirs('../output/')

# The raw database file is very large so we will open it using pickle
# We will also save the relevant information
db = pickle.load(open('../Data/PF07686_full.db','rb'))
Dseq = db['sequence']
Dsca = db['sca']
Dsect = db['sector']

# List all elements above the diagonal (i<j):
listS = [Dsca['simMat'][i,j] for i in range(Dsca['simMat'].shape[0]) \
         for j in range(i+1, Dsca['simMat'].shape[1])]

# Cluster the sequence similarity matrix
Z = sch.linkage(Dsca['simMat'], method = 'complete', metric = 'cityblock')
R = sch.dendrogram(Z,no_plot = True)
ind = R['leaves']

# Plotting
plt.rcParams['figure.figsize'] = 9, 4

# Plot a histogram of all the pairwise interactions
plt.subplot(121)
plt.hist(listS, math.floor(Dseq['Npos']/2))
plt.xlabel('Pairwise sequence identities', fontsize=14)
plt.ylabel('Identity counts', fontsize=14)

# Plot the correlation matrix
plt.subplot(122)
plt.imshow(Dsca['simMat'][np.ix_(ind,ind)], vmin=0, vmax=1)
plt.xlabel('Sequence 2', fontsize=14)
plt.ylabel('Sequence 1', fontsize=14)
plt.colorbar()
plt.tight_layout()
plt.savefig("../Figures/fig1.png", dpi=300)
