#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2020/2/7
by Charles Huang

Lab3 - Evaluate_Raccoon_Life
The whole program import data about a Raccoon from the txt file, transfer them
into a dictionary format, do calculation for new variable,then output them into
a new txt file.

"""
fin = open('/home/huan1460/ABE65100/03-working-with-files-in-python-CharlesWorgen/2008Male00006.txt','r')
lines=fin.readlines()
fin.close()
print(lines)
data = [0]*len(lines)

for lidx in range(len(lines)): # Import the data into a list
    data[lidx]= lines[lidx].strip().split(',')
    if lidx > 0 and lidx <15:
        data[lidx][3] = int(data[lidx][3])
        data[lidx][4:6] = map(float,data[lidx][4:6])
        data[lidx][8:15] = map(float,data[lidx][8:15])
   
 # Transfer the list into a dictionary   
keys = (lines[0].strip().split(','))
Data = dict()
for colum in range(len(keys)):
    Data[keys[colum]] = []
for colum in range(len(keys)):
    for lidx in range(len(data)):
        if lidx >0 and lidx <15:
            Data[keys[colum]].append(data[lidx][colum])

end_status = data[15] # The end status that does not fit in the dic

'''
Function used to calculate new variables
'''
def sum_list(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total
    
def mean_list(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    mean = total / len(list)    
    return mean

def distance(X,Y):
    list = [0]*(len(X))
    for i in range(len(X)):
        if i >0:
            list[i] = ((Y[i]-Y[i-1])**2+(X[i]-X[i-1])**2)**0.5
    return list        

'''
New variables
''' 
Data['Movement'] = distance(Data[' X'],Data[' Y'])      

aver_energy_level = mean_list(Data['Energy Level'])
location = [mean_list(Data[' X']),mean_list(Data[' Y'])]
total_dis = sum_list(Data['Movement'])

'''
Output - Header block
'''
fout = open("huan1460_Georges_life.txt","w")
line1 = "Raccoon name: George\n"
line2 = "Average location: %f, %f\n" %(location[0],location[1])
line3 = "Distance traveled: %f\n" % total_dis
line4 = "Average energy level: %f\n" %  aver_energy_level
line5 = "Raccoon end state: %s\n" % end_status
line6 = "\n"
fout.write(line1)
fout.write(line2)
fout.write(line3)
fout.write(line4)
fout.write(line5)
fout.write(line6)

'''
Oytput - data
'''
linedata = [0]*len(Data['Year'])
linehead = '\t'.join(keys)
for i in range(len(Data['Year'])):  
        linedata[i] = [str(Data['Year'][i]),str(Data['Day'][i]),
                str(Data['Time'][i]),str(Data[' X'][i]),
                str(Data[' Y'][i]),str(Data[' Asleep'][i]),
                str(Data['Behavior Mode'][i]),str(Data['Movement'][i])]
fout.write(linehead)
fout.write(line6)
for i in range(len(linedata)):
    fout.write('\t'.join(linedata[i]))
    fout.write(line6)

fout.close()    
 
'''
Metadata creating
'''       
fmeta =  open("huan1460_README.raccoon.txt","w")
linea= "The Evaluate_Raccoon_Life.py script can import a Raccoon behaviormodel from the 2008Male00006.txt file.\n"
lineb ="This script transfer all data into a dictionary format and contains function to calculate the average location, distance, average energy level of the raccoon.\n"
linec ="Then the script output the calculated result as well as original data into a new file called Georges_life.txt."
fmeta.write(linea) 
fmeta.write(lineb)  
fmeta.write(linec)
fmeta.close()       
    
