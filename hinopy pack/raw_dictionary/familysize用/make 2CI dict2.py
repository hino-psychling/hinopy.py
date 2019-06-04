# -*- coding: utf-8 -*-
#漢字二字熟語の二番目の漢字のファミリサイズを計算するプログラムです。
#二番目の漢字とファミリサイズの間に，タブで区切られています。
#2CIとは2Character Idiom

f = open('jonbs2_dict2.dat', 'r', encoding = 'utf-8')
rawdata = f.readlines()
L = [[x.strip().split()[0],x.strip().split()[1:]] for x in rawdata]
f.flush()
f.close()

Index1 = dict(L)
Inital = [x[0] for x in L]
family_size = [[x,str(len(Index1[x])//2)] for x in Inital]
output = ['\t'.join(x) + '\n' for x in family_size]

f = open('2CI_family_size2.dat', 'w', encoding = 'utf-8')
for x in output:
	f.write(x)
f.flush()
f.close()