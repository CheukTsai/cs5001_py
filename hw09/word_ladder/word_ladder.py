from queue import Queue
from stack import Stack
import string

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        """Initialize word ladder"""
        self.in_word = w1
        self.out_word = w2

        self.queue = Queue()
        self.stack = Stack()

        self.alphabet = string.ascii_lowercase
        self.wordlist = wordlist.copy()

    def make_ladder(self):
        """Make word ladder
        Self Object -> Stack, None"""

        """Push the first word into first stack,
        enqueue the first stack"""
        wordlist = self.wordlist
        self.stack.push(self.in_word)
        self.queue.enqueue(self.stack)

        """If the length of words are different,
        simply return None"""
        if len(self.in_word) != len(self.out_word):
            return None

        """If the length of words are same,
        do make ladder"""
        while not self.queue.isEmpty():

            # Dequeue the first stack
            stack = self.queue.dequeue()
            word_to_change = list(stack.peek())

            for i in range(len(word_to_change)):
                for letter in self.alphabet:

                    # If the letter are the same,
                    # skip the replacing process
                    if word_to_change[i] == letter:
                        continue
                    tmp = word_to_change[i]
                    word_to_change[i] = letter
                    new_word = "".join(word_to_change)

                    # Copy the stack and push
                    # new word into the stack
                    # and enqueue the new stack
                    # into the queue
                    if new_word in self.wordlist:
                        new_stack = stack.copy()
                        new_stack.push(new_word)
                        if new_word == self.out_word:
                            return new_stack
                        self.queue.enqueue(new_stack)
                        wordlist.remove(new_word)

                    # Get the reduction of the word
                    word_to_change[i] = tmp

        return None
