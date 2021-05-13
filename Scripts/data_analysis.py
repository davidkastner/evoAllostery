#Perform these commands in your terminal with pySCA installed
#scaProcessMSA -a ../data/decipher.an -b ../data/ -s 1O7V -c A -f 'Homo sapiens' -t -n
#scaCore -i ../output/decipher.db
#scaSectorID -i ../output/decipher.db

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
import pickle as pickle
from optparse import OptionParser
if not os.path.exists('../output/'):
    os.makedirs('../output/')

db = pickle.load(open('../output/decipher.db','rb'))
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
plt.subplot(121)
plt.hist(listS, math.floor(Dseq['Npos']/2))
plt.xlabel('Pairwise sequence identities', fontsize=14)
plt.ylabel('Number', fontsize=14)
plt.subplot(122)
plt.imshow(Dsca['simMat'][np.ix_(ind,ind)], vmin=0, vmax=1)
plt.colorbar()
plt.savefig("initial1_decipher.pdf")

# Generate U plots
Useq = Dsca['Useq']
Uica = Dsca['Uica']
plt.rcParams['figure.figsize'] = 9, 8
ica = ["","","","'","'","'"]
for k,U in enumerate(Useq+Uica):
    plt.subplot(2,3,k+1)
    sca.figWeights(U[:,0], U[:,1], Dseq['seqw'][0])
    plt.xlabel(r'${U%s}^{(%i)}_1$'%(ica[k],k%3), fontsize=16)
    plt.ylabel(r'${U%s}^{(%i)}_2$'%(ica[k],k%3), fontsize=16)
plt.tight_layout()
plt.savefig("U_plots_decipher.pdf")

phylo = list();
fam_names = ['Firmicutes', 'Actinobacteria', 'Bacteroidetes', \
             'Cyanobacteria', 'Proteobacteria']
col = (0, 0.18, 0.38, 0.5, 0.6)
# Firmicutes = red, Actinobacteria = yellow, Bacteroidetes = cyan,
# Cyanobacteria = green, Proteobacteria = blue

# Phylogenetic U plots
for i,k in enumerate(fam_names):
    sf = sca.Unit()
    sf.name = fam_names[i].lower()
    sf.col = col[i]
    sf.items = [j for j,q in enumerate(Dseq['hd'])  if sf.name in q.lower()]
    phylo.append(sf)

plt.rcParams['figure.figsize'] = 9, 3.5
U = Dsca['Uica'][1]
pairs = [[2*i,2*i+1] for i in range(3)]
for k,[k1,k2] in enumerate(pairs):
    plt.subplot(1,3,k+1)
    sca.figUnits(U[:,k1], U[:,k2], phylo)
    #sca.figUnits(U[:,k1], U[:,k2], subfam)
    plt.xlabel(r"${U'}^{(2)}_{%i}$"%(k1+1), fontsize=16)
    plt.ylabel(r"${U'}^{(2)}_{%i}$"%(k2+1), fontsize=16)
plt.tight_layout()

# Plot amino acid conservation plot
from matplotlib.ticker import MaxNLocator
fig, axs = plt.subplots(1,1, figsize=(9,3.25))
plt.rc('axes', linewidth=4)
xvals = [i+1 for i in range(len(Dsca['Di']))]
xticks = []
axs.set_xticks(xticks)
plt.bar(xvals, Dsca['Di'], color='k')
axs.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.tick_params(labelsize=25)
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
plt.ylabel(r'Conservation ($D_i$)', fontsize=23)
plt.xlim([0,len(xvals)])
plt.tight_layout()
plt.savefig("../figs/cons_decipher.pdf", bbox_inches = 'tight')

cons_list = np.array(Dsca['Di'])
cons_list.sort()
print('First: {}, {}, {}'.format(cons_list[-1], np.where(Dsca['Di'] == cons_list[-1])[0][0], Dseq['ats'][np.where(Dsca['Di'] == cons_list[-1])[0][0]]))
print('Second: {}, {}, {}'.format(cons_list[-1], np.where(Dsca['Di'] == cons_list[-2])[0][0], Dseq['ats'][np.where(Dsca['Di'] == cons_list[-2])[0][0]]))
print('Third: {}, {}, {}'.format(cons_list[-1], np.where(Dsca['Di'] == cons_list[-3])[0][0], Dseq['ats'][np.where(Dsca['Di'] == cons_list[-3])[0][0]]))
print(Dseq['ats'])

#Create plot of positional correlation matrix
plt.rcParams['figure.figsize'] = 13, 8
plt.imshow(Dsca['Csca'], vmin=0, vmax=1.4,interpolation='none',\
           aspect='equal')
ax = plt.gca()
ax.set_ylabel('Positions', fontsize = 24)
ax.set_xlabel('Positions', fontsize = 24)
plt.tick_params(labelsize=22)
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()
cbar = plt.colorbar(pad=.13)
cbar.ax.tick_params(labelsize=22)
plt.savefig('../figs/termpositional_heatmap_decipher.pdf')

