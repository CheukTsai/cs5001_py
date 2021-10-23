from queue_extra import Queue
from stack_extra import Stack
import string
import copy

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        self.in_word = w1
        self.out_word = w2

        self.queue = Queue()
        self.stack = Stack()

        self.alphabet = string.ascii_lowercase
        self.wordlist = copy.deepcopy(wordlist)

    def make_ladder(self):
        """Make word ladder
        Self Object -> Stack, None"""

        """Push the first word into first stack,
        enqueue the first stack"""
        self.stack.push(self.in_word)
        self.queue.enqueue(self.stack)

        while not self.queue.isEmpty():
            # Dequeue the first stack
            stack = self.queue.dequeue()
            word_to_change = list(stack.peek())

            """If in_word is longer than out_word,
            delete any letter once in any place
            in the in_word, and check if the new word
            is an English word"""
            for i in range(len(word_to_change)):
                if len(word_to_change) > len(self.out_word):
                    new_word = "".join(word_to_change[0:i])\
                        + "".join(word_to_change[i+1:])

                    # Copy the stack and push
                    # new word into the stack
                    # and enqueue the new stack
                    # into the queue
                    if new_word in self.wordlist[len(new_word)]:
                        new_stack = stack.copy()
                        new_stack.push(new_word)

                        if(new_word == self.out_word):
                            return new_stack
                        else:
                            self.queue.enqueue(new_stack)
                            self.wordlist[len(new_word)].remove(new_word)

            """If in_word is shorter than out_word,
            insert any letter once in any place
            in the in_word, and check if the new word
            is an English word"""
            for i in range(len(word_to_change)+1):
                for letter in self.alphabet:

                    if len(word_to_change) < len(self.out_word):
                        word_to_change.insert(i, letter)
                        new_word = "".join(word_to_change)
                        new_stack = stack.copy()
                        new_stack.push(new_word)

                        # Copy the stack and push
                        # new word into the stack
                        # and enqueue the new stack
                        # into the queue
                        if new_word in self.wordlist[len(word_to_change)]:
                            new_stack = stack.copy()
                            new_stack.push(new_word)

                            if new_word == self.out_word:
                                return new_stack
                            else:
                                self.queue.enqueue(new_stack)
                                self.wordlist[len(word_to_change)].remove(
                                    new_word)

                        # Get the reduction of the word
                        word_to_change.pop(i)

            """If the length of words are same,
            do make ladder"""
            for i in range(len(word_to_change)):
                for letter in self.alphabet:
                    if word_to_change[i] == letter:
                        continue
                    tmp = word_to_change[i]
                    word_to_change[i] = letter
                    new_word = "".join(word_to_change)

                    # Copy the stack and push
                    # new word into the stack
                    # and enqueue the new stack
                    # into the queue
                    if new_word in self.wordlist[len(word_to_change)]:
                        new_stack = stack.copy()
                        new_stack.push(new_word)

                        if new_word == self.out_word:
                            return new_stack
                        else:
                            self.queue.enqueue(new_stack)
                            self.wordlist[len(word_to_change)].remove(new_word)

                    # Get the reduction of the word
                    word_to_change[i] = tmp

        return None
