'''
-*- coding: utf-8 -*-
@Author  : Setsu
@Software: PyCharm
'''

import sys
import jaconv
import json
print('日野ゼミ常用コマンド集合でございます！')
# グローバル変数変数について、グッグル先生に聞いてください
dict_nttfreq_created = dict_jonbs_created = dict_jmnbs_created = dict_homoph_created = dict_nttfam_created = dict_nttpfam_created = False
re_imported = False


# 日野ゼミでは、よくcsv形式で実験項目を保存しています。また実験結果は,間隔で保存することも多いんです。
# csv形式の問題は、microsoftのexcelで開いてみると、勝手に無内容の,,,が入ってしまうので、除去する必要があります。
def make_rawdata(afilename, sep='\t', ecd='utf-8', changeint=False):
    if afilename[-3:] == 'csv':
        sep, ecd = ',', 'cp932'
    f = open(afilename, 'r', encoding=ecd)
    arawdata = [x.strip().split(sep) for x in f.readlines()]
    if afilename[-3:] == 'csv':  # csvファイルの空白のものを除去
        arawdata = [[y for y in x if y != ''] for x in arawdata]
    if changeint is True:  # 整数の変換
        arawdata = [[int(y) if y.isdigit() else y for y in x]
                    for x in arawdata]
    f.close()
    return arawdata


# 操作中のものを保存したい場合、毎回リストの中身をstrに変換しなきゃいけない。
# 面倒だから、自動的にリストの中身をstrに変換するmake_outputを作成する訳です。
# input sample
# 【【学校, 2342】，【出力, 2332】，【名詞, 232333】】
def make_output(afilename, aoutputlist):
    if afilename[-3:] == 'csv':
        ecd, sep = 'cp932', ','
    else:
        ecd, sep = 'utf-8', '\t'
    if type(aoutputlist[0]) == list:
        aoutputlist = [
            sep.join([str(y) for y in x]) + '\n' for x in aoutputlist
        ]
    f = open(afilename, 'w', encoding=ecd)
    for x in aoutputlist:
        f.write(x)
    f.flush()
    f.close()


# 入力データを行列だと思って、その行列を転置する操作が結構あります。
# そのための関数です。
def t(alist):
    return list(map(list, (zip(*alist))))


# モーラ数を判断する関数
# カタカナは非対応です。出力はモーラ単位に分割されたもののリスト。
def make_mora(astring):
    tmp_list = list(astring)
    for x in tmp_list:
        if x in 'ぁぃぅぇぉゃゅょゎ':
            position = tmp_list.index(x)
            tmp_list.remove(x)
            tmp_list[position - 1] = tmp_list[position - 1] + x
    return tmp_list


# 漢字とその漢字がするすべての発音を統一する関数
# sample input:[['一1', ['一万円札,426']], ['一1', ['一世一代,56']]]
# sample output:[['一1', ['一万円札,426', '一世一代,56']]]
def make_fusion(alist):
    tmp_list_index = list(set([x[0] for x in alist]))
    tmp_list_index.sort()
    tmp_dict_index = dict(zip(tmp_list_index,
                              list(range(len(tmp_list_index)))))
    tmp_list_index = [[x, []] for x in tmp_list_index]
    for x in alist:
        tmp_num = tmp_dict_index[x[0]]
        if x[1] not in tmp_list_index[tmp_num][1]:
            tmp_list_index[tmp_num][1].append(x[1])
    return tmp_list_index


# list内容唯一性判断について（中身もリスト）
# 入力リストの中の重複しているものを除去する関数、ただ、順番が壊されてしまいます。
# sample input:[[大学, 名詞, 334],[大学, 名詞, 334],[学校, 名詞, 1334]]
# sample output:[[大学, 名詞, 334],[学校, 名詞, 1334]]
def make_unique(alist):
    aresult = list(set(['\t'.join(x) for x in alist]))
    aresult = [x.split() for x in aresult]
    return aresult


