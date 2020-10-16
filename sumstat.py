import pandas as pd 
import os
import csv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Sumstat for PRS calculation')
parser.add_argument('--i', type=str, help='Dir for coverageFile')
args = parser.parse_args()

os.chdir(args.i)

filestat = pd.read_csv("coverageFile.txt",names=["Trait Name","PGS ID","Prim Count"],sep="\t")
filestat["Allele Count"] = np.nan
filestat["Avg Allele Dosage"] = np.nan
filestat["Avg Score"] = ""

for filename in os.listdir("PRS/"):
    if filename.endswith(".sscore"):
        score = pd.read_csv("PRS/"+filename,sep="\t")
        tmp = filename.rsplit( ".", 1)[0]


        filestat.loc[filestat["PGS ID"] == tmp,"Allele Count"] = score["ALLELE_CT"]
        filestat.loc[filestat["PGS ID"] == tmp,"Avg Allele Dosage"] = score["NAMED_ALLELE_DOSAGE_SUM"].mean()
        filestat.loc[filestat["PGS ID"] == tmp,"Avg Score"] = score["SCORE1_AVG"].mean()

filestat.to_csv("PRS_sumstats.txt", index=False,sep="\t",quoting = csv.QUOTE_NONE, escapechar = "")
filestat.fillna(0)
catstat = filestat.groupby(["Trait Name"]).mean()
catstat.to_csv("PRS_categorysumstats.txt", index=True,sep="\t",quoting = csv.QUOTE_NONE, escapechar = "")