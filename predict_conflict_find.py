from pysat.solvers import Glucose3
from pysat.solvers import Solver
from pysat.formula import CNF
import csv
import time
import pandas as pd
import numpy as np
from tqdm import tqdm

old=[]                          ###old triples
no_conflict=[]                  ###the unconflict triples that we chose preliminarily
conflict=[]                     ###conflict triples

def read_triplet_from_csv(file_path,have_head=False):
    triplets=[]
    with open(file_path,'r') as f_c:
        data=csv.reader(f_c)
        if have_head==True:
            next(data) #空第一行
        for item in data:
            triplets.append(item)

              
    return triplets
    

def get_x1(e1,e2):#判断两个三元组头实体是否相等，相等x1为1，不等为-1
    if e1==e2:
        return 1
    else:
        return -1

def get_x2(e1,e2):#判断两个三元组尾实体是否相等，相等x2为2，不等为-2
    if e1==e2:
        return 2
    else:
        return -2
    
def get_x3_x4(e1,e2):#判断两个三元组关系是否相等
    if e1==e2:
        return 3,-4 #x3为真，x4为假，两个三元组只存在一种关系
    else:
        return 3,4 #


def check_consistency(old_triplets, new_triplets,conflict_path,notconflict_path,mode):
    ###set them to global that we can continuely to add or delete items in or from them
    global old                  
    global no_conflict
    global conflict
    time_result = 0
    old=[item[0:3] for item in old_triplets]
    g = Glucose3(bootstrap_with=[[1],[2],[3],[4]], use_timer = True)
    count=0
    for triplet in tqdm(new_triplets):
        #print('现在处理第%s个新三元组'%count)
        count+=1
        flag_write_new=False
        #print('1')
        
        head, relation, tail = triplet[0], triplet[1], triplet[2]
       
        #定义一个SAT求解器  -(x1^x2^x3^x4)
        #   x1:equal(h1,h2)    x2:equal(t1,t2)   x3:r1(h1,t1)   x4:r2(h2,t2)

        for exist_triplet in old_triplets:
            #print('2')
            
            #如果存在重复三元组，则跳过
            if triplet[0]==exist_triplet[0] and triplet[1]==exist_triplet[1] and triplet[2]==exist_triplet[2]:
                break
            
            assumption=[]
            old_head,old_relation,old_tail=exist_triplet[0], exist_triplet[1], exist_triplet[2]
            x1=get_x1(old_head,head)
            assumption.append(x1)
            x2=get_x2(old_tail,tail)
            assumption.append(x2)
            x3,x4=get_x3_x4(old_relation,relation)
            assumption.append(x3)
            assumption.append(x4)
            result=g.solve(assumption)
            if result:
                flag_write_new=True
                print("存在冲突,有解")
                with open(conflict_path, 'a+') as file:
                    #file.write('头实体,关系,尾实体,标签\n')
                    # 写入旧三元组
                    if len(exist_triplet)==3:
                        file.write(f'{exist_triplet[0]},{exist_triplet[1]},{exist_triplet[2]},Old\n')
                        conflict.append([exist_triplet[0],exist_triplet[1],exist_triplet[2],'Old'])
                    else:
                        file.write(f'{exist_triplet[0]},{exist_triplet[1]},{exist_triplet[2]},{exist_triplet[3]}\n')
                        conflict.append([exist_triplet[0],exist_triplet[1],exist_triplet[2],exist_triplet[3]])
                    
                    # 写入新三元组
                    if mode=="linkpredict":
                        file.write(f'{triplet[0]},{triplet[1]},{triplet[2]},Prediction\n')
                        conflict.append([triplet[0],triplet[1],triplet[2],'Prediction']) 
                    else:
                        file.write(f'{triplet[0]},{triplet[1]},{triplet[2]},PubMed\n') 
                        conflict.append([triplet[0],triplet[1],triplet[2],'PubMed'])
                #print(g.get_model())
            else:
                # print("没有冲突,无解")                
                #没有冲突就把链接预测和pubmed文件写入
                if flag_write_new==False:
                    with open(notconflict_path, 'a+') as file:
                        if mode=="linkpredict":
                            #file.write(f'{triplet[0]},{triplet[1]},{triplet[2]},Prediction\n') 
                            no_conflict.append([triplet[0],triplet[1],triplet[2],'Prediction'])
                        else:
                            #file.write(f'{triplet[0]},{triplet[1]},{triplet[2]},PubMed\n') 
                            no_conflict.append([triplet[0],triplet[1],triplet[2],'PubMed'])
                    flag_write_new=True
    print('{0:.10f}s'.format(g.time_accum()))
    
       
                
# 测试代码 
if __name__ == "__main__":

    # 调用函数读取CSV文件中的三元组数据
    file_path=("./all_data/subKG_LungCancer_decoded.csv")#旧三元组
    linkpredict_path= ("./all_data/linkpredict_decoded.csv")  # 链接预测CSV文件路径
    conflict_file_path = './all_data/link_conflict.csv' #冲突文件路径
    no_conflict_path='./all_data/link_not_conflict.csv' #不冲突文件路径

    #######清空文件
    with open(conflict_file_path,'w') as f:
        f.seek(0)
        f.truncate()
    with open(no_conflict_path,'w') as f:
        f.seek(0)
        f.truncate()



    old_triplets = read_triplet_from_csv(file_path,True)
    linkpredict_triplets = read_triplet_from_csv(linkpredict_path)
    
    
    check_consistency(old_triplets,linkpredict_triplets ,conflict_file_path,no_conflict_path,"linkpredict") 
    
    #check_consistency(old_triplets, pubmed_triplets ,conflict_file_path,no_conflict_path,"pubmed") 

    #print(no_conflict)
    no_conflict_copy=no_conflict.copy()
    for item in no_conflict:                          ####delete the item in old data but in unconflict data
        if (item[0:3] in [e1[0:3] for e1 in old]):
            no_conflict_copy.remove(item)
            #print('removed '+str(item))
    
    for item in no_conflict:                          ####delete the item in conflict data but in unconflict data
        if (item[0:3] in [e2[0:3] for e2 in conflict]):
            no_conflict_copy.remove(item)
            #print('removed '+str(item))

    with open(no_conflict_path,'w') as file:
        writer=csv.writer(file)
        writer.writerows(no_conflict_copy)


    
    """ date=time.strftime('%Y%m%d',time.localtime(time.time()))
    path ='./about/'+date
    if not os.path.exists(path):
        os.makedirs(path)
        print('文件夹创建完成  '+path)

   # a2b.to_csv(args.fileout_dir, index=False,header=None,sep='\t')
    a2b.to_csv('about/'+date+'/gene_gene_data1.tsv', index=False,sep='\t')
    a2b.to_csv('about/gene_gene_data1.tsv', index=False,sep='\t')
 """


