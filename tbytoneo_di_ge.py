#!/usr/bin/env python
# coding: utf-8

import argparse
import pandas as pd
import time
parser = argparse.ArgumentParser(description='文件位置')
parser.add_argument('--new_paper_dir',default='new_about/20241112',type=str,required=False)
parser.add_argument('--date',type=str,required=True)
args=parser.parse_args()
try:
    t = pd.read_csv("./new_about/dines.tsv",sep='\t',header = None)

    l = list(t.iloc[:,0].values)
    num_list = ['di'+str(i) for i in range(len(l))]
    # name_dict = dict(zip(num_list,l))
    name_list_f = dict(zip(l,num_list))

    t1 = pd.read_csv("./new_about/genes.tsv",sep='\t',header = None)
    l1 = list(t1.iloc[:,0].values)
    num_list1 = ['ge'+str(i) for i in range(len(l1))]
    # name_dict = dict(zip(num_list,l))
    name_list_f1 = dict(zip(l1,num_list1))

    spo = pd.read_csv(args.new_paper_dir+'/di_ge_data.tsv',sep='\t')
    spo['date']=args.date
    di = spo["start"].unique().tolist()
    ge = spo["end"].unique().tolist()

    # date = time.strftime('%Y%m%d',time.localtime(time.time()))

    # diids = ['di'+date+'-'+str(a) for a in range(len(di))]
    # geids = ['ge'+date+'-'+str(a) for a in range(len(ge))]
    diids = [name_list_f[a] for a in di]
    geids = [name_list_f1[a] for a in ge]

    dinodes = pd.DataFrame({":ID":diids,":TYPE":'Disease','name':di})
    genodes = pd.DataFrame({":ID":geids,":TYPE":'Gene','name':ge})
    spo_encoded=spo.copy()
    spo_encoded['start'] = spo['start'].map(lambda x :dinodes[dinodes['name']==x][':ID'].iloc[0] )
    spo_encoded['end'] = spo['end'].map(lambda x :genodes[genodes['name']==x][':ID'].iloc[0] )

    spo_encoded.to_csv('./new_about/di_ge/edges_encoded.csv',index=None)
    spo.to_csv('./new_about/di_ge/edges.csv',index=None)
    nodes = pd.concat([dinodes,genodes],ignore_index=True)
    nodes.to_csv('./new_about/di_ge/nodes.csv',index=None)
except:
    pd.DataFrame([]).to_csv('./new_about/di_ge/edges.csv',index=None)
    pd.DataFrame([]).to_csv('./new_about/di_ge/nodes.csv',index=None)
    print('done')
print('done')






