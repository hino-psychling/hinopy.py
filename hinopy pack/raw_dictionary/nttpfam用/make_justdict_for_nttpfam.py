# -*- coding: utf-8 -*-
# import os
# os.chdir('C:\\Users\\Syunki\\Desktop\\hinopy pack\\raw_dictionary\\nttpfam用')
# nttpfam_rawdict.datとは初歩的な辞書です。一つの表記にたいして，同じ発音を複数持って，親密度もバラバラデス。
# 更に，親密度はｚのものもそのまま保留。
#　そして，更に精錬したのは，nttpfam_justdict.datというファイルです。
#　親密度の辞書のなかに値がzであるものが存在します。意味がわからないから，一旦削除します。
#　一つの表記にたいして，複数発音を持つことが許されますが，各発音は一番高い親密度のみ保存されています。


def make_fusion(alist):
    tmp_list_index = list(set([x[0] for x in alist]))
    tmp_list_index.sort()
    tmp_dict_index = dict(zip(tmp_list_index, list(range(len(tmp_list_index)))))
    tmp_list_index = [[x, []] for x in tmp_list_index]
    for x in alist:
        tmp_num = tmp_dict_index[x[0]]
        if x[1] not in tmp_list_index[tmp_num][1]:
            tmp_list_index[tmp_num][1].append(x[1])
    return tmp_list_index


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


def make_purification(alist):
	if len(alist) == 1:
		aresult = alist
	else:
		tmp_list = [x.split(',') for x in alist]
		tmp_list.sort(key = lambda l:float(l[1]))
		aresult = [','.join(x) for x in list(dict(tmp_list).items())]
	return aresult


#まずはrawdictの生成	
f = open('psylex1.txt', 'r', encoding='utf-8')
rawdata = [x.strip().split() for x in f.readlines()]
f.close()
rawdict = [[x[2], x[1]+','+x[6]] for x in rawdata]
rawdict = make_fusion(rawdict)
list_output = [[x[0]] + x[1] for x in rawdict]
make_output('nttpfam_rawdict.dat', list_output)
#これからはjustdictの精錬
#まず親密度はZのものを除去
rawdata_pured = [x for x in rawdata if x[6][0].isdigit()]
rawdict = [[x[2], x[1]+','+x[6]] for x in rawdata_pured]
rawdict = make_fusion(rawdict)
justdict = [[x[0], make_purification(x[1])]for x in rawdict]
list_output = [[x[0]] + x[1] for x in justdict]
make_output('nttpfam_justdict.dat', list_output)