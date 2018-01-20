# -*- coding:utf-8 -*-
import re


# https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin&fromtitle=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&fromid=6555484
def retest():
    # 开启多行模式
    # 不开多行的话, ^$只匹配当行起始和结尾
    # ^ 匹配输入字行首。如果设置了RegExp对象的Multiline属性，^也匹配“\n”或“\r”之后的位置
    # $ 匹配输入行尾。如果设置了RegExp对象的Multiline属性，$也匹配“\n”或“\r”之前的位置。

    pattern = re.compile("^qw.*sj$\n^f.*qw2$\n^.*qw$", re.M)

    m = pattern.match("qwrewrwfjsj\n" +
                      "flswrewrwreqw2\n" +
                      "qwqw12qw")

    print(m.group())
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
