import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x  #inside the point, x and y are it's attributes
        self.y = y

    def __str__(self):
        """
        Magic method that is called hen we try to print
        :return: <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__() #use the same way of printing as str

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5 #square root of the sum of x

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance

if __name__ == "__main__": #importing protection to others, only run if in this file
#now we need to instantiate it!
    p = Point(1, 2) #p is an instance of 1 and 2
p2 = Point(2, 3)
p4 = Point(4.4, -55)
print(f"p.x={p2.x} and p.y={p2.y}")
p2.x = 20
print(f"p.x={p2.x} and p.y{p2.y}")
print(p2)
#create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), #x value
                        random.randint(-10, 10))) #y value
print("I got these 5 random points")
print(points)
p = Point(3, 4)
print(p.distance_orig()) # expect 5 answer
p2 = Point(1,1)
print(f"I am comparing p > p2: {p>p2}") #I expect to have TRUE because I'm so cool
print(f"the sorted list of points is:")
points.sort()
print(points)
