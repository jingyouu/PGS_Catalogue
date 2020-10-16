import os
import argparse

parser = argparse.ArgumentParser(description='PRS calculation with plink')
parser.add_argument('--b', type=str, help='Bfiles to be calculate')
parser.add_argument('--s', type=int, help='Input dir of score files')
parser.add_argument('--o', type=str, help='Output dir for files filtered')
parser.add_argument('--p', type=str, help='Plink path')
args = parser.parse_args()

os.chdir(args.o)
plink = args.p
b_file = args.b
files = os.listdir(args.s)
files.sort()

#calculate prs score
for score_file in files:
    command = plink + "plink2 --bfile " + b_file + " --score ../PGS/QC/" + score_file + " 1 2 3" + " --out " + score_file.rsplit( ".", 1 )[0]
    os.system(command)


