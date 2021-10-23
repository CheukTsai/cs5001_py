""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Bench:
    """A class representing a sidelines bench"""

    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.bench_list = []
        pass

    def send_to_bench(self, player_name):
        # Tsai: since we are going to use the pop function,
        # and also to go along with the FIFO idea
        # new element should be put at the very beginning
        # of the list
        self.bench_list.insert(0, player_name)
        # TODO: Put the player "onto the bench"
        pass

    def get_from_bench(self):
        # pop the last element of the list
        if(len(self.bench_list) == 0):
            print("The bench is empty.")
        else:
            print(f"Got {self.bench_list.pop()} from bench")
        # TODO: Return the name of the player who has
        # been on the bench longest.
        pass

    # TODO: Write the function that will display the
    # current list of players on the bench

    # TODO: Write any other methods that might be used
    # by the methods above.

    # Tsai: Not more methods has been written
