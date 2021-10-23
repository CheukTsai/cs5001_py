from an_bn_cn import AnBnCn

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" Main module to check an_bn_cn """


def main():
    """ Main function to check an_bn_cn """

    an_bn_cn = AnBnCn()
    line = input("Input a string:\n")
    if an_bn_cn.accept(line):
        print("This string is accepted")
    else:
        print("This string is rejected")


main()
