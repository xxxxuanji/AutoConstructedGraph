#import pandas as pd
import csv
# import nltk
from nltk.tokenize import sent_tokenize
# nltk.download('punkt')
# a = pd.read_csv("./1-12.12.csv")
# a["Abstract"].to_csv("new.csv",index=None,header=None)

# a = pd.read_csv("./new.csv")
# data = a.drop_duplicates(subset=None, keep=False, inplace=False)
# data.to_csv("./new.csv",index=None,header=None)

# fd = open("./new.csv","r",encoding="utf-8")
# ft = open("./new.txt","w",encoding="utf-8")
# for line in fd.readlines():
#     ft.write(line[1:-2]+"\n")

# fd = open("./new.txt","r",encoding="utf-8")
# ft = open("./last.txt","w",encoding="utf-8")
# for line in fd.readlines():
#     for s in line.strip().split(". ")[:-1]:
#         ft.write(s+"."+"\n")


# 运行standoff2coll.py之后运行一下然后手动删除双引号
# fd = open("./new_about/papper.tsv","r",encoding="utf-8")
# ft = open("./new_about/test.tsv","w",encoding="utf-8")
# for line in fd.readlines():
#         # t = line.replace('""	O',"")
#         # t1 = t.replace('_	O',"")
#         # if t2 =="\n":
#         #         line = t2.strip("\n")
#         ft.write(t1)


import argparse
import time
import re
# parser = argparse.ArgumentParser()
# parser.add_argument("print1_path")
# args = parser.parse_args()
# print(args.print1_path)# 打印传入的参数,特征标记

# hallmarks_filename=args.print1_path ######传入的文件名
parser = argparse.ArgumentParser(description='modify_paper')
parser.add_argument('--date', type=str, default='2024/11/12',required=False, help='the form of date should be like 2024/11/12')
args=parser.parse_args()
cop = re.compile("[^.^a-z^A-Z^0-9^' '^':']")###使用正则项，保留[大小写字母，数字，连字符-，小数点'.'，空格]
#####修改了输入的文件路径，ft是否需要修改询问步云？
fd = open('new_about/'+''.join(args.date.split('/'))+'/new_paper.txt',"r",encoding="utf-8")
ft = open("new_about/"+''.join(args.date.split('/'))+"/new_paper_clause.txt","w",encoding="utf-8")
for line in fd.readlines():
        # sent_data = line.split(". ")
        sent_data=sent_tokenize(line)
        for i in sent_data:
                if len(i)<500:
                        line_cop=cop.sub(" ", i)+'\n'#在i中找到非cop中的字符，并删掉（用空代替）
                        ft.write(line_cop)

                '''
                ft.write(line.replace('"','')
                .replace(':','').replace(';','').replace('/','')
                .replace('[','').replace(']','').replace('(','')
                .replace(')','').replace('.','').replace('-','')
                .replace('_','').replace('%','').replace('蝿','').replace(',',''))
                '''
# fd = open("./luanma.txt","rb")
# ft = open("./luanma1.txt","w",encoding="UTF-8")
# for line in fd.readlines():
#         ft.write(line)
# f = open(r'./luanma.txt','rb')
# f.seek(0,0)
# for each_line in f:
#     print(each_line.decode('utf-8'))
# f.close()



