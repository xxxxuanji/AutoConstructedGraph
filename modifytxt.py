import csv
import re
import difflib
from difflib import SequenceMatcher
from tqdm import tqdm
from Bio import Entrez,Medline
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
abset=set()
titleset=set()
Entrez.email = "919474823@qq.com"
file='/home/tby/ln/NewGraph/biobert-master/datasets/RE/GNBR-v2/cd/alleviates/train.tsv'
label1='@DISEASE$'
label2='@CHEMICAL$'
replacedic={'@DISEASE$':'*',
            '@CHEMICAL$':'*',
            '/t':'',
            '-LRB-':'(',
            '-RRB-':')',
            '-LSB':'[',
            '-RSB':']',}
inputfile= open('./decoded_senteces','w')
with open(file,'r') as f:
    reader=csv.reader(f,delimiter='\t')
    count=0
    matched_sentence1=''
    matched_sentence2=''
    matched_sentence=[]
    for line in reader:
        text=line[0]
        if(text.count(label1)  == 1 and text.count(label2) == 1):
            for key,val in replacedic.items():
                text=text.replace(key,val)
                text=text.replace('_',' ',10)
            result_str=""
            inside_parentheses=False
            for char in text:
                if char == '(':
                    inside_parentheses = True
                elif char == ')':
                    inside_parentheses = False

                if inside_parentheses and char == ' ':
                    continue
                elif not inside_parentheses and char == ' ' and result_str[-1] == '(':
                    continue
                else:
                    result_str += char
            text=result_str
            handle = Entrez.esearch(db = 'pubmed', term =text )
            record_cd = Entrez.read(handle)
            if(len(record_cd['IdList'])>0):
                handle = Entrez.efetch(db="pubmed", id=record_cd['IdList'][0],
                                retmode="text", rettype="medline")
                record = Medline.read(handle)
                if('AB' in record):
                    ab=record['AB']
                    sentences=ab.split('.')
                    matched_sentence1=difflib.get_close_matches(text,sentences,1)
                if('TI' in record):
                    title=record['TI']
                    sentences=title.split('.')
                    matched_sentence2=difflib.get_close_matches(text,sentences,1)
                ratio1=(float)(SequenceMatcher(None,matched_sentence1[0],text).ratio()) if len(matched_sentence1)>0 else 0
                ratio2=(float)(SequenceMatcher(None,matched_sentence2[0],text).ratio()) if len(matched_sentence2)>0 else 0
                
                if(ratio1>ratio2):
                    matched_sentence=matched_sentence1
                else:
                    matched_sentence=matched_sentence2
                if len(matched_sentence) > 0:
                    words=matched_sentence[0].removeprefix(' ').split(' ')
                    encoded_words=text.split(' ')
                    try:
                        index1=encoded_words.index('*')
                        index2=encoded_words.index('*',index1+1)
                    except:
                        continue
                    if index1>=len(words) or index2>=len(words):
                        continue
                    encoded_words[index1]=words[index1]
                    encoded_words[index2]=words[index2]
                    decoded_sentence=' '.join(encoded_words)
                    print('%s:'%count)
                    print("original sentence:\t"+line[0])
                    print("decoded sentence:\t"+decoded_sentence)
                    inputfile.write('%s:'%count)
                    inputfile.write("original sentence:\t"+line[0])
                    inputfile.write("decoded sentence:\t"+decoded_sentence)
                    count+=1
inputfile.close()

        

