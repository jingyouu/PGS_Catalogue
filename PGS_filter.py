import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Filter PGS file based on params')
parser.add_argument('--i', type=str, help='Input dir for files to be filter')
parser.add_argument('--hg', type=int, help='Genome build version')
parser.add_argument('--o', type=str, help='Output dir for files filtered')
args = parser.parse_args()

os.chdir(args.i)
files = os.listdir(os.curdir)
files.sort()

with open("coverageFile.txt","a") as f:

    for filename in files:  
        
        with open (filename) as comment:

            lines = comment.readlines()

            if "hg19" in lines[4] or "GRCh37" in lines[4]:
                output = args.o + "hg19/"+filename
            elif "hg18" in lines[4] or "GRCh36" in lines[4]:                
                output = args.o + "QC/hg18/"+filename
            elif "hg38" in lines[4] or "GRCh38" in lines[4]:
                output = args.o + + "QC/hg38/"+filename
            else:
                output = args.o +filename

        
        data = pd.read_csv(filename,comment='#',sep='\t',engine='python')

        f.write(str(filename)+'\t')
        f.write(str(data.shape[0])+'\t')

        if not (data.columns.contains('effect_allele') and data.columns.contains('reference_allele')):
            f.write('No reference allele')
            f.write('\n')
            continue
                     
        if data.columns.contains('chr_position'):
            data["bp"] = data["chr_name"].astype(str) + ":" + data["chr_position"].astype(str)
            data = data[["bp","effect_allele","effect_weight","reference_allele"]]
            output = args.o + filename
        elif data.columns.contains('rsID'):
            data = data[["rsID","effect_allele","effect_weight","reference_allele"]]
        

        #remove 3+ allele in effect and reference cols
        data = data[(data['effect_allele'].str.len()<4) & (data['reference_allele'].str.len()<4)]
        f.write(str(data.shape[0])+'\t')

        #remove ambiguous allele                                                
        data.drop(data[(data['effect_allele'] == 'C') & (data['reference_allele']=='G')].index,inplace=True)
        data.drop(data[(data['effect_allele'] == 'G') & (data['reference_allele']=='C')].index,inplace=True)
        data.drop(data[(data['effect_allele'] == 'A') & (data['reference_allele']=='T')].index,inplace=True)
        data.drop(data[(data['effect_allele'] == 'T') & (data['reference_allele']=='A')].index,inplace=True)
        
        f.write(str(data.shape[0]))
        f.write('\n')

        data.to_csv(output, index=False,header=False,sep="\t")  
        