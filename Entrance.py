import argparse
from Bio import Entrez,Medline
import http.client
from tqdm import tqdm
parser = argparse.ArgumentParser(description='Entrance')
parser.add_argument('--date1', type=str, required=True, help='the form of date should be like 2024/11/12')
parser.add_argument('--date2',type=str,required=True)
parser.add_argument('--new_paper_dir',type=str,required=False)
parser.add_argument('--mesh_file', type=str, required=False, default='./Entries/LungCancer.txt', help='mesh terms file')
args=parser.parse_args()
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
abset=set()
titleset=set()
Entrez.email = "919474823@qq.com"
import os
with open(args.mesh_file,'r') as f:
    lines=f.readlines()
    term=lines[0].split('\n')[0]+'[MeSH Terms]'
    lines.pop(0)
    for line in lines:
        term=term+' OR '+line.split('\n')[0]+'[MeSH Terms]'
term=term+' AND (('+args.date1+'[Date - Publication] : '+args.date2+'[Date - Publication]))'
handle = Entrez.esearch(db = 'pubmed', retmax=10000,term = term)
record_cd = Entrez.read(handle)
dir='new_about/'+''.join(args.date2.split('/'))
if not os.path.exists(dir):
    os.makedirs(dir)
paper_file=os.path.join(dir,'new_paper.txt')
f=open(paper_file,'w')
for i in tqdm(record_cd['IdList']):
    handle = Entrez.efetch(db="pubmed", id=i,
                           retmode="text", rettype="medline")
    record = Medline.read(handle)

    title = record["TI"]
    title = title.replace('[', '').replace('].', '')#去除标题中[]
    try:
        ab = record["AB"]
    except KeyError:
        continue
    # print(title)
    if title not in titleset:
        titleset.add(title)
        f.write(title + '\n')
    if ab not in abset:
        f.write(ab + '\n')
        abset.add(ab)
f.close()
count = int(record_cd["Count"])
print(count)