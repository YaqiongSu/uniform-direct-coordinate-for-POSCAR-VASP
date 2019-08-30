#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright: Yaqiong Su, Eindhoven, 29th, August, 2019
"""
import numpy as np
import datetime
import time
import linecache as lce
import shutil

######   timing   ######
start = time.time()
print '********** uniform coordinate @ Yaqiong Su Eindhoven **********'
print 'is uniforming coordinate'
### current time ###
start_time = datetime.datetime.now()
print "Start time:       " + start_time.strftime('%Y.%m.%d-%H:%M:%S')

with open('POSCAR','rb') as f:
    lines = f.readlines()
    count = len(lines)
    print "total rows:", count

#shutil.copy('POSCAR','coor')

f0 = open('coor','wb')
for i in range(1,9):
    linei = 'line'+str(i)
    linei = lce.getline('POSCAR',i)
    locals()['line'+str(i)] = linei
    f0.write(linei)        
for i in range(9,count+1):
    linei = 'line'+str(i)
    linei = lce.getline('POSCAR',i)
    locals()['line'+str(i)] = linei
#    print linei
    line = linei.split()
    for x in range(len(line)):
        if float(line[x]) < 0:
            line[x] = float(line[x]) + 1
#            line[x] = round(line[x],16)
            line[x] = '{:.16f}'.format(line[x])
        elif float(line[x]) > 1:
            line[x] = float(line[x]) - 1
#            line[x] = round(line[x],16)
            line[x] = '{:.16f}'.format(line[x])
    f0.write('%s %s %s'%(line[0], line[1], line[2]))
    f0.write('\n')
f0.close()

###### pick up the selected atoms ######
f2 = open('pick','wb')
for i in range(1,3):
    linei = 'line'+str(i)
    linei = lce.getline('coor',i)
    locals()['line'+str(i)] = linei
    f2.write(linei)
for i in range(3,6):
    linei = 'line'+str(i)
    linei = lce.getline('coor',i)
    locals()['line'+str(i)] = linei    
    line = linei.split()
    linea = list(map(float,line))      
#    for x in range(len(linea)):
#        linea[x] = linea[x]*0.25
#        linea[x] = '{:.16f}'.format(linea[x])
#         linea[0] = linea[0]*0.25
#         linea[1] = linea[1]
#         linea[2] = linea[2]
    linea[0] = linea[0]*0.25
    linea[1] = linea[1]
    linea[2] = linea[2]
    f2.write('%s %s %s'%(linea[0], linea[1], linea[2]))
    f2.write('\n')
for i in range(6,7):
    linei = 'line'+str(i)
    linei = lce.getline('coor',i)
    locals()['line'+str(i)] = linei
    f2.write(linei)
for i in range(7,8):
    linei = 'line'+str(i)
    linei = lce.getline('coor',i)
    locals()['line'+str(i)] = linei    
    line = linei.split()
    linea = list(map(float,line))        
    for x in range(len(linea)):
        linea[x] = linea[x]*0.25
        linea[x] = '{:.0f}'.format(linea[x])
    f2.write('%s %s'%(linea[0], linea[1]))
    f2.write('\n') 
for i in range(8,9):
    linei = 'line'+str(i)
    linei = lce.getline('coor',i)
    locals()['line'+str(i)] = linei
    f2.write(linei)
for i in range(9,count+1):
    linei = 'line'+str(i)
    linei = lce.getline('coor',i)
    locals()['line'+str(i)] = linei
    nums = linei.split()
    nums = list(map(float,nums)) 
#    nums = [nums[a] for a in range(len(nums))]
#    nums = [float(x) for x in nums]
#    nums = ['{:.16f}'.format(float(x)) for x in nums]
    if nums[0] < 0.25:
#        for x in range(len(nums)):
#            nums[x] = nums[x]
#            nums[x] = '{:.16f}'.format(nums[x])
        nums[0] = nums[0]*4
        nums[1] = nums[1]
        nums[2] = nums[2]
        f2.write('%s %s %s'%(nums[0], nums[1], nums[2]))
        f2.write('\n')
f2.close()
         
##########   timing   #############
stop=time.time()
print("running time:     " + str(stop-start) + " seconds")
terminal_time = datetime.datetime.now()
print "Terminal time:    " + terminal_time.strftime('%Y.%m.%d-%H:%M:%S')
print 'coordinate has been uniformed'
print '********** uniform coordinate @ Yaqiong Su Eindhoven **********'