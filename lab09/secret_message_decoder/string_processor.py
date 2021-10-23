from stack_decoder import Stack

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class StringProcessor:
    """Class for processing strings"""

    def __init__(self):
        self.stack = Stack()
        self.out_string = ""

    def process_string(self, in_string):
        """
        Main method to process strings

        String -> String
        """
        for ch in in_string:
            if ch == "*":
                if self.stack.peek() is not None:
                    self.out_string += self.stack.pop()
            elif ch == "^":
                if self.stack.peek() is not None:
                    self.out_string += self.stack.pop()
                    self.out_string += self.stack.pop()
            else:
                self.stack.push(ch)
        return self.out_string
