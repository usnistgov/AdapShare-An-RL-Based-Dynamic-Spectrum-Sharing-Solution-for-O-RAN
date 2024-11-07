"""
Disclaimer: NIST-developed software is provided by NIST as a public service. You may use, copy, and distribute copies of the software in any medium, 
provided that you keep intact this entire notice. You may improve, modify, and create derivative works of the software or any portion of 
the software, and you may copy and distribute such modifications or works. Modified works should carry a notice stating that you changed 
the software and should note the date and nature of any such change. Please explicitly acknowledge the National Institute of Standards 
and Technology as the source of the software. 

NIST-developed software is expressly provided "AS IS." NIST MAKES NO WARRANTY OF ANY KIND, EXPRESS, IMPLIED, IN FACT, OR ARISING BY 
OPERATION OF LAW, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, 
AND DATA ACCURACY. NIST NEITHER REPRESENTS NOR WARRANTS THAT THE OPERATION OF THE SOFTWARE WILL BE UNINTERRUPTED OR ERROR-FREE, OR THAT ANY 
DEFECTS WILL BE CORRECTED. NIST DOES NOT WARRANT OR MAKE ANY REPRESENTATIONS REGARDING THE USE OF THE SOFTWARE OR THE RESULTS THEREOF, INCLUDING 
BUT NOT LIMITED TO THE CORRECTNESS, ACCURACY, RELIABILITY, OR USEFULNESS OF THE SOFTWARE.

You are solely responsible for determining the appropriateness of using and distributing the software and you assume all risks associated 
with its use, including but not limited to the risks and costs of program errors, compliance with applicable laws, damage to or loss of data, 
programs or equipment, and the unavailability or interruption of operation. This software is not intended to be used in any situation where a 
failure could cause risk of injury or damage to property. The software developed by NIST employees is not subject to copyright protection 
within the United States.
"""
"""
Objective: This script cleans the Raw_Output_BladeRF.tsv file generated by the LTE sniffer (OWL). The end 
result is a Output_BladeRF_OWL_Modified.tsv file with data extracted for resource demand prediction. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import csv

# code to remove any blank line from the raw data file
# Line 31-38 are commented since we provide Output_BladeRF.OWL.tsv
# with open(r"Raw_Output_BladeRF.tsv", newline='') as in_file:
#     with open("Output_BladeRF_OWL.tsv", 'w', newline='') as out_file:
#         writer = csv.writer(out_file)
#         for row in csv.reader(in_file):
#             if row:
#                 writer.writerow(row)

# adding header
headerList = ['SFN','Subframe Index','RNTI','Direction','MCS','NRB','TBS',	
              'TBS0','TBS1','DCI message type','NDI0','NDI1','HARQ PID',	
              'NCCE Location','Aggregation Level','CFI','DCI Correctness Check']
# open CSV file and assign header
with open('Output_BladeRF_OWL_Modified.tsv', 'w') as file:
    dw = csv.DictWriter(file, delimiter='\t', 
                        fieldnames=headerList)
    dw.writeheader()
                
# code to remove unnecessary information and blank line from the raw file and 
# create a file with the decoded DCI information corresponding to DCI mesage 
# type 8, i.e, subframes carrying data.
with open(r"Output_BladeRF_OWL.tsv", "r") as f:
    with open("Output_BladeRF_OWL_Modified.tsv", "w") as f_out:
        reader = csv.reader(f, delimiter="\t")
        writer = csv.writer(f_out, delimiter="\t")
        for row in reader:
            if row[0].startswith(tuple('0123456789')):
                writer.writerow(row)    
            