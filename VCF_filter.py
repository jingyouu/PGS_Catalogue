import os
import sys

plink = "../plink/plink2.0/"
vcf_file = "../eMERGE/merged_vcf_gz/chr22.dose.emerge_ids.consented.merged.vcf.gz"
maf = 0.1
hwe = 0.000001
rs = 0.8

command = plink + "plink2 --vcf " + vcf_file + " --maf " + str(maf) + " --hwe " + str(hwe) + " --minimac3-r2-filter " + str(rs) + " --make-bed --out VCF/chr22.dose.emerge_ids.consented.merged"

os.system(command)



