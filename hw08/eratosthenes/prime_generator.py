""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class PrimeGenerator:
    """
    Class to generate primes with Eratosthenes algorithm.
    """

    def __init__(self):
        # Basic constants
        self.POWER_HALF = 0.5

    def primes_to_max(self, number_input):
        """
        Function to generate primes with Eratosthenes algorithm.

        String -> List
        """

        # Prepare a list to collect prime numbers
        prime_list = []
        number = int(number_input)
        # Create a boolean list with length of input number
        is_prime = [True] * (number + 1)

        # Utilize Eratosthenes algorithm to generate the prime numbers
        range_mid = int(number ** self.POWER_HALF)
        for i in range(2, range_mid + 1):
            if is_prime[i]:
                for j in range(i * i, number + 1, i):
                    is_prime[j] = False
        for i in range(2, number+1):
            if is_prime[i]:
                prime_list.append(i)
        return prime_list
