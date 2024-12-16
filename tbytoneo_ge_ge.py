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
    t = pd.read_csv("./new_about/genes.tsv",sep='\t',header = None)

    l = list(t.iloc[:,0].values)
    num_list = ['ge'+str(i) for i in range(len(l))]
    # name_dict = dict(zip(num_list,l))
    name_list_f = dict(zip(l,num_list))

    spo = pd.read_csv(args.new_paper_dir+'/ge_ge_data.tsv',sep='\t')

    ges = spo["start"].unique().tolist()
    gee = spo["end"].unique().tolist()
    spo['date']=args.date
    # date = time.strftime('%Y%m%d',time.localtime(time.time()))

    # diids = ['ges'+date+'-'+str(a) for a in range(len(ges))]
    # geids = ['ge'+date+'-'+str(a) for a in range(len(gee))]

    gesids = [name_list_f[a] for a in ges]
    geeids = [name_list_f[a] for a in gee]

    gesnodes = pd.DataFrame({":ID":gesids,":TYPE":'Gene','name':ges})
    geenodes = pd.DataFrame({":ID":geeids,":TYPE":'Gene','name':gee})
    spo_encoded=spo.copy()
    spo_encoded['start'] = spo['start'].map(lambda x :gesnodes[gesnodes['name']==x][':ID'].iloc[0] )
    spo_encoded['end'] = spo['end'].map(lambda x :geenodes[geenodes['name']==x][':ID'].iloc[0] )

    spo_encoded.to_csv('./new_about/ge_ge/edges_encoded.csv',index=None)
    spo.to_csv('./new_about/ge_ge/edges.csv',index=None)
    nodes = pd.concat([gesnodes,geenodes],ignore_index=True)
    nodes.to_csv('./new_about/ge_ge/nodes.csv',index=None)
except:
    pd.DataFrame([]).to_csv('./new_about/ge_ge/edges.csv',index=None)
    pd.DataFrame([]).to_csv('./new_about/ge_ge/nodes.csv',index=None)
    print('done')






