# -*- coding: utf-8 -*-

def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('形態隣接語の語数を捜索するプログラムです。')
	print('二字熟語特化のバージョンです。\n二字熟語以外の語彙の形態隣接語を捜索したい場合、jonbs.pyを利用してください！\n')

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

def makeoutput(Goi,Index1,Index2):
	tempLoR = []
	List1 = Index1.get(Goi[0],[])
	List2 = Index2.get(Goi[1],[])
	Nojonbs = len(List1)//2+len(List2)//2	#Number of Jonbs
	CoT = 0	#Count of target
	if List1 != []:
		for x in [x for x in list(range(len(List1))) if x %2 ==0]:	#頭文字が被っている形態隣接語の検索結果の出力
			if List1[x] != Goi:
				print(List1[x]+'\t'+List1[x+1])	#出力
				tempLoR.append(List1[x]+'\t'+List1[x+1]+'\n')	#結果保存用のリストへ
			elif List1[x] == Goi:
				CoT = CoT + 1
	if List2 != []:
		for x in [x for x in list(range(len(List2))) if x %2 ==0]:	#二番目の文字が被っている形態隣接語の捜索結果の出力
			if List2[x] != Goi:
				print(List2[x]+'\t'+List2[x+1])	#出力
				tempLoR.append(List2[x]+'\t'+List2[x+1]+'\n')	#結果保存用のリストへ
			elif List2[x] == Goi:
				CoT = CoT + 1
	Nojonbs = Nojonbs - CoT	#ターゲット語の数を除去
	tempLoR.insert(0,Goi+'\t'+str(Nojonbs)+'\n')
	print('[%s]の形態隣接語の数は：%d' % (Goi,Nojonbs))
	return tempLoR

def output(LoR):	#結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.')+'\\result\\jonbs2_'+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.dat'	#name of output
		f = open(NoO,'w',encoding='utf-8')
		for x in LoR:
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
	Goi = input('形態隣接語の語数を捜索したい二字熟語を:')
	
	if Goi == 'end':
		output(LoR)
		break

	if len(Goi) == 2:
		print('	')
		LoR.append(makeoutput(Goi,Index1,Index2))
		print('	')
	else:
		print('入力エラー、二字熟語だけ入力してください!')