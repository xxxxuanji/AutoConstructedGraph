#!/usr/bin/env python
# coding: utf-8


import os
import time

import pandas as pd
from pandas import DataFrame
import argparse
import numpy as np
parser = argparse.ArgumentParser(description='文件位置')
# parser.add_argument('--re_file', type=str,  default="re_outputs_1", help='输入re结果位置')
parser.add_argument('--re_file1', type=str,  default="./re_output/cg/affects-expression", help='输入re结果位置')
parser.add_argument('--re_file2', type=str,  default="./re_output/cg/agonism", help='输入re结果位置')
parser.add_argument('--re_file3', type=str,  default="./re_output/cg/antagonism", help='输入re结果位置')
parser.add_argument('--re_file4', type=str,  default="./re_output/cg/binding", help='输入re结果位置')
parser.add_argument('--re_file5', type=str,  default="./re_output/cg/decreases-expression", help='输入re结果位置')
parser.add_argument('--new_paper_dir',type=str,required=True)

args = parser.parse_args()
# parser = argparse.ArgumentParser(description='文件位置')
# parser.add_argument('--result_file', type=str,  default="fileout/test_results.tsv", help='输入预测结果')
# parser.add_argument('--entity_file', type=str,  default="fileout/paperword.tsv", help='输入实体文件')
# parser.add_argument('--fileout_dir', type=str,default='fileout/data1.tsv',help='输出文件位置')
# args = parser.parse_args()




# results = pd.read_csv(args.re_file+"/test_results.tsv",sep='\t',header = None)
entities_relations=[]
file_value=[]
try:
    results1 = pd.read_csv(args.re_file1+"/test_results.tsv",sep='\t',header = None)
    results2 = pd.read_csv(args.re_file2+"/test_results.tsv",sep='\t',header = None)
    results3 = pd.read_csv(args.re_file3+"/test_results.tsv",sep='\t',header = None)
    results4 = pd.read_csv(args.re_file4+"/test_results.tsv",sep='\t',header = None)
    results5 = pd.read_csv(args.re_file5+"/test_results.tsv",sep='\t',header = None)    
    files = pd.read_csv('./new_about/ch_ge/test.tsv',sep='\t')

    for i in range(len(results1.iloc[:,0])):
        lit = list([results1.iloc[i,1],results2.iloc[i,1],results3.iloc[i,1],results4.iloc[i,1],results5.iloc[i,1]])
        re = max(lit)
        if re>0.5:
            n = lit.index(re)
            if n == 0:
                entitie_relation = [files.iloc[i,2],"affects-expression",files.iloc[i,3],str(re)]
            if n == 1:
                entitie_relation = [files.iloc[i,2],"agonism",files.iloc[i,3],str(re)]
            if n == 2:
                entitie_relation = [files.iloc[i,2],"antagonism",files.iloc[i,3],str(re)]
            if n == 3:
                entitie_relation = [files.iloc[i,2],"binding",files.iloc[i,3],str(re)]
            if n == 4:
                entitie_relation = [files.iloc[i,2],"decreases-expression",files.iloc[i,3],str(re)]
            file_value.append(files.iloc[i,2]+files.iloc[i,3])
            entities_relations.append(",".join(entitie_relation))


    duplicates_ids=[]
    ids=[]
    for i in np.unique(file_value):
        id = np.where(np.array(file_value) == i)
        if len(id[0])>1:
            duplicates_ids.append(id[0])
        else:
            ids.append(id[0].tolist()[0])
    d_id=[]
    for duplicates_id in duplicates_ids:
        maxid = 0
        max= 0
        for id in duplicates_id:
            ii = entities_relations[id].split(',')
            d = float(ii[3])
            if d > max:
                max = d
                maxid = id
        d_id.append(maxid)

    ids=sorted(ids+d_id)

    start_list=[]
    guanxi_list=[]
    end_list=[]
    for i in ids:
        ii = entities_relations[i].split(",")
        start_list.append(ii[0])
        guanxi_list.append(ii[1])
        end_list.append(ii[2])
    c = {"start":start_list,"relation":guanxi_list,"end":end_list}


    # results = pd.read_csv(args.entity_file,sep='\t',header = None)
    # results = pd.read_csv(args.files_file,sep='\t',header = None)

    # print(results[1])



    # entities_all1=[]
    # entities_all2=[]
    # entities_all4=[]
    # entities_all=[]

    # wrong = ['and','low','high','can','has','age','non']
    # for i,call in enumerate(results[1]):
    #     if(files.iloc[i,2] in wrong or files.iloc[i,3] in wrong):
    #         continue
    #     # if call > 0.1:#应为0.6
    #     #     entities = [files.iloc[i,2],files.iloc[i,3]]
    #     #     entities_all1.append(entities)
    #     # if call > 0.2:#应为0.6
    #     #     entities = [files.iloc[i,2],files.iloc[i,3]]
    #     #     entities_all2.append(entities)
    #     # if call > 0.4:#应为0.6
    #     #     entities = [files.iloc[i,2],files.iloc[i,3]]
    #     #     entities_all4.append(entities)
    #     if call > 0.6:#应为0.6
    #         entities = [files.iloc[i,2],files.iloc[i,3]]
    #         entities_all.append(entities)
    # print(len(entities_all))

    # for i,call in enumerate(results2[1]):
    #     if call > 0.4:#应为0.6
    #         entities = [files.iloc[i][2],files.iloc[i][3]]
    #         entities_all2.append(entities)




    a2b = DataFrame(c) #生成相应datafrme
    # a2b.insert(1,":TYPE",'gene_gene')#插入关系名字

    # a2b2 = DataFrame(entities_all2)
    # a2b2.insert(1,":TYPE",'chemical_disease')
    # a2b2.columns=[":START_ID",":TYPE",":END_ID"]



    # a2b.to_csv(args.fileout_dir, index=False,header=None,sep='\t')
    a2b.to_csv(args.new_paper_dir+'/ch_ge_data.tsv', index=False,sep='\t')
    # a2b.to_csv('about/cddata1.tsv', index=False,sep='\t')

    # a2b2.to_csv('about/'+date+'/data2.tsv', index=False,sep='\t')
    # a2b2.to_csv('about/data2.tsv', index=False,sep='\t')
except:
    a2b = DataFrame([]) #生成相应datafrme
    a2b.to_csv(args.new_paper_dir+'/ch_ge_data.tsv', index=False,sep='\t')
print('done')

