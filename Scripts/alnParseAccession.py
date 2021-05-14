# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:47:56 2021

@author: Anna
"""

#!/usr/bin/env python
"""
 parse accession numbers from the headers of an alignment with typical Blast formatting.
:Arguments:
    Input_MSA.fasta (the alignment to be processed)
:Keyword Arguments:
    --output             output file name, default: FilteredAln.fa
This script was adpated from thr alnParseGI script from the pySCA module
"""

import scaTools as sca
import argparse

if __name__ =='__main__':
    #parse inputs
    parser = argparse.ArgumentParser()
    parser.add_argument("alignment", help='Input Sequence Alignment')
    parser.add_argument("--output", dest="outputfile", default = 'Acc_Num', help="specify an outputfile name")
    options = parser.parse_args()

    headers, seqs = sca.readAlg(options.alignment)
    accs = [h.split(':')[0] for h in headers]
    
    f = open(options.outputfile, 'w')
    for acc in accs:
        f.write('%s\n' % acc)
    f.close()