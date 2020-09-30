import requests
import json
import wget

url = "https://www.pgscatalog.org/rest/score/all?limit=30&offset=20"
resp = requests.get(url,stream=True)

data = resp.json()
     
with open("coverageFile.txt","a") as f:
     
    for i in range(len(data['results'])):
        tmp_dict = data['results'][i]
        #trait 
        f.write(tmp_dict['trait_reported'].encode('utf-8')+'\t')
        #number of snps
        f.write(tmp_dict['id']+'\t')
        #number of vairants
        f.write(str(tmp_dict['variants_number']))
        f.write("\n")

        #download score files
        score_url = tmp_dict['ftp_scoring_file']
        wget.download(score_url,"PGS/")

 
