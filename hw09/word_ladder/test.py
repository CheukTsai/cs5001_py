# from stack import Stack


# def mystery(s, values):
#     hey = 0
#     go = 0
#     for val in values:
#         # print(count)
#         s.push(val)
#         hey += 1
#     n = 20
#     for i in range(4):
#         n += s.pop()
#         go += 1
#     for i in range(2):
#         n -= s.pop()
#         go += 1
#     print(go, "go")
#     print(hey, "hey")
#     return n


# def main():
#     count = 0
#     values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#     stack = Stack()
#     print(mystery(stack, values))


# main()


class A:
    def __init__(self):
        self.call = 0

    def spam(self, m, n):
        self.call += 1
        if m == 0:
            return n+1
        elif m > 0 and n == 0:
            return self.spam(m-1, 1)
        elif m > 0 and n > 0:
            return self.spam(m-1, self.spam(m, n-1))


a = A()
result = a.spam(1, 1)
print(a.call, "calls11")
print(result, "result11")


class A:
    def __init__(self):
        self.call = 0

    def spam(self, m, n):
        self.call += 1
        if m == 0:
            return n+1
        elif m > 0 and n == 0:
            return self.spam(m-1, 1)
        elif m > 0 and n > 0:
            return self.spam(m-1, self.spam(m, n-1))


a = A()
result = a.spam(1, 0)
print(a.call, "calls10")
print(result, "result10")

# def summ1(list1, acc):
#     if len(list1) == 0:
#         return acc
#     else:
#         acc = acc + 1
#         return summ1(list1[1:], acc)


# print(summ1([1, 3, 5, 7], 0))


# def summ2(list1):
#     if len(list1) == 0:
#         return 0
#     else:
#         return list1[0] + summ2(list1[1:])


# print(summ2([1, 3, 5, 7]))


# def summ3(list1, acc):
#     if acc == len(list1):
#         return 0
#     else:
#         return list1[0]+summ3(list1[1:], acc+1)


# print(summ3([1, 3, 5, 7], 0))


# def summ4(list1, acc):
#     if len(list1) == 0:
#         return acc
#     else:
#         return list1[0] + summ4(list1[1:], acc-1)


# print(summ4([1, 3, 5, 7], 0))


# def summ5(list1, acc):
#     if len(list1) == 0:
#         return acc
#     else:
#         acc = acc + list1[0]
#         return summ5(list1[1:], acc)


# print(summ5([1, 3, 5, 7], 0))


# def summ(list1):
#     if len(list1) == 0:
#         return 0
#     else:
#         return list1[0] + summ(list1[1:])


# print(summ([1, 3, 5, 7]))


# def foo(n):
#     if n < 1:
#         print(n)
#         return -1
#     else:
#         print(n)
#         return n*foo(n-3)


# print(foo(7), "final")


# def count(n):
#     print(n)
#     if n <= 0:

#         print("ok")
#     else:
#         count(n-2)
#         # print(n)


# count(5)

# mylist = [4, 6, 2]
# tot = 0
# for num in mylist:
#     tot = tot+num
# print(tot/len(mylist))

# def fac(n):
#     if n <= 1:
#         return 1
#     else:
#         return fac(n-1) * n


# print(fac(3))
