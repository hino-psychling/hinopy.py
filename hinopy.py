'''
-*- coding: utf-8 -*-
@Author  :
@Software: PyCharm
'''

import sys
print('日野ゼミ常用コマンド集合でございます！')
#グローバル変数変数について、グッグル先生に聞いてください
dict_nttfreq_created = False


# 日野ゼミでは、よくcsv形式で実験項目を保存しています。また実験結果は,間隔で保存することも多いんです。
# csv形式の問題は、microsoftのexcelで開いてみると、勝手に無内容の,,,が入ってしまうので、除去する必要があります。
def make_rawdata(afilename, sep = '\t', ecd = 'utf-8', changeint = False):
	if afilename[-3:] == 'csv':
		sep, ecd = ',', 'cp932'
	f = open(afilename, 'r', encoding=ecd)
	arawdata = [x.strip().split(sep) for x in f.readlines()]
	if afilename[-3:] == 'csv':	#csvファイルの空白のものを除去
		arawdata = [[y for y in x if y != ''] for x in arawdata]
	if changeint == True:	#整数の変換
		arawdata = [[int(y) if y.isdigit() else y for y in x] for x in arawdata]
	f.close()
	return arawdata

# 操作中のものを保存したい場合、毎回リストの中身をstrに変換しなきゃいけない。
# 面倒だから、自動的にリストの中身をstrに変換するmake_outputを作成する訳です。
# input sample
# 【【学校, 2342】，【出力, 2332】，【名詞, 232333】】
def make_output(afilename, aoutputlist):
	if afilename[-3:] == 'csv':
		ecd, sep = 'cp932', ','
	else:
		ecd, sep = 'utf-8', '\t'
	if type(aoutputlist[0]) == list:
		aoutputlist = [sep.join([str(y) for y in x]) + '\n' for x in aoutputlist]
	f = open(afilename, 'w', encoding=ecd)
	for x in aoutputlist:
		f.write(x)
	f.flush()
	f.close()

# 入力データを行列だと思って、その行列を転置する操作が結構あります。
# そのための関数です。
def t(alist):
	return list(map(list,(zip(*alist))))

# モーラ数を判断する関数
# カタカナは非対応です。出力はモーラ単位に分割されたもののリスト。
def make_mora(astring):
	tmp_list = list(astring)
	for x in tmp_list:
		if x in 'ぁぃぅぇぉゃゅょゎ':
			position = tmp_list.index(x)
			tmp_list.remove(x)
			tmp_list[position-1] = tmp_list[position-1]+x
	return tmp_list

# 漢字とその漢字がするすべての発音を統一する関数
# sample input:[['一1', ['一万円札,426']], ['一1', ['一世一代,56']]]
# sample output:[['一1', ['一万円札,426', '一世一代,56']]]
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

# list内容唯一性判断について（中身もリスト）
# 入力リストの中の重複しているものを除去する関数、ただ、順番が壊されてしまいます。
# sample input:[[大学, 名詞, 334],[大学, 名詞, 334],[学校, 名詞, 1334]]
# sample output:[[大学, 名詞, 334],[学校, 名詞, 1334]]
def make_unique(alist):
	aresult = list(set(['\t'.join(x) for x in alist]))
	aresult = [x.split() for x in aresult]
	return aresult

# テスト中直接頻度操作などの常用ものをパッケージの中に内包する
# 辞書の導入は時間がかかります。その故にhinopy導入する時点では、辞書の導入はなし。
# dict_nttfreq_createdという変数で辞書は作成しているかどうかを判別。
def get_nttfreq(aword, changeint = False):
	global dict_nttfreq_created
	if dict_nttfreq_created == False:
		print('dict_nttfreq、作成中、少々お待ち下さい！')
		dict_path = [x for x in sys.path if x[-9:] == 'hinopy.py'][0] + '\\dicts\\nttfreq.dict'
		f = open(dict_path, 'r', encoding='utf-8')
		global dict_nttfreq
		dict_nttfreq = eval(f.read())
		f.close()
		dict_nttfreq_created = True
	aresult = dict_nttfreq.get(aword, '0')
	if changeint == True:
		aresult = int(aresult)
	return aresult