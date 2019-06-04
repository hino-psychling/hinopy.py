# -*- coding: utf-8 -*-
#原初辞書の中に重複している語彙が沢山あります。重複している項目を除去するためのプログラムです。
#辞書型は、同じキーに対して、最後に入力された値だけ保持する特性があります。
#その特性を利用して、原初辞書(SRD.txt)の中身を一旦辞書型に変換し、またリストに戻して、ファイルに出力します。
#出力されたJustdict.txtの中に重複している語彙が削除されて、また最大の出現頻度のみ残されます。
#親密度の辞書のなかに値がzであるものが存在します。意味がわからないから，一旦削除します。

f = open('SRD.txt','r',encoding='utf-8')
rawdict = f.readlines()
f.close()
L = [x.strip().split(',') for x in rawdict]
tempL = []
for x in L:
	if x[1] != 'z':
		tempL.append(x)
Largdict = dict(tempL)

LoJD = []
for k,v in Largdict.items():
	LoJD.append(k+'\t'+v+'\n')

import time
start = time.clock()

f = open('nttfam_justdict.dat','w',encoding='utf-8')
for x in LoJD:
	f.write(x)
f.flush()
f.close()
end = time.clock()- start
print('Used time for making Justdict.txt:',end)

while True:
	pass