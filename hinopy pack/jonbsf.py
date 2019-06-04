# -*- coding: utf-8 -*-

def introduction():
	print('形態隣接語彙の数を検索するプログラムです。')
	print('ファイルごと処理するバージョンです。#ファイルの中に一文字のもの入れないでください！#')
	print('検索の結果を保存して終了したい場合、endを入力ください！')

def ToI(NoF):	#Test of Input もし入力に問題があったら，１を出力する
	try:
		f = open(NoF,'r',encoding = 'utf-8')
		f.close()
		print('\nこれより，処理が開始する！')
	except:
		return 1

def getinput(NoF):
	f = open(NoF, 'r', encoding='utf-8')
	LoG = f.readlines()
	f.close()
	LoG = [x.strip() for x in LoG]
	return LoG

def change(str):	#入力の文字を変化するため、大学　⇒　¥w学、大¥w
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
	return L,switch

def jonbs(ent,raw,dict):	#形態隣接語を処理する部分、reモジュールを使用したものです
	tempLoR = []
	for x in raw:	#大学の場合[¥w学,大¥w]
		for y in dict:
			if re.match(x, y[1]) and ent != y[1]:
				tempLoR.append(y[1]+'\t'+y[0])
	header = ent + '\t' + str(len(tempLoR))	#ターゲット語と形態隣接語の数
	tempLoR.insert(0,header)
	print('[%s]にたいする処理が完了した' % ent)
	return tempLoR

def output(LoR,Nof):	#結果をファイルに保存する関数です。
	NoO = os.path.abspath('.') + '\\result\\jonbsf_' + Nof + '_' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # Name of Output結果保存用ファイルの名前
	f = open(NoO,'w',encoding = 'utf-8')	#Name of Output
	for x in LoR:
		if x != '':
			for item in x:
				f.write(item+'\n')
			f.write('\n')
		else: 
			f.write('\n')
	f.flush()
	f.close()

import time,re,os
dictionary = list(range(9))	#辞書を格納するの大辞書ですdictionary[2]とは、二字熟語の辞書です。
switch = [0] * 10	#辞書が生成しているかどうかを確認するためのものです。0とは、辞書が存在しないと意味しています。
LoR = []

introduction()	#プログラムの説明などを編集しやすくなるために，説明文を1つの関数に格納した。
while True:

	Nof = input('\n処理するファイルの名前を:')

	if Nof == 'end':
		break

	if ToI(Nof) == 1:
		print('\nファイルは存在しません！')
		continue

	LoG = getinput(Nof)	#ファイルの中の語彙をList of Goiというリストに転送

	start = time.clock()  # 時間を図る
	for x in LoG:	#バッチ処理
		if len(x) > 1:
			if switch[len(x)] == 0:	#辞書の存在をチェック、存在しない場合、calldictによって辞書を作成そして、dictionaryに保存
				dictionary[len(x)],switch = calldict(len(x), switch)
			LoC = change(x)
			LoR.append(jonbs(x,LoC,dictionary[len(x)]))	#jonbs関数を実施、結果をList of Resultに保存
	output(LoR,Nof)	#結果をファイルに出力する関数
	elapsed = (time.clock() - start)  # 経過時間
	print('処理完了です。\n%.2f秒の時間がかかりました。' % elapsed)