# -*- coding: utf-8 -*-


def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('Nttデータベースを使用した語彙発音親密度のプログラムです。\n今辞書を作成しています。少々お待ちください！')
	print('親密度=zの部分を削除したバージョンです。\nまた，データベースにない語彙の親密度は0です。\n')
	

def makedict():	#辞書を作成する部分
	start = time.clock()	#辞書を作るまで何秒かかりますかを図りたい
	f = open(os.path.abspath('.')+'\\dictionary\\nttpfam_justdict.dat','r',encoding='utf-8')
	rawdict = f.readlines()
	f.close()
	L = [x.strip().split() for x in rawdict]
	L = [[x[0], x[1:]] for x in L]
	Largdict = dict(L)
	elapsed = (time.clock() - start)	#経過時間
	print('辞書作成完了です。\n%.2f秒の時間がかかりました。' % elapsed)
	print('なお、検索を結果を保存して終了したい場合、endを入力ください！\n')
	return Largdict

	
def output(LoR):	#結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.')+'\\result\\nttfam_'+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.dat'	#name of output
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
	
	Freq = Largdict.get(Goi,'0.000')	#データベースに存在しないものの頻度を０に
	if type(Freq)!= list:
		print('データベースに存在しない単語です。')
		LoR.append(Goi + '\tデータベースに該当なし\t0.000\n')
	else:
		for x in Freq:
			hyouki, pfam = x.split(',')
			print('[%s]-[%s]の親密度は：%s' % (Goi,hyouki,pfam))
			LoR.append(Goi+'\t'+hyouki+'\t'+pfam+'\n')	#結果出力のため、検索結果を格納