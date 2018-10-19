"""
TO DO: setting attributes to our functions inside of a class

"""


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor": #first attribute
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor": #2nd
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError


def main():
    # create an instance of myColor
    cls1 = myColor() #instanstiate myColor() class as cls1
    # print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)


if __name__ == "__main__":
    main()
