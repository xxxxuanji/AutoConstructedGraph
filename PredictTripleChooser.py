import csv
import  random
from tqdm import  tqdm
def WriteWillPredictFile(predict_file_path,mesh_file,graph_file):
    test_set=set()
    nodes=set()
    relations=set()
    with open(graph_file,'r') as f:
        reader=csv.reader(f)
        
        for line in tqdm(reader):
            nodes.add(line[0])
            nodes.add(line[2])
            relations.add(line[1])
    with open(mesh_file,'r') as f:
        for line in f.readlines():
            node=line.split('\n')[0]
            if node in nodes:
                for relation in relations:
                    test_set.add((node,relation,node))
    with  open(predict_file_path,'w') as f:
        # num=60000
        # test_list=random.sample(list(test_set),num)
        test_list=list(test_set)
        for triple in tqdm(test_list):
            f.write(triple[0]+','+triple[1]+','+triple[2]+'\n')
        