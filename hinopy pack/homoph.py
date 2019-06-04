# -*- coding: utf-8 -*-

def introduction():  # importのパッケージと実験の説明をここに格納
	# timeとosパッケージを使用しました
	print('sakuin.datを使用した同音語数を検索するプログラムです。\n今辞書を作成しています。少々お待ちください！\n')


def makedict():  # 辞書を作成する部分
	start = time.clock()  # 辞書を作るまで何秒かかりますかを図りたい
	f = open(os.path.abspath('.') + '\\dictionary\\homoph_justdict.dat', 'r', encoding='utf-8')
	rawdict = f.readlines()
	f.close()
	L = [[x.strip().split()[0], x.strip().split()[1:]] for x in rawdict]
	Largdict = dict(L)
	elapsed = (time.clock() - start)  # 経過時間
	print('辞書作成完了です。\n%.2f秒の時間がかかりました。' % elapsed)
	print('なお、検索を結果を保存して終了したい場合、endを入力ください！\n')
	return Largdict

def makeoutput(Goi,Homophs,LoR):	#dictの値は一つのリストなので、リストを分解してList of Resultsについか
	if Homophs != '0':
		LoR.append(Goi+'\t'+str(len(Homophs))+'\n')
		print(Goi+'\t',len(Homophs))
		for x in Homophs:
			LoR.append(Goi + '\t' + x + '\n')
			print(Goi+'\t'+x)
		LoR.append('\n')
	if Homophs == '0':
		LoR.append(Goi + '\t' + Homophs+ '\n')
		print(Goi + '\t', Homophs)
		LoR.append('\n')
	return LoR

def output(LoR):  # 結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.') + '\\result\\homoph_' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # name of output
		f = open(NoO, 'w', encoding='utf-8')
		for x in LoR:
			f.write(x)
		f.flush()
		f.close()


import time, os

introduction()
Largdict = makedict()
LoR = []  # list of Result 結果保存用リスト

# while部分
while True:
	Goi = input('同音語数を検索したい語の発音を（ひらかな）:')

	if Goi == 'end':
		output(LoR)
		break

	Homophs = Largdict.get(Goi,'0')	#データベースに存在しないものの頻度を０に
	LoR = makeoutput(Goi,Homophs,LoR)
