from prime_generator import PrimeGenerator

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


""" Test every method in PrimeGenerator Class """

pg = PrimeGenerator()


def test_primes_to_max():
    """ Test primes to max function """
    assert pg.primes_to_max(10) == [2, 3, 5, 7]
    assert pg.primes_to_max(20) == [2, 3, 5, 7, 11, 13, 17, 19]
