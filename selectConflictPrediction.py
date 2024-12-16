import csv
all_predict=set()
with open('all_data/linkpredict_decoded.csv','r') as f:
    reader=csv.reader(f)
    for line in reader:
        all_predict.add((line[0],line[1],line[2]))
with open('all_data/subKG_LungCancer_decoded1.csv','r') as f:
    reader=csv.reader(f)
    for line in reader:
        if len(line)==4 and (line[0],line[1],line[2]) in all_predict:
            all_predict.remove((line[0],line[1],line[2]))
with open('all_data/conflict_linkpredict.csv','w') as f:
    writer=csv.writer(f)
    for line in all_predict:
        writer.writerow(line)
