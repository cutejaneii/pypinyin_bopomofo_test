#!flask/bin/python
# -*- coding: utf-8 -*-

from pypinyin import pinyin, Style

from_word = '唐伯虎'
pinlist = pinyin(from_word.decode('utf-8'), style=Style.BOPOMOFO)

final_result = ''

for p in pinlist:
        to_word = p[0] # 印出注音，例如:  ㄊㄤˊ

        for bo in to_word:
                print(bo) # 分解注音，印出注音的每一個字母，例如: ㄊ

        final_result = final_result + to_word + ' '

print(final_result)
