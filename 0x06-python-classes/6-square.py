#!/usr/bin/python3
''' module for the `Square Class '''


class Square:
    ''' A Sqaure; a shape whose sides are all of the same length '''
    def __init__(self, size=0, position=(0, 0)):
        '''  Square constructor '''
        self.size = size
        self.position = position

    def area(self):
        ''' calculates the area of the square '''
        return self.__size ** 2

    @property
    def size(self):
        ''' gets the length of a side of a square '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' sets the length of the sides of a square '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        ''' prints a square '''
        if self.size == 0:
            print()
        else:
            print("{:s}".format(self.__position[1] * '\n' +
                                (self.__position[0] * ' ' +
                                 '#' * self.__size + '\n') * self.__size)[:-1])

    @property
    def position(self):
        ''' gets the position of the square '''
        return self.__position


