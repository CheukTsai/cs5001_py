import math
print("Please type in the x and y for the first point: ")
x1 = float(input("x for the first point: "))
y1 = float(input("y for the first point: "))
print("Please type in the x and y for the second point: ")
x2 = float(input("x for the second point: "))
y2 = float(input("y for the second point: "))
print("The Euclidean distance between the two points will be", math.sqrt((y1-y2)*(y1-y2)+(x1-x2)*(x1-x2)))