# 入力した文字列はひらかなのみであるかどうかをチェックする関数
def is_pure_hiragana(astring):
    global re_imported
    if re_imported is False:
        import re
        global re
        re_imported = True
    aresult = True
    if ''.join(re.findall('[ぁ-ん]+', astring)) != astring:
        aresult = False
    return aresult


# 入力した文字列はカタカナのみであるかどうかをチェックする関数
def is_pure_katakana(astring):
    global re_imported
    if re_imported is False:
        import re
        global re
        re_imported = True
    aresult = True
    if ''.join(re.findall('[ァ-ン]+', astring)) != astring:
        aresult = False
    return aresult


# 入力した文字列は漢字のみであるかどうかをチェックする関数
def is_pure_kanji(astring):
    global re_imported
    if re_imported is False:
        import re
        global re
        re_imported = True
    aresult = True
    if ''.join(re.findall('[一-龥]+', astring)) != astring:
        aresult = False
    return aresult


def get_length(word_phonetic):
    if ' ' in word_phonetic or '　' in word_phonetic:
        res = str(len(word_phonetic.split()[0]))
    else:
        res = str(len(word_phonetic))
    return res


def get_mora(word_phonetic, simple_output=True):
    if ' ' in word_phonetic or '　' in word_phonetic:
        normalized_input = word_phonetic.split()[1]
    else:
        normalized_input = word_phonetic
    res = list(normalized_input)
    for hirakana in res:
        if hirakana in 'ぁぃぅぇぉゃゅょゎ':
            position = res.index(hirakana)
            res.remove(hirakana)
            res[position - 1] = res[position - 1] + hirakana
    if simple_output is True:
        return str(len(res))
    else:
        return res


def get_nttfreq(word_phonetic, changeint=False):
    # 語彙を扱う場合、よく表記と発音一緒に利用するから
    # もし、表記と発音両方どもある場合、表記だけ取り出す
    if ' ' in word_phonetic or '　' in word_phonetic:
        normalized_input = word_phonetic.split()[0]
    else:
        normalized_input = word_phonetic
    global dict_nttfreq_created
    if dict_nttfreq_created is False:
        print('dict_nttfreq、作成中、少々お待ち下さい！')
        dict_path = [
            x for x in sys.path if x.split('\\')[-1][:9] == 'hinopy.py'
        ][0] + '\\dicts\\nttfreq.dict'
        f = open(dict_path, 'r', encoding='utf-8')
        global dict_nttfreq
        dict_nttfreq = eval(f.read())
        f.close()
        dict_nttfreq_created = True
    res = dict_nttfreq.get(normalized_input, '0')
    if changeint is True:
        res = int(res)
    return res


def get_fam(word_phonetic, changefloat=False):
    # 語彙を扱う場合、よく表記と発音一緒に利用するから
    # もし、表記と発音両方どもある場合、表記だけ取り出す
    if ' ' in word_phonetic or '　' in word_phonetic:
        normalized_input = word_phonetic.split()[0]
    else:
        normalized_input = word_phonetic
    global dict_nttfam_created
    if dict_nttfam_created is False:
        print('dict_nttfam、作成中、少々お待ち下さい！')
        dict_path = [
            x for x in sys.path if x.split('\\')[-1][:9] == 'hinopy.py'
        ][0] + '\\dicts\\ntt_fam.json'
        f = open(dict_path, 'r', encoding='utf-8')
        global d_fam
        d_fam = json.load(f)
        f.close()
        dict_nttfam_created = True
    res = d_fam.get(normalized_input, '0')
    if changefloat is True:
        res = float(res)
    return res


