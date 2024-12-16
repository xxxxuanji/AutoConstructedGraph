import csv
# old_node=set()
# count=0
# with open('/home/tby/ln/NewGraph_Copy2/all_data/subKG_LungCancer_decoded1.csv','r')  as f:
#     reader=csv.reader(f)
#     for line in reader:
#         old_node.add(line[0])
#         old_node.add(line[2])
# with open('/home/tby/ln/NewGraph_Copy2/all_data/nodes_pubmed.csv','r') as  f:
#     reader=csv.reader(f)
#     next(reader)
#     for line in reader:
#         if  line[2] not in old_node:
#             count+=1
# print(count)
with open('/home/tby/lyc/buildNewKG/papers/sentence.txt','r') as f:
    
    for line in f.readlines():
        words=line.split(' ')
        if 'fluvoxamine'  in words and 'death' in words:
            print(line)
