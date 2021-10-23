import re
my_dict1 = {"a": "b",
            "c": {"d": "e"},
            "f": {"g": {"h": "i"}},
            "j": ["k"]}

print(my_dict1["j"])

# my_dict = {"a": "b",
#            "c": {"d": {"e": "f"}},
#            "g": {"h": "i"},
#            "j": {"k"}}

# print(
#     my_dict['c'['d'['e']]])


# class A:
#     def __init__(self):
#         self.est_val = 2

#     def __eq__(self, other):
#         return self.est_val == other.est_val

#     def __gt__(self, other):
#         return self.est_val > other.est_val

#     def __lt__(self, other):
#         return self.est_val < other.est_val


# a = A()
# print(a.__lt__())

class A():
    def a(self):
        self.a = 1
        print(self.a)


a = A()
a.a()

s = "Jena S. Park"
p = re.findall(r"^[A-Z](?:\.|\w+)\s(\w)(?:\.|\w+)\s\w", s)
print(p)
