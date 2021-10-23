import sys
from prime_generator import PrimeGenerator


""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" The main controller of the prime list generator """


def main():
    pg = PrimeGenerator()
    input_num = sys.argv[1]

    # Make sure not to get empty list or receive negative
    # integers that don't have square root
    if int(input_num) >= 2:
        print(pg.primes_to_max(input_num))
    else:
        print("Please input an integer that is no less than 2")
        return


main()
