# -*- coding: utf-8 -*
#import os
#os.chdir('C:\\Users\\Syunki\\Desktop\\hinopy pack\\raw_dictionary\\jmnbs用')
#sakuin.datというファイルの４４２５行日の発音「か」のうしろに謎のスペースがついてます。
#貸し付けるの発音も「かしつけける」と登録しています
#最初の考案が失敗した。つまり「だいがく」を「いがく」「だがく」「だいく」「だいが」に変換し辞書を作成する
#問題は，「げんかい」と「げんいん」に共通する「げんい」です。
#今の案は「だいがく」を「○いがく」「だ○がく」「だい○く」「だいが○」に変換し辞書を作り直し
#間牒	かんちょぅ　という入力ミスを発見
#小さい「ぁぃぅぇぉ」も前の仮名と合併し一つのモラとしてカウントします

def make_mora(astring):
	tmp_list = list(astring)
	for x in tmp_list:
		if x in 'ぁぃぅぇぉゃゅょゎ':
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


# alistの最小ユニットは[表記，発音（ひらがら）]
def make_decomposition(alist):
	aresult = []
	for x in alist:
		tmp_list_delpron = make_arrangement(make_mora(x[1]))
		if tmp_list_delpron != []:
			for y in tmp_list_delpron:
				aresult.append([''.join(y), ','.join(x)])
	return aresult

	
def make_fusion(alist):
    tmp_list_index = list(set([x[0] for x in alist]))
    tmp_list_index.sort()
    tmp_dict_index = dict(zip(tmp_list_index, list(range(len(tmp_list_index)))))
    tmp_list_index = [[x, []] for x in tmp_list_index]
    for x in alist:
        tmp_num = tmp_dict_index[x[0]]
        if x[1] not in tmp_list_index[tmp_num][1]:
            tmp_list_index[tmp_num][1].append(x[1])
    return tmp_list_index


def make_output(afilename, aoutputlist):
	if afilename[-3:] == 'csv':
		ecd, sep = 'cp932', ','
	else:
		ecd, sep = 'utf-8', '\t'
	if type(aoutputlist[0]) == list:
		aoutputlist = [sep.join(x) + '\n' for x in aoutputlist]
	f = open(afilename, 'w', encoding=ecd)
	for x in aoutputlist:
		f.write(x)
	f.flush()
	f.close()

	
f = open('sakuin.dat', 'r', encoding = 'utf-8')
rawdata = [x.strip().split(',') for x in f.readlines()]
f.close()
#間牒	かんちょぅ　を修正
for x in rawdata:
	if x[0] == 'かんちょぅ':
		rawdata[rawdata.index(x)][0] = 'かんちょう'
list_chosen = [[x[1], x[0]] for x in rawdata]
list_output = make_fusion(make_decomposition(list_chosen))
list_output = [[x[0]] + x[1] for x in list_output]
make_output('jmnbs_justdict.dat', list_output)