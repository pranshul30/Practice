import csv
 
data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
 ]


try:
    with open ('packing_list.csv','r') as file:
     r=csv.reader(file)
     for row in file:
         print(row)
         
except: 
    print('Error File not found now we will create one')       
    with open('packing_list.csv','w') as f:
        w=csv.writer(f)
        w.writerows(data)

            