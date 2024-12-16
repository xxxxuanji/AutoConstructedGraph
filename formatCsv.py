import csv
with open('all_data/graph.csv','r') as f1:
    with open('all_data/graph_new.csv','w') as f2:
        writer=csv.writer(f2)
        reader=csv.reader(f1)
        for line in reader:
            if(len(line)==3):
                line.append('Old_2022/12/30')
            writer.writerow(line)