def get_pfam(word_phonetic, changefloat=False):
    # 音声単語親密度だが、表記自体も重要だから、引数として、表記と音韻情報両者が必要です
    # 音声単語親密度辞書のなか、音韻情報についての記録はカタカナなので、入力を標準化する必要がある
    normalized_input = ' '.join(
        [word_phonetic.split()[0],
         jaconv.hira2kata(word_phonetic.split()[1])])
    # 所要辞書の読み込み
    global dict_nttpfam_created
    if dict_nttpfam_created is False:
        print('dict_nttpfam、作成中、少々お待ち下さい！')
        dict_path = [
            x for x in sys.path if x.split('\\')[-1][:9] == 'hinopy.py'
        ][0] + '\\dicts\\ntt_pfam.json'
        f = open(dict_path, 'r', encoding='utf-8')
        global d_pfam
        d_pfam = json.load(f)
        f.close()
        dict_nttpfam_created = True
    res = d_pfam.get(normalized_input, '0')
    if changefloat is True:
        res = float(res)
    return res


def get_jonbs(word_phonetic, changeint=False, simple_output=True):
    # 所要辞書の読み込み
    global dict_jonbs_created
    if dict_jonbs_created is False:
        print('dict_jonbs、作成中、少々お待ち下さい！')
        dict_path = [
            x for x in sys.path if x.split('\\')[-1][:9] == 'hinopy.py'
        ][0] + '\\dicts\\jonbs.json'
        f = open(dict_path, 'r', encoding='utf-8')
        global d_jonbs
        d_jonbs = json.load(f)
        f.close()
        dict_jonbs_created = True
    # 入力の標準化 表記だけ取り出す
    if ' ' in word_phonetic or '　' in word_phonetic:
        normalized_input = word_phonetic.split()[0]
    else:
        normalized_input = word_phonetic
    # '大学' → ['○大', '大○']
    l_input = []
    for i in range(len(normalized_input)):
        tmp_l = list(normalized_input)
        del tmp_l[i]
        tmp_l.insert(i, '○')
        l_input.append(''.join(tmp_l))
    # d_jonbsを使って、jonbsを獲得
    l_all_jonbs = []
    for s in l_input:
        for line in d_jonbs.get(s, []):
            # target語彙の除去
            if normalized_input not in line:
                l_all_jonbs.append(line)
    # 結果出力部分
    if simple_output is not True:
        return l_all_jonbs
    elif changeint is False:
        return str(len(l_all_jonbs))
    else:
        return len(l_all_jonbs)


def get_jmnbs(word_phonetic, changeint=False, simple_output=True):
    # 所要辞書の読み込み
    global dict_jmnbs_created
    if dict_jmnbs_created is False:
        print('dict_jmnbs、作成中、少々お待ち下さい！')
        dict_path = [
            x for x in sys.path if x.split('\\')[-1][:9] == 'hinopy.py'
        ][0] + '\\dicts\\jmnbs.json'
        f = open(dict_path, 'r', encoding='utf-8')
        global d_jmnbs
        d_jmnbs = json.load(f)
        f.close()
        dict_jmnbs_created = True
    # 入力の標準化 音韻情報だけ取り出す
    if ' ' in word_phonetic or '　' in word_phonetic:
        normalized_input = word_phonetic.split()[1]
    else:
        normalized_input = word_phonetic
    # 'だいがく' → ['○いがく', 'だ○がく', 'だい○く', 'だいが○']
    l_input = []
    for i in range(len(normalized_input)):
        tmp_l = list(normalized_input)
        del tmp_l[i]
        tmp_l.insert(i, '○')
        l_input.append(''.join(tmp_l))
    # d_jmnbsを使って、jmnbsを獲得
    l_all_jmnbs = []
    for s in l_input:
        for line in d_jmnbs.get(s, []):
            # targetを除去
            if normalized_input not in line:
                l_all_jmnbs.append(line)
    # 結果出力部分
    if simple_output is not True:
        return l_all_jmnbs
    elif changeint is False:
        return str(len(l_all_jmnbs))
    else:
        return len(l_all_jmnbs)


