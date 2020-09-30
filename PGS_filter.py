import os
import pandas as pd

os.chdir('PGS/')

files = os.listdir(os.curdir)
files.sort()

with open("QC/coverageFile.txt","a") as f:

    for filename in files:  
        
        data = pd.read_csv(filename,comment='#',sep='\t',engine='python')

        f.write(str(filename)+'\t')
        f.write(str(data.shape[0])+'\t')

        if not (data.columns.contains('effect_allele') and data.columns.contains('reference_allele')):
            f.write('No reference allele')
            f.write('\n')
            continue

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

        data.to_csv("QC/"+filename, index=False,header=False,sep="\t")  
    