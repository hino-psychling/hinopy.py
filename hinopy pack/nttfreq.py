# -*- coding: utf-8 -*-

def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('Nttデータベースを使用した語彙頻度検索のプログラムです。\n今辞書を作成しています。少々お待ちください！\n')

def makedict():	#辞書を作成する部分
	start = time.clock()	#辞書を作るまで何秒かかりますかを図りたい
	f = open(os.path.abspath('.')+'\\dictionary\\nttfreq_justdict.txt','r',encoding='utf-8')
	rawdict = f.readlines()
	f.close()
	L = [x.strip().split(',') for x in rawdict]
	Largdict = dict(L)
	elapsed = (time.clock() - start)	#経過時間
	print('辞書作成完了です。\n%.2f秒の時間がかかりました。' % elapsed)
	print('なお、検索を結果を保存して終了したい場合、endを入力ください！\n')
	return Largdict

def output(LoR):	#結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.')+'\\result\\nttfreq_'+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.dat'	#name of output
		f = open(NoO,'w',encoding='utf-8')
		for x in LoR:
			f.write(x)
		f.flush()
		f.close()

import time,os
introduction()
Largdict = makedict()
LoR = []	#list of Result 結果保存用リスト

#while部分
while True:
	Goi = input('検索したい語彙は:')
	
	if Goi == 'end':
		output(LoR)
		break
	
	Freq = Largdict.get(Goi,'0')	#データベースに存在しないものの頻度を０に
	print('[%s]の出現頻度は：%s' % (Goi,Freq))
	LoR.append(Goi+'\t'+Freq+'\n')	#結果出力のため、検索結果を格納