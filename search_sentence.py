keywords1='Nrf2'
keywords2='Lung Cancer'
words=['Nrf2','Lung Cancer']
with open('/home/tby/ln/NewGraph_Copy2/all_data/conflict.csv','r') as f:
    for line in f.readlines():
        if line[0] in words and line[2] in words:
            print(line)
# import csv
# with open('/home/tby/ln/NewGraph_Copy2/all_data/subKG_LungCancer_decoded2.csv','r') as f:
#     reader=csv.reader(f)
#     for line in reader:
#         if len(line) <3:
#             continue
#         if 'p53' in line[2] and 'adenocarcinoma' in line[0]:
#             print(line)