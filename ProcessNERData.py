file1='/home/tby/ln/NewGraph/biobert-master/datasets/NER/BC4CHEMD/test.tsv'
file2='/home/tby/ln/NewGraph/biobert-master/datasets/NER/BC2GM/test.tsv'
file3='/home/tby/ln/NewGraph/biobert-master/datasets/NER/NCBI-disease/test.tsv'
file1_reader=open(file1,'r')
file2_reader=open(file2,'r')
file3_reader=open(file3,'r')
file4='/home/tby/ln/NewGraph/biobert-master/datasets/NER/ComprehensiveData/test.tsv'
file4_writer=open(file4,'w')
import  csv
csv.field_size_limit(2000000)
from tqdm import tqdm
readers=[file1_reader,file2_reader,file3_reader]
suffixes=['Chemical','Gene','Disease']
for i in range(3):
    for line in readers[i]:
        line=line.split('\t')
        if(len(line)<2):
            file4_writer.write('\n')
            continue
        if('O' not in  line[1]):
            line[1]=line[1].removesuffix('\n')+'-'+suffixes[i]+'\n'
        file4_writer.write(line[0]+'\t'+line[1])
    readers[i].close()
file4_writer.close()
    