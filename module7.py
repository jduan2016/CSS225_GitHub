## Professor: Linh Vu
# Student: Jia Duan
# Date: 11/9/2024
# CSS 225 - Assignment 7

import turtle
import math


def areaOfCircle(r):
    """
    This function calculates the area of a circle
    """
    areaCircle = round(math.pi*pow(r,2),2)
    print("Problem 1.")
    print(f"When radius is {r}, the are of the circle is {areaCircle}.\n")
        
def check_number(my_range,alist):
    """
    This function checks if a list of number is in certain range
    Use range(1,10)
    """
    i,j = my_range.start,my_range.stop #Get the boundary values for the range
    range_flag = True
    for element in alist:
        if element < i or element >= j:
            range_flag = False
            break
    print("Problem 2.")
    if range_flag == True:
        print(f"The numbers in {alist} is between {i}(inclusive) and {j}(exclusive)\n")
    else:
        print(f"The numbers in {alist} is NOT between {i}(inclusive) and {j}(exclusive)\n")



def list_multiplication(alist):
    """
    This functions multiple all the elements in a list
    """
    result = 1
    for i in alist:
        result = result *i
    print("Problem 3.1")
    print(f"The product of all the elements in {alist} is {result}.\n")

    
def list_multiplication_recursive(alist: list):
    # 5 points extra credit
    """
    This functions multiple all the elements in a list using recursion
    """
    # [5, 2, 7, -1]
    # [2, 7, -1]
    # [ 7, -1 ]
    # [ -1 ]

    # The guard
    if (alist is not None) and (len(alist) == 0):
        return 1
    
    if len(alist) == 1:
        return alist[0]
    else:
        #if list_multiplication_recursive(alist[1:]) == True:
        # 5 * -14 = -70
        # 2 * -7 = -14
        # 7 * -1 = -7
        # -1
        return alist[0] * list_multiplication_recursive(alist[1:])

def get_unique(alist):
    """
    Given a list, this funciton return a list of unique numbers."
    """
    # unique_list = list(set(alist)) # The list is sorted using this method.
    unique_list = []
    for element in alist:
        if element not in unique_list:
            unique_list.append(element)
    print("Problem 4.")
    print(f"The unique list created from {alist} is {unique_list}.\n")

    
def draw_square(t, sz) :
    """Get turtle t to draw a square of sz side"""
    t.color("blue")
    t.pensize(2)
    for i in range(5): #5 squares
        for i in range(4) :
            t.forward(sz)
            t.left(90)
        t.penup()
        t.backward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()
        sz += 20
        
    wn = turtle.Screen()
    # alex = turtle.Turtle()
    # alex.color("blue")
    wn.exitonclick()

class Car:
    # This car class has attributes in model, year, color,type, and manufacturer
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def get_car_type(self):
        return self.car_type
    
    def get_manufacturer(self):
        return self.manufacturer
    
    def fullspec(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + \
        ' ' + self.car_type + ' ' + self.manufacturer
    

def main():
    # Call functions here
    r = 3
    areaOfCircle(r)
    alist1 = [1,2,3,4,5,6,7,8,9,10]
    check_number(range(1,10),alist1)
    alist2 = [5,2,7,-1]
    list_multiplication(alist2)
    print("Problem 3.2")
    print(f"The product of all the elements in {alist2} is {list_multiplication_recursive(alist2)}.\n")
    alist3 = [1,3,3,3,6,2,3,5]
    get_unique(alist3)
    # Initiation for problem 5
    t = turtle.Turtle()
    draw_square(t,20)
    car1 = Car("Corvette", 2025, "Blue", "Sports", "Chevrolet")
    car2 = Car("Civis", 2012, "Black", "Sedan", "Honda")
    print(car1.get_model())
    print(car1.get_year())
    print(car1.get_color())
    print(car2.get_car_type())
    print(car2.get_manufacturer())
    print(car1.fullspec())
    print(car2.fullspec())

if __name__ == "__main__":
    main()