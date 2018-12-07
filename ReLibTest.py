# -*- coding:utf-8 -*-
import re

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin&fromtitle=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&fromid=6555484
def retest():
    # 开启多行模式
    # 不开多行的话, ^$只匹配当行起始和结尾
    # ^ 匹配输入字行首。如果设置了RegExp对象的Multiline属性，^也匹配“\n”或“\r”之后的位置
    # $ 匹配输入行尾。如果设置了RegExp对象的Multiline属性，$也匹配“\n”或“\r”之前的位置。

    pattern = re.compile(r"共(\d*)页")
    m = pattern.findall("共 5 45  页 共 5 45  页".replace(" ", ""))
    if len(m) > 0:
        for s in m:
            print(s)
    else:
        print("--not find--")
    print("-------------------------")

    pattern = re.compile(r"(\d*)评论(\d*)人气")
    m = pattern.findall("68 评论  5209 人气 6118 评论  51209 人气".replace(" ", ""))
    if m is not None:
        print(m)
    else:
        print("--not find--")
    print("-------------------------")

    pattern = re.compile(r"\d{1,3}")
    m = pattern.findall("h123 ddd 234d 13d4iu 43433")
    if m is not None:
        print(m)
    else:
        print("--not find--")
    print("-------------------------")

    pattern = re.compile(r"[a-z]\d?")
    m = pattern.findall("hello a1b 23c456 t346")
    if m is not None:
        print(m)
    else:
        print("--not find--")
    print("-------------------------")

    pattern = re.compile(r"\d?")
    m = pattern.findall("h")
    if m is not None:
        print(m)
    else:
        print("--not find--")
    print("-------------------------")

    # 非贪婪模式  从头(最少字符串)开始匹配,
    pattern = re.compile("e.*?a")
    # 贪婪模式  从尾(最多字符串)开始匹配
    # pattern = re.compile("e.*a")
    m = pattern.findall("1 ef5 ew32 aef ska")
    if m is not None:
        print(m)
    else:
        print("--not find--")
    print("-------------------------")

    pattern = re.compile("^.*?$", re.M)
    m = pattern.match("abce fg1\n" +
                      "4adike\n" +
                      "ganhgi")

    if m is not None:
        print(m.group())
    else:
        print("--not find--")
    print("-------------------------")

    pattern = re.compile("^qw.*?sj$(\n^f.*qw2$)\n^.*qw$", re.M)

    m = pattern.match("qwrewrwfjsj\n" +
                      "flswrewrwreqw2\n" +
                      "qwqw12qw")
    if m is not None:
        print(m.group())
        # 不传 表示匹配的整个字符串  传 表示取第几分组数据(前提是表达式中有分组)
        print(m.group(1))
    else:
        print("--not find--")
    print("-------------------------")

    # 测试贪婪模式？？？？？？？？
    pattern = re.compile("113")
    a = pattern.findall("1113aaddcc1\n11388ew88\n")
    for aa in a:
        print(aa)
    print("-------------------------")

    # I = IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE # ignore case
    # L = LOCALE = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
    # U = UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode locale
    # M = MULTILINE = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
    # S = DOTALL = sre_compile.SRE_FLAG_DOTALL # make dot match newline
    # X = VERBOSE = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments

    #  re.S 表示   . 将 匹配 换行 \n  默认不匹配
    pattern = re.compile("1.12", re.S)
    a = pattern.match("1\n12")
    print(a.group())
    print("-------------------------")


if __name__ == "__main__":
    retest()
