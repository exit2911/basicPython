# give objects number-like behavior

"""
TO DO: Creating your own mathematical operations for cartesian points 

"""


class Point():
    def __init__(self, x, y): #imagine self as x, and x and y as different ts
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # implement addition
    def __add__(self, other):  #__add__ interpreted as +
        return Point(self.x + other.x, self.y + other.y)

    # implement subtraction
    def __sub__(self, other): 
        return Point(self.x - other.x, self.y - other.y)

    # implement in-place addition
    def __iadd__(self, other): #__iadd__ increment add
        self.x += other.x
        self.y += other.y
        return self


def main():
    # Declare some points
    p1 = Point(10, 20) #Point() is your function defined above
    p2 = Point(30, 30)
    print(p1, p2)

    # Add two points
    p3 = p1 + p2
    print(p3)

    # subtract two points
    p4 = p2 - p1
    print(p4)

    # Perform in-place addition
    p1 += p2
    print(p1)


if __name__ == "__main__":
    main()
