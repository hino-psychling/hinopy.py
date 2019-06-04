# -*- coding: utf-8 -*-

import time

start = time.clock()

f = open('jonbs_dict2.dat','r',encoding = 'utf-8')
rawdata = f.readlines()
rawdict = [[x.strip().split()[1],x.strip().split()[0]] for x in rawdata]	#ファイルの中身をリストへ
f.close()

Index1 = []	#頭文字を格納
Index2 = []	#二番目の文字を格納

for x in rawdict:
	if x[0][0] not in Index1:
		Index1.append(x[0][0])

for x in rawdict:
	if x[0][1] not in Index2:
		Index2.append(x[0][1])

Index1 = [[x,[]] for x in Index1]
Index2 = [[x,[]] for x in Index2]

for x in Index1:
	for y in rawdict:
		if x[0] == y[0][0]:
			x[1].append(y)
			
for x in Index2:
	for y in rawdict:
		if x[0] == y[0][1]:
			x[1].append(y)

f = open('jonbs2_dict1.dat','w',encoding = 'utf-8')
for x in Index1:
	item = x[0]
	for y in x[1]:
		item = item + '\t' + '\t'.join(y)
	item =  item + '\n'
	f.write(item)
f.flush()
f.close()
print('jonbs2_dict1 done!')

f = open('jonbs2_dict2.dat','w',encoding = 'utf-8')
for x in Index2:
	item = x[0]
	for y in x[1]:
		item = item + '\t' + '\t'.join(y)
	item =  item + '\n'
	f.write(item)
f.flush()
f.close()
print('jonbs2_dict2 done!')
elapsed = time.clock() - start
print('used time for making dict is %.2fs' % elapsed)

while True:
	pass