def get_homoph(word_phonetic, changeint=False, simple_output=True):
    # 所要辞書の読み込み
    global dict_homoph_created
    if dict_homoph_created is False:
        print('dict_homoph、作成中、少々お待ち下さい！')
        dict_path = [
            x for x in sys.path if x.split('\\')[-1][:9] == 'hinopy.py'
        ][0] + '\\dicts\\sakuin_homoph.json'
        f = open(dict_path, 'r', encoding='utf-8')
        global d_homoph
        d_homoph = json.load(f)
        f.close()
        dict_homoph_created = True
    # パッケージ化ための辞書読み込むなどまだ書いてないんです
    # 入力の標準化 音韻情報だけ取り出す
    if ' ' in word_phonetic or '　' in word_phonetic:
        normalized_input = word_phonetic.split()[1]
    else:
        normalized_input = word_phonetic
    res = d_homoph.get(normalized_input, [])
    # 結果出力部分
    if simple_output is not True:
        return res
    elif changeint is False:
        return str(len(res))
    else:
        return len(res)


def get_opcon(word_phonetic, simple_output=True):
    # 高凝集で低結合のプログラミング（High Cohesion and Low Coupling）のために
    # 音韻隣接語の判断匿名関数を作る
    is_phonetic_friend = lambda l_target, l_jonb: 'Enemy' if len(
        l_target) != len(l_jonb) else ('Friend' if sum([
            1 if l_target[i] != l_jonb[i] else 0 for i in range(len(l_target))
        ]) <= 1 else 'Enemy')
    # 形態隣接語をゲット、そして表記と音韻情報を分割してdata_fileに保存
    l_df = [word_phonetic.split()] + [
        w.split()
        for w in get_jonbs(word_phonetic.split()[0], simple_output=False)
    ]
    # 頻度を追加する
    l_df = [w + [get_nttfreq(w[0], changeint=True)] for w in l_df]
    # 音韻隣接語であるかどうかを判断
    l_df = [l_df[0] + ['Target']] + [
        w + [
            is_phonetic_friend(get_mora(l_df[0][1], simple_output=False),
                               get_mora(w[1], simple_output=False))
        ] for w in l_df[1:]
    ]
    # 一貫性計算
    l_jonb_friends = [w[2] for w in l_df if w[-1][0] == 'F']
    l_jonb_all = [w[2] for w in l_df]
    sum_target_friends = l_df[0][2] + sum(l_jonb_friends)
    sum_all = sum(l_jonb_all)
    if sum_target_friends != 0 and sum_all != 0:
        op_onsistancy = sum_target_friends / sum_all
    else:
        op_onsistancy = 0
    l_df[0].append(str(round(op_onsistancy, 3)))
    l_df.append([])
    if simple_output is True:
        l_df = l_df[0][-1]
    return l_df


# headerとword_listこの２つの引数
# word_listの中身は語彙＋発音　eg:大学＋だいがく
# word_listはlistではなくでも可能が、　同じく語彙＋発音で
# Defaultのheaderは全て可能のデータ
def get_all(word_list, header=None, simple_output=True):
    if header is None:
        header = [
            'Length', 'Mora', 'Nttfreq', 'Fam', 'Pfam', 'Jonbs', 'Jmnbs',
            'Homoph', 'Opcon'
        ]
    # 一つの単語のデータを見たい場合でも対応可能
    if type(word_list) != list:
        word_list = [word_list]
    # ヘッダーの整形、全部大文字にする
    header = [s.title() for s in header]
    operator = {
        'Length': get_length,
        'Mora': get_mora,
        'Nttfreq': get_nttfreq,
        'Fam': get_fam,
        'Pfam': get_pfam,
        'Jonbs': get_jonbs,
        'Jmnbs': get_jmnbs,
        'Homoph': get_homoph,
        'Opcon': get_opcon
    }
    word_list = [[s] for s in word_list]
    for ope in header:
        for item in word_list:
            item.append(operator.get(ope, lambda s: 'None')(item[0]))
    # 出力をもっとキレイに見えるため、表記と発音を別々にバラす
    word_list = [l[0].split() + l[1:] for l in word_list]
    if simple_output is not True:
        word_list.insert(0, ['Item', 'Pronunciation'] + header)
    return word_list
