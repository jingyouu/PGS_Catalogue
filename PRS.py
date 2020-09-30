import os

os.chdir('PRS/')
plink = "../../plink/plink2.0/"
b_file = "../VCF/chr22.dose.emerge_ids.consented.merged"
files = os.listdir("../PGS/")
files.sort()

#calculate prs score
for score_file in files:
    command = plink + "plink2 --bfile " + b_file + " --score ../PGS/" + score_file + " 1 3 2" + " --out " + score_file.rsplit( ".", 1 )[0]
    os.system(command)
