import argparse
import os
import numpy as np
import pandas as pd
import time
import csv


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("hallmarks_files_path")
# args = parser.parse_args()
# print(args.hallmarks_files_path)# 打印传入的参数,特征标记

# hallmarks_filename=args.hallmarks_files_path ######传入的文件名


# t = pd.read_csv("./100_about/chnes.tsv",sep='\t',header = None)
# l = list(t.iloc[:,0].values)
# num_list = ['ch'+str(i) for i in range(len(l))]
# name_dict = dict(zip(num_list,l))
# name_list_f = dict(zip(l,num_list))
# spo = pd.read_csv('./100_about/20230622/ch_di_data.tsv',sep='\t')

# ch = spo[":START_ID"].unique().tolist()
# di = spo[":END_ID"].unique().tolist()

# chids = [name_list_f[a] for a in ch]
# diids = [name_list_f[a] for a in di]
parser = argparse.ArgumentParser(description='文件位置')
parser.add_argument('--date',type=str,default='2024/11/21',required=False)
args=parser.parse_args()
fileName = ["./new_about/ch_di/edges.csv","./new_about/ch_ge/edges.csv","./new_about/di_ge/edges.csv","./new_about/ge_ge/edges.csv"]
all_path=[]
for fn in fileName:
    try:
        t = pd.read_csv(fn,sep=',')
        all_path.append(t)
    except:
        continue
all = pd.concat(all_path,ignore_index=False)
all.to_csv("test.csv",index=None)
fd = open("test.csv","r")
# print(fd.readlines)



dir='all_data'
if not os.path.exists(dir):
    os.makedirs(dir)
#fd1 = open("./edges.csv","w")
fd1 = open(dir+'/'+'edges_pubmed.csv',"a")
next(fd)
for line in fd.readlines():
    datas=line.split(',')
    line=','.join(datas[0:3])
    line+='\n'
    fd1.write(line.replace('"',''))
    
fileName = ["./new_about/ch_di/nodes.csv","./new_about/ch_ge/nodes.csv","./new_about/di_ge/nodes.csv","./new_about/ge_ge/nodes.csv"]
all_path=[]
for fn in fileName:
    try:
        t = pd.read_csv(fn)
        all_path.append(t)
    except:
        continue
all = pd.concat(all_path)
all.to_csv("test.csv",index=None)
fd = open("test.csv","r")
# print(fd.readlines)
fd1 = open("nodes.csv","w")
for line in fd.readlines():
    fd1.write(line.replace('"',''))
fd1.close()




t = pd.read_csv("./nodes.csv")

# t.drop_duplicates(subset=['name'], keep='first', inplace=False)
# print(t.iloc[:,0].values)
kk_jihe = set()
for i in t.iloc[:,:].values:
    kk_jihe.add(tuple(i))
id_list = []
type_list =[]
entity_list =[]
date_list=[]
nodes_dic={}
chemical_nodes_count=0
disease_nodes_count=0
gene_nodes_count=0
with open('./all_data/nodes_pubmed.csv','r') as f:
    reader=csv.reader(f)
    for line in reader:
        if line[1]=='Chemical':
            chemical_nodes_count+=1
        elif line[1]=='Disease':
            disease_nodes_count+=1
        else:
            gene_nodes_count+=1
        nodes_dic[line[0]]=(line[1],line[2])
key_set=set(nodes_dic.keys())
for i in kk_jihe:
    ii = np.array(i)
    # if ii[0] not in key_set:
    #     if 'ge' in ii[0]:
    #         ii[0]='ge'+str(gene_nodes_count)
    #         gene_nodes_count+=1
    #     elif 'ch' in ii[0]:
    #         ii[0]='ch'+str(chemical_nodes_count)
    #         chemical_nodes_count+=1
    #     else:
    #         ii[0]='di'+str(disease_nodes_count)
    #         disease_nodes_count+=1
    id_list.append(ii[0])
    type_list.append(ii[1])
    entity_list.append(ii[2])
    date_list.append(args.date)
c = {"id":id_list,"type":type_list,"entity":entity_list}
b_dataframe = pd.DataFrame(c)
#b_dataframe.to_csv('./temp.csv',index = None)#############################
b_dataframe.to_csv('./all_data/nodes_pubmed.csv',mode='a',index = None,header=False)