#Generate plot of the eigenspectrum
fig, axs = plt.subplots(1,1, figsize=(9,3))
plt.rc('axes', linewidth=2)
# plt.rcParams['figure.figsize'] = 9, 3.5
hist0, bins = np.histogram(Dsca['Lrand'].flatten(), bins=Dseq['Npos'],
                           range=(0,Dsect['Lsca'].max()))
hist1, bins = np.histogram(Dsect['Lsca'], bins=Dseq['Npos'],
                           range=(0,Dsect['Lsca'].max()))
plt.bar(bins[:-1], hist1, np.diff(bins),color='k')
plt.plot(bins[:-1], hist0/Dsca['Ntrials'], 'r', linewidth=3)
plt.tick_params(labelsize=12)
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
plt.xlabel('Eigenvalues', fontsize=14)
plt.ylabel('Counts', fontsize=14)
print('Number of eigenmodes to keep is %i' %(Dsect['kpos']))
plt.savefig('../figs/eigenspectrum_decipher.pdf', bbox_inches = 'tight')

#Generate t-distribution plots
plt.rcParams['figure.figsize'] = 10,3.5
Vpica = Dsect['Vpica']
for k in range(Dsect['kpos']):
    print(k)
    iqr = scoreatpercentile(Vpica[:,k],75) - scoreatpercentile(Vpica[:,k],25)
    binwidth=2*iqr*(len(Vpica)**(-0.33))
    nbins=int(round((max(Vpica[:,k])-min(Vpica[:,k]))/binwidth))
    plt.subplot(1,Dsect['kpos'],k+1)
    h_params = plt.hist(Vpica[:,k], nbins)
    x_dist = np.linspace(min(h_params[1]), max(h_params[1]), num=100)
    plt.plot(x_dist,Dsect['scaled_pd'][k],'r',linewidth = 2)
    plt.xlim(-.24, .4)
    plt.xlabel(r'$V^p_{%i}$'%(k+1), fontsize=19)
    plt.tick_params(labelsize=16)
    if k == 0:
        plt.ylabel('Counts', fontsize=18)
    if k != 0:
        plt.yticks([])

for n,ipos in enumerate(Dsect['ics']):
    sort_ipos = sorted(ipos.items)
    ats_ipos = ([Dseq['ats'][s] for s in sort_ipos])
    ic_pymol = ('+'.join(ats_ipos))
    print('IC %i is composed of %i positions:' % (n+1,len(ats_ipos)))
    print(ic_pymol + "\n")

    plt.tight_layout()
plt.savefig('../figs/tdist_decipher.pdf')
plt.show()

# plot the SCA positional correlation matrix, ordered by contribution to the top ICs
plt.rcParams['figure.figsize'] = 10, 10
plt.subplot(121)
plt.imshow(Dsca['Csca'][np.ix_(Dsect['sortedpos'], Dsect['sortedpos'])], \
           vmin=0, vmax=2,interpolation='none',aspect='equal',\
           extent=[0,sum(Dsect['icsize']),0,sum(Dsect['icsize'])])
line_index=0
for i in range(Dsect['kpos']):
    plt.plot([line_index+Dsect['icsize'][i],line_index+Dsect['icsize'][i]],\
             [0,sum(Dsect['icsize'])],'w', linewidth = 2)
    plt.plot([0,sum(Dsect['icsize'])],[sum(Dsect['icsize'])-line_index,\
                        sum(Dsect['icsize'])-line_index],'w', linewidth = 2)
    line_index += Dsect['icsize'][i]

plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig('../figs/orig_sector_heatmap_decipher.pdf')

#define the new sector groupings - 2 total
sec_groups = ([0],[1,4],[2,3])
sectors = list()
for n,k in enumerate(sec_groups):
    s = sca.Unit()
    all_items = list()
    for i in k: all_items = all_items+Dsect['ics'][i].items
    s.items = all_items
    s.col = (1/len(sec_groups))*n
    sectors.append(s)

# plot the re-ordered matrix
plt.subplot(122)
line_index=0
sortpos = list()
for s in sectors:
    sortpos.extend(s.items)
plt.imshow(Dsca['Csca'][np.ix_(sortpos, sortpos)], vmin=0, vmax=2,\
           interpolation='none',aspect='equal',\
           extent=[0,len(sortpos),0,len(sortpos)])
for s in sectors:
    plt.plot([line_index+len(s.items),line_index+len(s.items)],\
             [0,len(sortpos)],'w', linewidth = 2)
    plt.plot([0,sum(Dsect['icsize'])],[len(sortpos)-line_index, \
                                       len(sortpos)-line_index],'w', linewidth = 2)
    line_index += len(s.items)

plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig('../figs/reordered_sector_heatmap_decipher.pdf')

#Write the results out to a PyMol file
for i,k in enumerate(sectors):
    sort_ipos = sorted(k.items)
    ats_ipos = ([Dseq['ats'][s] for s in sort_ipos])
    ic_pymol = ('+'.join(ats_ipos))
    print('Sector %i is composed of %i positions:' % (i+1,len(ats_ipos)))
    print(ic_pymol + "\n")
sca.writePymol('2G5R', sectors, Dsect['ics'], Dseq['ats'], \
               '../output/decipher_2hrl.pml', 'A', '../data/', 0)
