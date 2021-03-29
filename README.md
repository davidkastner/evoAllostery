# Statistical Coupling Analysis for the V-set Protein Family
![Graphical Summary of README](Images/graphical_summary.png)
_**Graphical Summary:** Brief introduction >
Generating multiple sequence alignments > Generating a Correlation Matrix_

## Table of Contents
1. **Introduction**
    * Raw data description
    * Installing dependencies
2. **Multiple sequence alignment**
    * Creating your own MSA
    * Annotating your MSA
3. **Generate the correlation matrix**
    * Running the scripts
    * Interpreting the results

## Introduction
### Raw data description

The raw data at the heart of our project is a single binary database file.
This file contains a multiple sequence alignment generated from 60,000 V-set sequences.
Using the pySCA API, the multiple sequence alignment has been enhanced to include phylogenetic metadata.
While this dataset can be easily accessed via the PFam database website,
we have included the processed database file here for ease of use.
For the original multiple sequence alignment:

> https://pfam.xfam.org/family/V-set

## Installation

In order to run these calculations, we will need to install some dependencies.
The Ranganathan Lab has included a beautiful tutorial with the pySCA distribution.
Walking though the pySCA installation tutorial will also install all other dependencies.
You can use a package manager like homebrew to keep the installation clean.
Here I will outline the installation steps, but make sure to refer to the Ranganathan tutorial.

1. Core system dependencies
    * Xcode developer scaTool
    > xcode-select --install
    * python 3
    > brew install python3
    * Pip
    >
    * GCC
    > brew install gcc

1. pySCA
> https://ranganathanlab.gitlab.io/pySCA/install/

2. scipy
> conda install -c anaconda scipy

3. pysca
>

4. Install

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

## Citations
1.
