from an_bn import AnBn


def main():
    an_bn = AnBn()
    line = input("Input a string:\n")
    if an_bn.accept(line):
        print("This string is accepted")
    else:
        print("This string is rejected")


main()
