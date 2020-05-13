import os
#import file
import numpy as np
#np.set_printoptions(suppress=False)

#input your file path
_file = input("INPUT FILE WITH FULL PATH:\n")

best_gflops = 0.00000
worst_gflops = 100.00000
best = []
worst = []
alllines = {}
#Read file
worst = []
with open(_file,'r',encoding = 'utf-8') as f:
    for line in f.readlines():
        if line[0] == 'W' and not 'Written' in line and not line == '':
            thisline = line.split()
            ident = "-".join(thisline[1:5])
            #print(ident)
            if ident in alllines.keys():
                alllines[ident].append([thisline[0],thisline[6]])
            else:
                alllines[ident] = [[thisline[0],thisline[6]]]
            #if thisline[1]
            if float(thisline[6])>best_gflops:
                best_gflops = float(thisline[6])
                best = list(thisline)
            if float(thisline[6])<worst_gflops:
                worst_gflops = float(thisline[6])
                worst = list(thisline)
#print(best)
#print(alllines)
print("==FIND BEST(FASTEST) ONE AS==")
print("T/V={}, N={}, NB={}, P={}, Q={}, RunningTime={}, best_Gflops={}".format(best[0],best[1],best[2],best[3],best[4],best[5],best[6]))
print("==FIND WORST(SLOWEST) ONE AS==")
print("T/V={}, N={}, NB={}, P={}, Q={}, RunningTime={}, best_Gflops={}".format(worst[0],worst[1],worst[2],worst[3],worst[4],worst[5],worst[6]))

#print([for pick ])
for key in alllines.keys():
    array = np.array([float(pair[1]) for pair in alllines[key]])
    #print(key," = ",arra
    # y)
    print(key,"# min ={:e}, max = {:e}, avr = {:e}, mean = {:e}, mid = {:e}, std = {:e}, var = {:e}".format(np.amin(array),np.amax(array),np.average(array),np.mean(array),np.median(array), np.std(array), np.var(array)))
    #print(key,"max = ",)
    #print(list)