# -*- coding: utf-8 -*-

import time
f = open('psylex72.txt','r',encoding='utf8')
rawdata = f.readlines()
f.close()
LoD = []
for x in rawdata:
	LoD.append([x.split()[0],x.split()[17]])
NLoD = sorted(LoD, key=lambda x:x[1])

LoD = [x[0]+','+x[1]+'\n' for x in LoD]
NLoD = [x[0]+','+x[1]+'\n' for x in NLoD]

start = time.clock()
f = open('rawdict.txt','w',encoding='utf8')
for x in LoD:
	f.write(x)
f.flush()
f.close()
end = time.clock()- start
print('Used time for making rawdict.txt:',end)

start = time.clock()
f = open('SRD.txt','w',encoding='utf8')
for x in NLoD:
	f.write(x)
f.flush()
f.close()
end = time.clock()- start
print('Used time for making SRD.txt:',end)

while True:
	pass