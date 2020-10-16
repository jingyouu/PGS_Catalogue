import os
import sys
import argparse

hg19_file = "/home/jy3035/project/map/hg19-151.txt"
hg38_file = "/home/jy3035/project/map/hg38-151.txt"
hg18_file = "/home/jy3035/project/map/hg18-130.txt"

parser = argparse.ArgumentParser(description='Genome build from rsID to bp')
parser.add_argument('--i', type=str, help='Input dir for files to be build')
parser.add_argument('--hg', type=int, help='Genome build version')
parser.add_argument('--o', type=str, help='Output dir for files built')
args = parser.parse_args()

files = os.listdir(args.i)
files.sort()

if args.hg == 18:
    hg_file = hg18_file
elif args.hg == 19:
    hg_file = hg19_file
elif args.hg == 38:
    hg_file = hg38_file
else:
    sys.exit("No available genoume build version")

for filename in files:  
    
    os.system("awk 'NR==FNR{a[$2]=$1;next} {$1=a[$1];}1' " + hg_file + " "+ filename + " > " + args.o + filename)