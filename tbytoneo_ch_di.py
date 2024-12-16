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
    t = pd.read_csv("./new_about/chnes.tsv",sep='\t',header = None)
    l = list(t.iloc[:,0].values)
    num_list = ['ch'+str(i) for i in range(len(l))]
    # name_dict = dict(zip(num_list,l))
    name_list_f = dict(zip(l,num_list))

    t1 = pd.read_csv("./new_about/dines.tsv",sep='\t',header = None)
    l1 = list(t1.iloc[:,0].values)
    num_list1 = ['di'+str(i) for i in range(len(l1))]
    # name_dict = dict(zip(num_list,l))
    name_list_f1 = dict(zip(l1,num_list1))
    date=time.strftime('%Y%m%d',time.localtime(time.time()))
    spo = pd.read_csv(args.new_paper_dir+'/ch_di_data.tsv',sep='\t')
    spo['date']=args.date
    ch = spo["start"].unique().tolist()
    di = spo["end"].unique().tolist()

    # print(ch)
    # date = time.strftime('%Y%m%d',time.localtime(time.time()))

    # chids = ['ch'+'-'+str(a) for a in range(len(ch))]
    # diids = ['di'+'-'+str(a) for a in range(len(di))]
    chids = [name_list_f[a] for a in ch]
    diids = [name_list_f1[a] for a in di]

    chnodes = pd.DataFrame({":ID":chids,":TYPE":'Chemical','name':ch})
    dinodes = pd.DataFrame({":ID":diids,":TYPE":'Disease','name':di})
    spo_encoded=spo.copy()
    spo_encoded['start'] = spo['start'].map(lambda x :chnodes[chnodes['name']==x][':ID'].iloc[0] )
    spo_encoded['end'] = spo['end'].map(lambda x :dinodes[dinodes['name']==x][':ID'].iloc[0] )
    spo_encoded.to_csv('./new_about/ch_di/edges_encoded.csv',index=None)
    spo.to_csv('./new_about/ch_di/edges.csv',index=None)
    nodes = pd.concat([chnodes,dinodes],ignore_index=True)
    nodes.to_csv('./new_about/ch_di/nodes.csv',index=None)
except:
    pd.DataFrame([]).to_csv('./new_about/ch_di/edges.csv',index=None)
    pd.DataFrame([]).to_csv('./new_about/ch_di/nodes.csv',index=None)
print('done')







