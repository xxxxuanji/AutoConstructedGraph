import csv
def id2node(nodes_file,dict,entity_index):
    with open(nodes_file,'r') as f:
        reader=csv.reader(f)
        for  line  in reader:
            dict[line[0]]=line[entity_index]

def decode(dict,triples_file,decoded_file):
    with  open(triples_file,'r') as f1:
        with  open(decoded_file,'w') as f2:
            reader=csv.reader(f1)
            writer=csv.writer(f2)
            for line in reader:
                if len(line)<3:
                    print(line)
                    continue
                if(dict.get(line[0])!=None and  dict.get(line[2])!=None):
                    line[0]=dict[line[0]]
                    line[2]=dict[line[2]]
                    writer.writerow(line)
                else:
                    print(line)

if __name__ == "__main__":
    old_id2node={}
    pubmed_id2node={}
    id2node('all_data/nodes.csv',old_id2node,1)
    id2node('all_data/nodes_pubmed.csv',pubmed_id2node,2)
    decode(old_id2node,'all_data/subKG_LungCancer.csv','all_data/subKG_LungCancer_decoded.csv')