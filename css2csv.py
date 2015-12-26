# -*- coding: utf-8 -*-

__author__ = 'akyao'


import re
import sys

# selectorの一覧
# grep "{" style.css | sed -e s/\{// > ~/fuck.txt
# propertyの一覧
# grep ":" static/common/css/media.css | grep -v "{" | sed -e s/:.*//g | tr -d " " | sort | uniq

# 起動方法
# cat media.css | cssfmt | python css2csv.py


if __name__ == "__main__":
    # TODO 引数足らない場合
    all_lines = sys.stdin.readlines()

    # 全行くっつける
    line = ""
    for f in all_lines:
        # @charsetとか消す
        f = re.sub(r'@charset.+', "", f)
        # 前後の空白を消す 改行も消えちゃう
        line += f.strip().rstrip()

    # コメント消す
    line = re.sub(r'/\*.*?\*/', "", line, flags=re.DOTALL)

    # 前後の空白を消す

    # CSSは以下のフォーマットでできているとする
    # selector1{key1:val2;key2:val2} selector2{key1:val2;key2:val2}

    # }でsplit
    blocks = line.split("}")

    for block in blocks:
        splited = block.split("{")
        if len(splited) == 2:
            # loop: セレクタ部分とプロパティたちにわける
            selector, props = splited[0:2]
            splited_props = props.split(";")
            for prop in splited_props:
                splited_prop = prop.split(":")
                if len(splited_prop) == 2:
                    prop_key, prop_val = splited_prop[0:2]
                    print prop_val

    # 簡単なCSSならこれで解析できているはず

    # TODO 準備

    # TODO CSV書き込み

    # TODO titleの書き出し
    # TODO セレクタのループ
