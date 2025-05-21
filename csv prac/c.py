import csv
s=0
path='bestseller.csv'
with open(path,'r',encoding='utf-8')as f:
    c=csv.reader(f)
    f.readline()
    
    for row in c:
        c=float(row[4])
        if(c>s):
         s=c
         best=row
        
    output='b.csv'
    with open(output,'w',newline='')as o:
        k=csv.writer(o)
        k.writerow(['Book','Author','Sales'])
        k.writerow([best[0],best[1],best[4]])
        print(output)   