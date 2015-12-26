# -*- coding: utf-8 -*-

__author__ = 'akyao'


import re
import sys

# selectorの一覧
# grep "{" style.css | sed -e s/\{// > ~/fuck.txt
# propertyの一覧
# grep ":" static/common/css/media.css | grep -v "{" | sed -e s/:.*//g | tr -d " " | sort | uniq

# 起動方法
# cat media.css | cssfmt | python css2csv.py > fuck.tsv


class CssBlock(object):

    all_property = []

    def __init__(self, selector):
        """
        :type selector: str
        :type properties : dict[str, str]
        """
        self.selector = selector
        self.properties = dict()
        # TODO all_property

    def add_property(self, key, value):
        self.properties[key] = value
        if key not in CssBlock.all_property:
            CssBlock.all_property.append(key)


class ResultPrint(object):

    def __init__(self):
        self.result_txt = ""

    def add_cell(self, txt):
        self.result_txt += txt + "\t"

    def add_line(self):
        # tab消す
        self.result_txt += "\n"

    def print2(self):
        print(self.result_txt)


if __name__ == "__main__":

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

    all_blocks = []
    for block in blocks:
        splited = block.split("{")
        if len(splited) == 2:
            # loop: セレクタ部分とプロパティたちにわける
            selector, props = splited[0:2]
            cssBlock = CssBlock(selector)

            for prop in props.split(";"):
                splited_prop = prop.split(":")
                if len(splited_prop) == 2:
                    prop_key, prop_val = splited_prop[0:2]
                    cssBlock.add_property(prop_key, prop_val)
            all_blocks.append(cssBlock)

    # TODO 準備

    # TODO CSV書き込み

    printer = ResultPrint()

    # titleの書き出し
    printer.add_cell("")
    for header in CssBlock.all_property:
        printer.add_cell(header)
    printer.add_line()

    # 各要素の描き込み
    for css_block in all_blocks:
        printer.add_cell(css_block.selector)
        for prop_key in CssBlock.all_property:
            if css_block.properties.has_key(prop_key):
                printer.add_cell(css_block.properties[prop_key])
            else:
                printer.add_cell("")
        printer.add_line()

    printer.print2()