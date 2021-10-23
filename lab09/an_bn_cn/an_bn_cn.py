from stack_checker import Stack

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class AnBnCn:
    """Class for evaluating strings of n A's followed by n B's by n C's"""

    def __init__(self):
        self.stack = Stack()

    def accept(self, in_string):
        """
        Main method to check whether input string
        is legal by the rules or not

        String -> Boolean
        """

        # At first we expect A but not B
        expect_a = True
        expect_b = False

        for ch in in_string.lower():
            if ch == "a":
                if expect_a:
                    self.stack.push(ch)
                else:
                    return False

            elif ch == "b":
                if self.stack.is_empty():
                    return False
                else:
                    if expect_a:
                        expect_a = False
                        expect_b = True
                        self.stack.push(ch)
                        # Still keep pushing B into the stack
                    else:
                        self.stack.push(ch)
                        # Still keep pushing B into the stack

            elif ch == "c":
                if self.stack.is_empty() or expect_a:
                    # If expecting B but without B,
                    # will return False as well.
                    return False
                else:
                    if expect_b:
                        expect_b = False
                        # Delete two items once,
                        # to present 2 As and 2 Bs
                        # are needed to be popped by 1 C.
                        self.stack.pop()
                        self.stack.pop()
                    else:
                        self.stack.pop()
                        self.stack.pop()

        if self.stack.is_empty():
            return True
        return False

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack = Stack()
