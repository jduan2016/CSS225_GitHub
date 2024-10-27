# Professor: Linh Vu
# Student: Jia Duan
# Date: 10/20/2024
# CSS 225 - Assignment 5
import turtle
from time import sleep

def print_hello(n):
    # TODO: Print hello n times
    # pass
    """
    This function prints hello n time using a loop
    """
    while n>0:
        print("hello")
        n-=1
    # print("\n")

def print_hello_alt(n):
    # TODO: There is another way without using loop but just print statement
    # 5 pts Extra credit
    # pass
    """
    This function prints hello n time without using a loop
    """
    print("hello\n"*n)


def print_hello_recursion(n):
    # What about we use recursion?
    # 20 pts Extra credit
    # https://runestone.academy/ns/books/published/thinkcspy/IntroRecursion/toctree.html
    # pass
    """
    This function prints hello n times using recursion
    """
    if n == 1:
        print('hello')
    else:
        print('hello')
        print_hello_recursion(n-1)
    # print("\n")

def power_list(arr):
    # TODO: This is problem 2 in the handout
    # a. Write a loop that prints each of the numbers on a new line.
    # b. Write a loop that prints each number and its square on a new line.
    # pass
    """
    This function prints each number of the list on a new line,
    it also prints each number and its square on a new line.
    """
    # arr = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    for i in range(len(arr)):
        print(arr[i])
    for i in range(len(arr)):
        print(arr[i],arr[i]**2)


def power_list_recursion_a(arr):
    # TODO: This is problem 2 in the handout
    # Instead of looping, how about recursion?
    # 20 pts Extra credit
    # pass
    """
    This function uses recursion to print each number of the list on a new line.
    """
    # arr = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    n = len(arr)
    # Base case 1
    if n == 0:
        print(arr)
    # Base case 2
    elif n == 1:
        print(arr[0])
    else:
        print(arr[0])
        if power_list_recursion_a(arr[1:]) == True: # Remove "None"
            print(power_list_recursion_a(arr[1:]))

def power_list_recursion_b(arr):
    """
    This function uses recursion to print square of each number on a new line.
    """
    # arr = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    # def square_list(alist):
    #     """
    #     This function calculate the square of each number on the list
    #     """
    #     return [i ** 2 for i in alist] # list comprehension

    n = len(arr)
    # arr = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    n = len(arr)
    # Base case 1
    if n == 0:
        print(arr)
    # Base case 2
    elif n == 1:
        print((arr[0])**2)
    else:
        print(arr[0]**2)
        if power_list_recursion_b(arr[1:]) == True: # Remove "None"
            print("test")
            # Get the square of each element in the list
            print((power_list_recursion_b(arr[1:]))**2)


def draw_polygon(sides, length, line_color, fill_color):
    """
    Draws a regular polygon with the given parameters.

    Parameters:
    sides (int): The number of sides of the polygon.
    length (int): The length of each side of the polygon.
    line_color (str): The color of the polygon's outline (as a string, e.g., 'blue').
    fill_color (str): The color to fill the inside of the polygon (as a string, e.g., 'red').
    
    """
    # pass
    # import turtle
    # https://docs.python.org/3/library/turtle.html
    # sides = int(input("How many sides does the polygon have?"))
    # length = int(input("What is the length of each side of the polygon?"))
    # line_color = str(input("What is the line color?"))
    # fill_color = str(input("What is the fill color?"))
    wn = turtle.Screen()
    # turtle.bgcolor('lightpink')
    t = turtle.Turtle()
    t.color(line_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    # Using a for loop to draw the polygon
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()
    # turtle.done() # Keep the window open
    # #turtle.reset()
    # turtle.exitonclick()
    #####################################################
    # # Clear the screen and reset the turtle's position - so we can start a new turtle
    # turtle.done()
    sleep(2)
    turtle.clearscreen()
    t.penup()
    t.home()
    # t.pendown()
    # turtle.exitonclick()

def problem_4():
    """
    Consider a program that iterates the integers from 1 to 50. For multiples of three
    print “Divisible by three” instead of the number and for the multiples of five print “Divisible by
    five”. For numbers which are multiples of both three and five print “Divisible by both”.
    """
    # pass
    for i in range(1,50):
        if i % 15 == 0:
            print(f"{i} is divisilbe by 3 and 5")
        elif i % 3 == 0:
            print(f"{i} is divisible by 3")
        elif i % 5 == 0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i}")

def problem_5():
    # pass
    """
    Write a program to draw some kind of picture. 
    Be creative and experiment with the turtle methods provided in Summary of Turtle Methods
    """
    # https://docs.python.org/3/library/turtle.html
    # import turtle
    wn = turtle.Screen()
    turtle.bgcolor('black')
    tt = turtle.Turtle()
    # 6 edge-stars
    # colors = ['purple', 'LightSlateBlue','DeepSkyBlue']
    # for i in range(300):
    #     tt.forward(i+1)
    #     tt.left(30)
    #     tt.back(i+1)
    #     tt.right(90)
    #     tt.pencolor(colors[i%3])
    # # Spiral 1
    # colors = ['purple', 'DeepSkyBlue']
    # for i in range(300):
    #     tt.forward(i+1)
    #     tt.left(88)
    #     tt.pencolor(colors[i%2])
    # # Spiral 2
    colors = ['purple', 'DeepSkyBlue','red']
    # colors = ['DeepSkyBlue','red']
    for i in range(300):
        tt.forward(i+1)
        tt.left(50)
        # tt.penup()
        tt.forward(i-1)
        tt.left(119)
        tt.forward(i+1)
        tt.left(58)
        tt.forward(i-1)
        tt.left(118)
        tt.forward(i+1)
        tt.left(57)
        # tt.pendown()
        tt.pencolor(colors[i%3])
    #     # tt.pencolor(colors[i%2])
    #turtle.reset()
    #####################################################
    # Clear the screen and reset the turtle's position - so we can start a new turtle
    # turtle.clearscreen()
    # tt.penup()
    # tt.home()
    # tt.pendown()
    #turtle.done()
    turtle.exitonclick()

def main():
    # call your functions here
    #turtle.exitonclick()

    #t = turtle.Turtle()
    n = 100
    print("Problem 1:")
    print("Print hello n times")
    print_hello(n)
    print("Print hello n times without using a loop")
    print_hello_alt(n)
    print("Print hello n time using recursion")
    print_hello_recursion(n)
    print("Problem 2: Print a list")
    arr = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    power_list(arr)
    print("Problem 2.a: Print a list using recursion")
    power_list_recursion_a(arr)
    print("Problem 2.b: Print the square of a list using recursion")
    power_list_recursion_b(arr)
    print("Problem 3: Draw a colorful polygon")
    draw_polygon(7,100,"purple","yellow")
    print("Problem 4: 1-50,the number that is divisible by 3 or 5 or both")
    problem_4()
    print("Problem 5: Draw an interesting shape with turtle")
    problem_5()
    
#main()
if __name__ == '__main__':
    main()