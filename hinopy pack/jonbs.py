# -*- coding: utf-8 -*-

def introduction():
	#time,re,osパッケージを使用した
	print('形態隣接語彙の数を検索するプログラムです。')
	print('検索の結果を保存して終了したい場合、endを入力ください！')

def ToI(ent):	#Test of input　2-9文字の語彙のみ許されるようにチェックします
	if len(ent) > 9 or len(ent) < 2:
		return 1

def change(str):	#入力の文字を変化するため、大学　⇒　¥w学、大¥w　正規表現を利用する予定です
	strlist = list(str)
	LoC = []
	for x in range(len(str)):
		tmpt = strlist[:]
		tmpt[x] = '\w'
		LoC.append(''.join(tmpt))
	return LoC	#List of Changed

def calldict(length,switch):	#入力する熟語の長さによって辞書を作成する
	switch[length] = 1	#文字の長さに対応する辞書をすでに生成した印です
	NoD = os.path.abspath('.')+'\\dictionary\\jonbs_dict'+str(length)+'.dat'	#Name of Dict辞書の位置と名前を
	f = open(NoD,'r',encoding = 'utf-8')
	rawdict = f.readlines()
	f.close()
	L = [x.strip().split() for x in rawdict]
	print('\n' + str(length) + '字熟語の辞書を作成した。')
	return L,switch

def jonbs(ent,raw,dict):	#形態隣接語を処理する部分、reモジュールを使用したものです
	tempLoR = []
	for x in raw:	#大学の場合[¥w学,大¥w]
		for y in dict:
			if re.match(x, y[1]) and ent != y[1]:
				tempLoR.append(y[1]+'\t'+y[0])
	header = ent + '\t' + str(len(tempLoR))
	tempLoR.insert(0,header)
	for x in tempLoR[1:]:
		print(x)
	print('[%s]の形態隣接語の数は：%s' % (ent,str(len(tempLoR)-1)))
	return tempLoR

def output(LoR):	#結果をファイルに保存する関数です。
	NoO = os.path.abspath('.') + '\\result\\jonbs_' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # Name of Output結果保存用ファイルの名前
	f = open(NoO,'w',encoding = 'utf-8')	#Name of Output
	for x in LoR:
		for item in x:
			f.write(item+'\n')
		f.write('\n')
	f.flush()
	f.close()

import time,re,os
dictionary = list(range(9))	#辞書を格納するの大辞書ですdictionary[2]とは、二字熟語の辞書です。
switch = [0] * 10	#辞書が生成しているかどうかを確認するためのものです。0とは、辞書が存在しないと意味しています。
LoR = []

introduction()	#プログラムの説明などを編集しやすくなるために，説明文を1つの関数に格納した。
while True:
	ent = input('\n形態隣接語の数を検索したい語彙を:')

	if ent == 'end':
		if len(LoR) > 0:
			output(LoR)	#結果をファイルに出力する
		break

	if ToI(ent) == 1:
		print('\n入力エラーです。')
		continue

	if switch[len(ent)] == 0:	#辞書の存在をチェック、存在しない場合、calldictによって辞書を作成そして、dictionaryに保存
		dictionary[len(ent)],switch = calldict(len(ent), switch)
	
	LoC = change(ent)
	print('')
	LoR.append(jonbs(ent,LoC,dictionary[len(ent)]))	#jonbs関数を実施、結果をList of Resultに保存