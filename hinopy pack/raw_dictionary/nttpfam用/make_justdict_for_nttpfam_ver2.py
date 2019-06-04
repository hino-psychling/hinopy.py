# -*- coding: utf-8 -*-
# import os
# os.chdir('C:\\Users\\Syunki\\Desktop\\hinopy pack\\raw_dictionary\\nttpfam用')
# nttpfam_rawdict.datとは初歩的な辞書です。一つの表記にたいして，同じ発音を複数持って，親密度もバラバラデス。
# 更に，親密度はｚのものもそのまま保留。
#　そして，更に精錬したのは，nttpfam_justdict.datというファイルです。
#　親密度の辞書のなかに値がzであるものが存在します。意味がわからないから，一旦削除します。
#　一つの表記にたいして，複数発音を持つことが許されますが，各発音は一番高い親密度のみ保存されています。


def make_output(afilename, aoutputlist):
	if afilename[-3:] == 'csv':
		ecd, sep = 'cp932', ','
	else:
		ecd, sep = 'utf-8', '\t'
	if type(aoutputlist[0]) == list:
		aoutputlist = [sep.join(x) + '\n' for x in aoutputlist]
	f = open(afilename, 'w', encoding=ecd)
	for x in aoutputlist:
		f.write(x)
	f.flush()
	f.close()


#まずはrawdictの生成	
f = open('nttpfam_justdict.dat', 'r', encoding='utf-8')
rawdata = [x.strip().split() for x in f.readlines()]
f.close()
result = []
for x in rawdata:
	for y in x[1:]:
		hyouki, atai = y.split(',')
		result.append(x[0]+','+hyouki+'\t'+atai+'\n')
make_output('nttpfam_justdict_ver2.dat', result)