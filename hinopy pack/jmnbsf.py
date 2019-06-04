# -*- coding: utf-8 -*-


def introduction():	#importのパッケージと実験の説明をここに格納
	#timeとosパッケージを使用しました
	print('音韻隣接語の語数を捜索するプログラムです。')
	print('ファイルごと処理するバージョンです。')
	print('改良したので，出力もにファイルあります。simpleがついてるものは，ターゲットと隣接語の数だけのものです。')
	print('単独の語彙の音韻隣接語を検索したい場合、jmnbs.pyを利用してください！\n')


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


def make_dict():
	#プログラムの主体を見やすくために，辞書の作成を一つの関数の中に格納
	NoD = os.path.abspath('.')+'\\dictionary\\jmnbs_justdict.dat'	#Name of Dict辞書の位置と名前を
	f = open(NoD, 'r', encoding = 'utf-8')
	tmp_list = [x.strip().split() for x in f.readlines()]
	f.close()
	tmp_list = [[x[0], x[1:]] for x in tmp_list]
	adict = dict(tmp_list)
	return adict


def make_mora(astring):
	tmp_list = list(astring)
	for x in tmp_list:
		if x in 'ゃゅょ':
			position = tmp_list.index(x)
			tmp_list.remove(x)
			tmp_list[position-1] = tmp_list[position-1]+x
	return tmp_list

	
def make_arrangement(alist):
	aresult = []
	if len(alist)>1:
		for x in list(range(len(alist))):
			aresult.append(alist[:x]+['○']+alist[x+1:])
	return aresult
	

def jmnbs(aent):	#音韻隣接語を処理する部分、aentとは入力した語彙の発音，
	tmp_LoR = []
	list_for_dict = make_arrangement(make_mora(aent))
	for x in list_for_dict:
		tmp_LoR = tmp_LoR + dict_jmnbs.get(''.join(x), [])
	tmp_LoR = [x.split(',') for x in tmp_LoR if x.split(',')[1] != aent]
	header = [aent, str(len(tmp_LoR))]
	tmp_LoR.insert(0,header)
	# for x in tmp_LoR[1:]:
	# 	print(x[0]+'\t'+x[1])
	# print('[%s]の音韻隣接語の数は：%s' % (aent,str(len(tmp_LoR)-1)))
	tmp_LoR.append([])
	return tmp_LoR


def output(LoR,NoF):	#結果を出力し、保存する関数。ファイルのをresultというフォルダーの下に
	if len(LoR) > 0:
		NoO = os.path.abspath('.')+'\\result\\jmnbsf_'+NoF+'_'+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.dat'	#name of output
		NoOS = os.path.abspath('.')+'\\result\\jmnbsf_simple_'+NoF+'_'+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.dat'	#name of output
		list_output = ['\t'.join(x)+'\n' for x in LoR]
		list_output_simple = [x for x in LoR if x != []]
		list_output_simple = ['\t'.join(x)+'\n' for x in list_output_simple if x[1].isdigit()]
		f = open(NoO,'w',encoding='utf-8')
		for x in list_output:
			f.write(x)
		f.flush()
		f.close()
		f = open(NoOS,'w',encoding='utf-8')
		for x in list_output_simple:
			f.write(x)
		f.flush()
		f.close()

		
import time,os
introduction()	#プログラムの説明をprint
dict_jmnbs = make_dict()	#辞書を作成
LoR = []	#list of Result 結果保存用リス
#while部分
while True:
	NoF = input('音韻隣接語の数を捜索したいリストの名前を:')
	#中止条件
	if NoF == 'end':
		break
	#ファイル存在しているかどうか
	if ToI(NoF) == 1:
		print('ファイルが存在しません！')
		continue
	else:
		LoG = getinput(NoF)	#List of Goi つまり、ファイルから処理する必要がる語彙をリストに格納
		start = time.clock()
		for x in LoG:	#語彙ごとに隣接語の数を検索するfor文
			if x == '':
				LoR = LoR + []	#リストの中にもし空白がある場合保留
			else:
				LoR = LoR + jmnbs(x)	#List　of Resultに結果を出力、出力されたのはリストです。
				print('[%s]に対する処理が完了です!' % x)
		elapsed = (time.clock() - start)
		print('処理完了です。%.2f秒の時間がかかりました!\n' % elapsed)
		output(LoR,NoF)	#List　of ResultとName of fileを引数として、outputという関数で結果をファイルの中に書き込みます！