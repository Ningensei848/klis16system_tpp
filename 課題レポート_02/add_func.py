# -*- encoding: utf-8 -*-

import sys
from pathlib import Path

args = sys.argv # <class 'list'>

i = 0
func_dict = {}
p_dict = {}

### 入力ファイルのパスを作成
path = Path(args[1]) # arg[1]は入力ファイル名
with path.open() as f:
    file = f.readlines()

    for line in file:
        i += 1
        match_G = re.search(pattern_g, line)
        match_f = re.match(pattern_f, line)
        match_p = re.match(pattern_p, line)
        if match_G: # 1-1. G={hoge, foo, bar}が含まれていたら、それを取得
            # 1-2. 余分なものを取り除き、list[hoge, foo, bar]をつくる
            func_group = re.sub(pattern_fg, '', line)
            func_list = line.split # ==> func_list = [f1, ... , fn]
        elif match_f: # 2-1. 先頭に「f_x」があれば、それを取得
            # 2-2. 余分なものを取り除き、func_dictに追加
            temp_str = line.split(':=')
            func_dict[temp_str[0]] = temp_str[1]
        elif match_p: # 3-1. 先頭に「preduce」があったらp_dictとして定義
            # 3-2. keyは, f + (「func_dict」の要素数＋１）
            preduce = match_p.group()
            # 3-3. lineに次のgspolyの行が現れるまで探索
        else:
            pass