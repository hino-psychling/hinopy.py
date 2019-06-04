# -*- coding: utf-8 -*-

def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('Nttデータベースを使用した語彙文字総和頻度検索プログラムのファイル処理バージョンです。')
	print('検索したい語彙をtxtファイルに保存して、フォルダーにいれてください！')
	print('今辞書を作成しています\n')

def makedict():	#辞書を作成する部分
	start = time.clock()	#辞書を作るまで何秒かかりますかを図りたい
	f = open(os.path.abspath('.')+'\\dictionary\\nttcfreq_justdict.txt','r',encoding='utf-8')
	rawdict = f.readlines()
	f.close()
	L = [x.strip().split(',') for x in rawdict]
	Largdict = dict(L)
	elapsed = (time.clock() - start)	#経過時間
	print('辞書作成完了です。\n%.2f秒の時間がかかりました。' % elapsed)
	print('なお、プログラムを終了したい場合、endを入力ください！\n')
	return Largdict

def ToI(name):	#Test of Input もし入力に問題があったら，１を出力する
	try:
		f = open(name,'r',encoding = 'utf-8')
		f.close()
	except:
		return 1
		
def SoC(name):	#Summation of Characters
	Cfreq = 0
	for x in name:
		Cfreq = Cfreq + int(Largdict.get(x,'0'))
	return str(Cfreq)

def BPoCF(name):	#Batch Processing of Character Frequencies Nttcfreqのバッチ処理バージョン
	f = open(name,'r',encoding = 'utf-8')
	LoG = f.readlines()
	f.close()
	LoG = [x.strip() for x in LoG]
		
	print('これより、処理が開始します。')	#処理時間を図る部分
	start = time.clock()
		
	for x in LoG:	#バッチ処理のコーアです。入力リストの中にもし空白がある場合も保存
		if x != '':
			Cfreq = SoC(x)	#文字総和頻度の関数を引用
			print('[%s]に対する処理が完了です!' % x)
			LoR.append(x+'\t'+Cfreq+'\n')	#結果出力のため検索結果を格納
		else:
			LoR.append('\n')

	NoO = os.path.abspath('.') + '\\result\\nttfcreqf_' + name + '_' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # name of output
	f = open(NoO,'w',encoding = 'utf-8')
	for x in LoR:
		f.write(x)
	f.flush()
	f.close()
			
	elapsed = (time.clock() - start)	#終了時点
	print('\n全検索が完了しました。\n%.2f秒の時間がかかりました。\n' % elapsed)

import time,os
introduction()	#実験の説明を
Largdict = makedict()	#辞書の作成
LoR = []	#list of Result 結果保存用リスト

#while部分
while True:
	NoF = input('処理するファイルの名前を:')	#Name of File
	
	if NoF == 'end':
		break
	
	if ToI(NoF) == 1:
		print('ファイルが存在しません。')
		continue
	else:
		BPoCF(NoF)