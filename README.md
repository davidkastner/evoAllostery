# Statistical Coupling Analysis for the V-set Protein Family
## Introduction

For this project, the raw date as been stored in a binary database file.
It contains the multiple sequence alignment for the V-set protein family.
The multiple sequence also includes full annotations with phylogenetic metadata.
This dataset can be easily accessed via the PFam database website.

> https://pfam.xfam.org/family/V-set

In order to run these calculations, we will need to install some dependencies.
For a clean set up, we recommend using brew on MacOS.
Similar commands can be used for Linux and windows.

## Installation
1. Install matplotlib
> conda install -c conda-forge matplotlib

2. Install scipy
> conda install -c anaconda scipy

3. Install pysca
>

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
# import mpld3
import pickle as pickle
from optparse import OptionParser

## Generating the Summary Histogram and Heatmap
