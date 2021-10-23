def count(n):
    if n <= 0:
        print("go!")
    else:
        count(n-1)
        print(n)


count(5)


