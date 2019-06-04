# -*- coding: utf-8 -*-


def introduction():
	#time,osパッケージを使用した
	print('モラ単位の音韻隣接語の数を検索するプログラムです。')
	print('ひらがなで検索したい単語の発音を入力してください。')
	print('音韻隣接語の検索なので，入力は２かな以上でお願いします。')
	print('検索の結果を保存して終了したい場合、endを入力してください！')


def make_dict():
	#プログラムの主体を見やすくために，辞書の作成を一つの関数の中に格納
	NoD = os.path.abspath('.')+'\\dictionary\\jmnbs_justdict.dat'	#Name of Dict辞書の位置と名前を
	f = open(NoD, 'r', encoding = 'utf-8')
	tmp_list = [x.strip().split() for x in f.readlines()]
	f.close()
	tmp_list = [[x[0], x[1:]] for x in tmp_list]
	adict = dict(tmp_list)
	return adict

	
def make_mora(astring):
	tmp_list = list(astring)
	for x in tmp_list:
		if x in 'ぁぃぅぇぉゃゅょゎ':
			position = tmp_list.index(x)
			tmp_list.remove(x)
			tmp_list[position-1] = tmp_list[position-1]+x
	return tmp_list

	
def make_arrangement(alist):
	aresult = []
	if len(alist)>1:
		for x in list(range(len(alist))):
			aresult.append(alist[:x]+['○']+alist[x+1:])
	return aresult
	

def jmnbs(aent):	#音韻隣接語を処理する部分、aentとは入力した語彙の発音，
	tmp_LoR = []
	list_for_dict = make_arrangement(make_mora(aent))
	for x in list_for_dict:
		tmp_LoR = tmp_LoR + dict_jmnbs.get(''.join(x), [])
	tmp_LoR = [x.split(',') for x in tmp_LoR if x.split(',')[1] != aent]
	header = [aent, str(len(tmp_LoR))]
	tmp_LoR.insert(0,header)
	for x in tmp_LoR[1:]:
		print(x[0]+'\t'+x[1])
	print('[%s]の音韻隣接語の数は：%s' % (aent,str(len(tmp_LoR)-1)))
	tmp_LoR.append([])
	return tmp_LoR

	
def output(LoR):	#結果をファイルに保存する関数です。
	NoO = os.path.abspath('.') + '\\result\\jmnbs_' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # name of output
	f = open(NoO, 'w', encoding='utf-8')
	list_output = ['\t'.join(x)+'\n' for x in LoR]
	for x in list_output:
		f.write(x)
	f.flush()
	f.close()


import time,os
LoR = []
introduction()	#プログラムの説明などを編集しやすくなるために，説明文を1つの関数に格納した。
dict_jmnbs = make_dict()
while True:
	ent = input('\n音韻隣接語の数を検索したい語彙を:')
	# 中止条件と出力
	if ent == 'end':
		if len(LoR) > 0:
			output(LoR)	#結果をファイルに出力する
		break
	# 入力は少なくても１モラーが必要です
	if len(ent) < 2:
		print('\n入力エラーです。')
		continue
	# 入力ものをモラー単位に変換，そうして辞書用ものに変換，jmnbsという関数に導入，結果を保存
	LoR = LoR + jmnbs(ent)	#jmnbs関数を実施、結果をList of Resultに保存