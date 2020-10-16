import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Filter VCF files')
parser.add_argument('--maf', type=str, help='Maf threshold')
parser.add_argument('--hwe', type=int, help='hwe threshold')
parser.add_argument('--rs', type=str, help='rs threshold')
parser.add_argument('--p', type=str, help='Plink path')
parser.add_argument('--i', type=str, help='Input namefor files to be filter')
parser.add_argument('--o', type=str, help='Output dir for files filtered')
args = parser.parse_args()

plink = args.p
maf = args.maf
hwe = args.hwe
rs = args.rs

for i in range(1,22):
    vcf_file = "../eMERGE/merged_vcf_gz/chr"+ str(i) +".dose.emerge_ids.consented.merged.vcf.gz"
    command = plink + "plink2 --vcf " + vcf_file + " --maf " + str(maf) + " --hwe " + str(hwe) + " --minimac3-r2-filter " + str(rs) + " --make-bed --out " args.o + str(i) +".dose.emerge_ids.consented.merged"
    os.system(command)


