# -*- coding: utf-8 -*-

def introduction():  # importのパッケージと実験の説明をここに格納
	# timeとosパッケージを使用しました
	print('sakuin.datを使用した同音語数を検索するプログラムですのパッチ処理バージョンです。')
	print('検索したい語彙の発音（ひらかな）をtxtファイルに保存して、フォルダーにいれてください')
	print('辞書が作成中です！')

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

def ToI(name):	#Test of Input もし入力に問題があったら，１を出力する
	try:
		f = open(name,'r',encoding = 'utf-8')
		f.close()
	except:
		return 1

def makeoutput(Goi,Homophs,LoR):	#dictの値は一つのリストなので、リストを分解してList of Resultsについか
	if Homophs != '0':
		LoR.append(Goi+'\t'+str(len(Homophs))+'\n')
		for x in Homophs:
			LoR.append(Goi + '\t' + x + '\n')
		LoR.append('\n')
	if Homophs == '0':
		LoR.append(Goi + '\t' + Homophs+ '\n')
		LoR.append('\n')
	return LoR

def output(LoR):  # 結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.') + '\\result\\homophf_' +NoF+'_'+ time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # name of output
		f = open(NoO, 'w', encoding='utf-8')
		for x in LoR:
			f.write(x)
		f.flush()
		f.close()


def BPoH(name):  # Batch Processing of Homoph Homophのバッチ処理バージョン
	LoR = []  # list of Result 結果保存用リスト
	f = open(name, 'r', encoding='utf-8')
	LoG = f.readlines()
	f.close()
	LoG = [x.strip() for x in LoG]

	print('これより、処理が開始します。\n')  # 処理時間を図る部分
	start = time.clock()

	for x in LoG:  # バッチ処理のコーアです。入力リストの中にもし空白がある場合も保存
		if x != '':
			Homophs = Largdict.get(x, '0')  # データベースに存在しないものの頻度を０に
			LoR = makeoutput(x, Homophs, LoR)
			print('[%s]に対する処理が完了です!' % x)

	output(LoR)
	elapsed = (time.clock() - start)  # 終了時点
	print('\n全検索が完了しました。\n%.2f秒の時間がかかりました。\n' % elapsed)

import time, os

introduction()
Largdict = makedict()

# while部分
while True:
	NoF = input('同音語数を検索したい語の発音を（ひらかな）:')

	if NoF == 'end':
		output(LoR)
		break

	if ToI(NoF) == 1:
		print('ファイルが存在しません。')
		continue
	else:
		BPoH(NoF)
