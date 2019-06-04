# -*- coding: utf-8 -*-

def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('形態隣接語の語数を捜索するプログラムです。')
	print('二字熟語特化で，ファイルごと処理するバージョのんです。')
	print('二字熟語以外の語彙の形態隣接語を捜索したい場合、jonbs.pyを利用してください！\n')

def ToI(NoF):	#Test of Input もし入力に問題があったら，１を出力する
	try:
		f = open(NoF,'r',encoding = 'utf-8')
		f.close()
		print('\nこれより，処理が開始する！')
	except:
		return 1

def getinput(NoF):	#処理したいファイルの中身を読み込んで，全ての単語を１つのリストのなかに
	f = open(NoF, 'r', encoding='utf-8')
	LoG = f.readlines()
	f.close()
	LoG = [x.strip() for x in LoG]
	return LoG

def makedict():	#辞書を作成する部分
	start = time.clock()	#辞書を作るまで何秒かかりますかを図りたい
	f = open(os.path.abspath('.')+'\\dictionary\\jonbs2_dict1.dat','r',encoding='utf-8')	#頭文字の辞書の生成
	rawdict = f.readlines()
	f.close()
	L = [[x.strip().split()[0],x.strip().split()[1:]] for x in rawdict]
	Index1 = dict(L)
	f = open(os.path.abspath('.')+'\\dictionary\\jonbs2_dict2.dat','r',encoding='utf-8')	#二番目文字の辞書の生成
	rawdict = f.readlines()
	f.close()
	L = [[x.strip().split()[0], x.strip().split()[1:]] for x in rawdict]
	Index2 = dict(L)
	elapsed = (time.clock() - start)	#経過時間
	print('辞書作成完了です。\n%.2f秒の時間がかかりました。' % elapsed)
	print('なお、検索を結果を保存して終了したい場合、endを入力ください！\n')
	return Index1,Index2

def makeoutput(Goi,Index1,Index2):	#形態隣接語の数を検査して，結果をtempLoRに
	tempLoR = []
	List1 = Index1.get(Goi[0],[])
	List2 = Index2.get(Goi[1],[])
	Nojonbs = len(List1)//2+len(List2)//2	#Number of Jonbs
	CoT = 0	#Count of Target ターゲット語の数を計算して、隣接語の数から排除！
	if List1 != []:
		for x in [x for x in list(range(len(List1))) if x %2 ==0]:	#頭文字を共有している形態隣接語の検索結果の出力
			if List1[x] != Goi:	#ターゲット語をカウントされないように
				tempLoR.append(List1[x]+'\t'+List1[x+1]+'\n')	#結果保存用のリストへ
			elif List1[x] == Goi:
				CoT = CoT + 1
	if List2 != []:
		for x in [x for x in list(range(len(List2))) if x %2 ==0]:	#二番目の文字を共有している形態隣接語の捜索結果の出力
			if List2[x] != Goi:	#ターゲット語をカウントされないように
				tempLoR.append(List2[x]+'\t'+List2[x+1]+'\n')	#結果保存用のリストへ
			elif List2[x] == Goi:
				CoT = CoT + 1
	Nojonbs = Nojonbs - CoT	#最終的な形態隣接語の数です
	tempLoR.insert(0,Goi+'\t'+str(Nojonbs)+'\n')
	print('[%s]の形態隣接語の数は：%d' % (Goi,Nojonbs))
	return tempLoR

def output(LoR,NoF):	#結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.')+'\\result\\jonbs2f_'+NoF+'_'+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.dat'	#name of output
		f = open(NoO,'w',encoding='utf-8')
		for x in LoR:
			if x != '':
				for y in x:
					f.write(y)
			f.write('\n')
		f.flush()
		f.close()

import time,os
introduction()	#プログラムの説明をprint
Index1,Index2 = makedict()	#辞書を作成
LoR = []	#list of Result 結果保存用リスト

#while部分
while True:
	NoF = input('形態隣接語の語数を捜索したい二字熟語を:')

	if NoF == 'end':
		break

	if ToI(NoF) == 1:
		print('ファイルが存在しません！')
		continue
	else:
		LoG = getinput(NoF)	#List of Goi つまり、ファイルから処理する必要がる語彙をリストに格納
		start = time.clock()
		for x in LoG:	#語彙ごとに隣接語の数を検索するfor文
			if x == '':
				LoR.append('\n')	#リストの中にもし空白がある場合保留
			else:
				LoR.append(makeoutput(x,Index1,Index2))	#List　of Resultに結果を出力、出力されたのはリストです。
		elapsed = (time.clock() - start)
		print('処理完了です。%.2f秒の時間がかかりました!' % elapsed)
		output(LoR,NoF)	#List　of ResultとName of fileを引数として、outputという関数で結果をファイルの中に書き込みます！