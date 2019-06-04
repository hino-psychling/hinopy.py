# -*- coding: utf-8 -*-

#語彙頻度の導入
f = open('nttfreq_justdict.txt', 'r', encoding = 'utf-8')
rawdict = f.readlines()
f.close()
Largedict = dict([x.strip().split(',') for x in rawdict])

#頭文字の導入
f = open('jonbs2_dict1.dat', 'r', encoding = 'utf-8')
rawdata = f.readlines()
f.close()
#頭文字のみのIndexリストを作成
Index = [x.strip().split()[0] for x in rawdata]
#頭文字が対応する2字熟語（その熟語の発音を除去）のリストを作成（中身は複数のリスト）
Vocabularies = [x.strip().split()[1::2] for x in rawdata]

#ファミリ頻度の計算
#語彙頻度の辞書を使って，Vocabulariesの中身（語彙）を頻度変換して，加算，そして再びstrに変換し，ファミリ頻度総和のリストができる。
#頭文字のリストと頻度総和のリストを組合せると完了！
#一歩つづのコードは以下の様です
#frequencies = [[Largedict.get(y, '0') for y in x] for x in Vocabularies]
#Int_frequencies = [list(map(int, x)) for x in frequencies]
#Sum_frequencies = [sum(x) for x in Int_frequencies]
#Str_sum_frequencies = list(map(str, Sum_frequencies))
#一行で以上のコードを書くと以下の様です
str_sum_frequencies = [str(sum([int(Largedict.get(y,'0')) for y in x])) for x in Vocabularies]
f = open('Inital_Character_family_frequency.dat', 'w', encoding = 'utf-8')
for x in range(len(Index)):
    f.write(Index[x] + '\t' + str_sum_frequencies[x] + '\n')
f.flush()
f.close()

print('done')
while True:
    pass