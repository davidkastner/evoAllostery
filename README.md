# Statistical Coupling Analysis for the V-set Protein Family
![Graphical Summary of README](Figures/graphical_summary.png)
_**Graphical Summary:** Brief introduction >
Generating multiple sequence alignments > Generating a Correlation Matrix_

## Table of Contents
1. **Overview**
    * Introduction
    * Raw data description
2. **Installation**
    * Folder structure
    * Installing dependencies
3. **Multiple sequence alignment**
4. **Generate the correlation matrix**

## 1. Overview
### Introduction
The purpose of these repo is to facilitate running statistical coupling analysis for the V-set family proteins.
Specifically, the project is looking at evolutional similarities between PD-1, PD-L1, and VISTA.
The repo starts from raw structural and sequence data and generates a multiple sequence alignment for PD-1.
The alignment is then processed to extract evolutional information,
to find domains under unique selectional pressure.
The pySCA code is written and maintained by the Ranganathan Lab and is used extensively throughout the analysis (1,2).
It is beautifully documented here:  
https://ranganathanlab.gitlab.io/pySCA/

### Raw data description

The raw data at the heart of our project is a single binary database file.
This file contains a multiple sequence alignment generated from 60,000 V-set sequences.
Using the pySCA API, the multiple sequence alignment has been enhanced to include phylogenetic metadata.
While this dataset can be easily accessed via the PFam database website,
we have included the processed database file here as they can take up to 7 hours to download and annotate.
However, we will outline the process below for those who would benefit.
You can find the database file in the _Data_ directory.
For the original multiple sequence alignment data visit and select _Generate_:  
https://pfam.xfam.org/family/V-set#tabview=tab3

## 2. Installation
### Folder structure
The repo is divided into three key directories: _Data_, _Figures_, and _Scripts_.
The _Data_ directory contains the raw database file with the multiple sequence alignment and phylogenetic annotations.
The _Figures_ directory contains an example output figure for comparision and is where any output figures will be saved.
The _Scripts_ directory contains a python script that interacts with the database file.
The script called _data_analysis_ currently will generated a single figure;
however, more functionality will be added in the future.

### Installing dependencies
In order to run these calculations, we will need to install some dependencies.
The Ranganathan Lab has included a beautiful tutorial with the pySCA distribution.
Completing the Ranganathan Lab pySCA installation tutorial will automatically install several other dependencies, including:
numpy, scipy, argparse, wheel, and matplotlib.
You can use a package manager like homebrew to keep the installation clean.
The installation is summarized below,
but make sure to refer to the original Ranganathan tutorial for more details:
https://ranganathanlab.gitlab.io/pySCA/install/

1. Core system dependencies
    > xcode-select --install  
    > brew install python3  
    > brew install gcc  

2. Fasta36
    > git clone https://github.com/wrpearson/fasta36.git  
    > cd fasta36/src  
    > make -j2 -f ../make/Makefile.os_x86_64 all  
    > cp -r ../bin /usr/local  
    > rm /usr/local/bin/README  
    > cd ../..  

3. pySCA
    > git clone https://github.com/ranganathanlab/pySCA.git  
    > cd pySCA-master  
    > pip install .  

4. The pySCA distribution automatically installs the following:
    * numpy
    * scipy
    * argparse
    * wheel
    * matplotlib

## 3. Multiple Sequence Alignment

_Note: This step is optional and is performed in the pySCA directory created upon completion of step 3 of the installation._
https://ranganathanlab.gitlab.io/pySCA/install/

While we have provided the multiple sequence alignment (MSA) file, it can also be generated from scratch.
If you wish to use our MSA then you can use the file system in this Github, and skip to the next section.
If you wish to generate the MSA then you will need to use the pySCA installation directory.
First, visit the PFam website and search for the V-set protein family: https://pfam.xfam.org/family/V-set.
Download the MSA as an annotation file in the FASTA file format.
You will also need the PDB for PD-1, which can be found here: https://www.rcsb.org/structure/3BIK.
Lastly, download the databased annotation file 'pfamseq.txt': http://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/database_files/.
This file is very large and will take several hours to finish downloading.
Add all three files to the pySCA directory at /pySCA-master/data/.
Run the following commands from the terminal to process the annotated MSA file.
These commands create the same .db file that we have provided.
For benchmarking purposes, you should know that the first line is the most computationally expensive.
It can take several hours. The following three should take less than 10 minutes.

> annotateMSA -i ../data/PF07686_full.txt -o ../data/PF07686_full.an -a 'pfam' -p ./data/pfamseq.txt  
> scaProcessMSA -a ../data/PF07686_full.an -b ../data/ -s 3BIK -c B -f 'Homo sapiens' -t -n  
> scaCore -i ../output/PF07686_full.db  
> scaSectorID -i ../output/PF07686_full.db  

## 4. Generating the correlation matrix

Download the _domain-clusters_ repository.
Inside the scripts directory of the _domain-clusters_ Github repository,
you will find a python script.
It takes a single file as input, the provided .db file, and outputs the figure.
Once pySCA has been successfully installed,
this script will create a histogram of all pairwise interactions within the dataset.
It will also generate a correlation matrix, which shows which sequences within the MSA are correlated.
Due to the size of the database file, this script can take 15 minutes to complete.
When it completes, the figure will be placed automatically in the Figures directory.
For reference, an example of the figure has been provided in the Figures directory.
It is called "fig1_example.pdf."

> python data_analysis.py  

## Citations
1. Rivoire, O., et al. Evolution-Based Functional Decomposition of Proteins. (2016)
2. Halabi, N., et al. Protein sectors: evolutionary units of three-dimensional structure. Cell. 138, (2009).
