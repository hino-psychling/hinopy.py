# -*- coding: utf-8 -*-

def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('Nttデータベースを使用した語彙発音親密度検索プログラムのファイル処理バージョンです。')
	print('同じ表記に複数の発音が対応していると言う問題を解消するためのVERSION2です。')
	print('そのため，入力ファイルに表記ではなく，発音も一緒に載せてください。')
	print('親密度=zの部分を削除済みで，データベースにない語彙の親密度は0です。')
	print('検索したい語彙をtxtファイルに保存して、フォルダーにいれてください！')
	print('今辞書を作成しています\n')

def makedict():	#辞書を作成する部分
	start = time.clock()	#辞書を作るまで何秒かかりますかを図りたい
	f = open(os.path.abspath('.')+'\\dictionary\\nttpfam_justdict_ver2.dat','r',encoding='utf-8')
	rawdict = f.readlines()
	f.close()
	L = [x.strip().split() for x in rawdict]
	Largdict = dict(L)
	elapsed = (time.clock() - start)	#経過時間
	print('辞書作成完了です。\n%.2f秒の時間がかかりました。' % elapsed)
	print('なお、検索を結果を保存して終了したい場合、endを入力ください！\n')
	return Largdict


def ToI(name):	#Test of Input もし入力に問題があったら，１を出力する
	try:
		f = open(name,'r',encoding = 'utf-8')
		f.close()
	except:
		return 1

def BPoF(name):	#Batch Processing of Frequencies Nttfreqのバッチ処理バージョン
	f = open(name,'r',encoding = 'utf-8')
	LoG = f.readlines()
	f.close()
	LoG = [x.strip().split() for x in LoG]
	LoG = [','.join(x) for x in LoG]
		
	print('これより、処理が開始します。\n')	#処理時間を図る部分
	start = time.clock()
		
	for x in LoG:
		if x != '':
			Freq = Largdict.get(x,'0.000')	#辞書にないものの頻度を0に固定
			print('[%s]に対する処理が完了です!' % x)
			LoR.append(x + '\t' + Freq + '\n')  # 結果出力のため検索結果を格納
		else:	#入力のファイルの中に空白がある場合、保留
			LoR.append('\n')

	NoO = os.path.abspath('.') + '\\result\\nttfamf_' +name+'_'+ time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) + '.dat'  # name of output
	f = open(NoO,'w',encoding = 'utf-8')
	for x in LoR:
		f.write(x)
	f.flush()
	f.close()
			
	elapsed = (time.clock() - start)	#終了時点
	print('\n全検索が完了しました。\n%.2f秒の時間がかかりました。\n' % elapsed)
		
import time,os
introduction()
Largdict = makedict()
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
		BPoF(NoF)