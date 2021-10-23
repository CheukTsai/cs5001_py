def printbody1(a, d):
    n = 0
    s = int((a - 1) / 2)
    for i in range(a * d):
        picture = ""
        temp = 0
        for j in range(1, a + 1):
            if((i >= a * n) and (i < s + a * n)):
                picture += "-"
            else:
                picture += "X"

        print(picture)
        temp = i
        if(temp == a*n):
            n = n + 1


def printbody(a, d):
    n = 0
    picture = ""
    while n < d:
        if(a % 2 == 1):
            t = int((a + 1) / 2)
            s = int((a - 1) / 2)
            for i in range(t, t + a * d): a*d*d
                for j in range(1, a + 1):
                    if((i >= t + a * n) and (i < t + s + a * n)):
                        picture += "-"
                    if((i >= t + s + a * n) and (i < t + s + t + a * n)):
                        picture += "X"
                print(picture)
                picture = ""
        if(a % 2 != 1):
            t = int(a / 2)
            for i in range(t, t + a * d):
                for j in range(1, a + 1):
                    if((i >= t + a * n) and (i < t + t + a * n)):
                        picture += "-"
                    if((i >= t + t + a * n) and (i < t + t + t + a * n)):
                        picture += "X"
                print(picture)
                picture = ""
        n = n + 1
        a = a
        d = d


printbody(5, 4)
