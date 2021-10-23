""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Point:
    """ To get x and y of a point, and the midpoint with other points """

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        """ Get x of the point
        None -> Float """
        return self.xCoord

    def getY(self):
        """ Get x of the point
        None -> Float """
        return self.yCoord

    def midPoint(self, otherPoint):
        """ Return a new midpoint
        with new x and new y"""

        newX = float((self.xCoord + otherPoint.getX()) / 2)
        newY = float((self.yCoord + otherPoint.getY()) / 2)
        return Point(newX, newY)
