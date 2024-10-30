## Professor: Linh Vu
# Student: Jia Duan
# Date: 10/30/2024
# CSS 225 - Assignment 6
import random
import math

def problem_1():
    """
    Use a for statement and random.randrange to return 10 random integers
    between 25 and 35
    """
    a = 25
    b = 35
    for _ in range(10):
        print(random.randrange(a,b))


def problem_2():
    """
    Use random.randrange to return an odd integer between 0 and 100.
    """
    a = 0
    b = 100
    print(random.randrange(a,b,1)) # step = 2 to get even integer
    
    
def problem_3():
    """
    Use random.choice to select a day of the week from a list and return that day
    """
    days = ["Sunday", "Monday", "Tuesday", "Wednedsay", "Thursday", "Friday", "Saturday"]
    print(random.choice(days))

def pi_approximation():
    """
    Search on the internet for a way to calculate an approximation for pi. There are
    many that use simple arithmetic. Write a program to compute the approximation and then
    print that value as well as the value of math.pi from the math module
    """
    print(f"The pi caluclated by math.pi is: ",math.pi)
    # https://www.wikihow.com/Calculate-Pi
    # x * sin(180 / x), where x is a large number
    large_number = 999999
    new_pi = math.radians(large_number * math.sin(180/large_number))
    print(f"The pi by approximation is: {new_pi}")



def conversion(rad):
    """
    Search the internet for how to convert radians to degrees. Write a program to
    compute the conversion given a rad. Print this value as well as the calculated value
    using the degrees function in the math module
    """
    # https://www.wikihow.com/Convert-Radians-to-Degrees
    # 1 radian = 180/pi
    deg = rad * 180/math.pi
    print(f"The degrees by math.degrees is: ",math.degrees(rad))
    print(f"The degrees by approximation is: {deg}")

def factorial_iterative():
    """
    Use a for statement to calculate the factorial of a n
    """
    num = int(input("Give a non-negative integer: "))
    fac = 1
    for i in range(1,num+1):
        fac = fac*i
    print(f"Factorial for {num} by our iterative function is {fac}")
    print(f"Factorial by math.factorial is", math.factorial(num))

    
def factorial_recursive(n):
    """
    extra credit: 5 points
    feel free to change anything in this
    """
    # def print_fac(n,fac):
    #     print(f"Factorial for {n} by our function is {fac}")
    #     print(f"Factorial by math.factorial is", math.factorial(n))

    # base case:
    if n == 0:
        return 1
        #print_fac(n,fac)
    elif n == 1:
        return n
        #print_fac(n,fac)
    else:
        return n * factorial_recursive(n-1)
        #print_fac(n,fac)
    

def main():
    # call your functions here
    print("Problem 1:\n")
    problem_1()
    print("Problem 2:\n")
    problem_2()
    print("Problem 3:\n")
    problem_3()
    print("Problem 4 - pi approximation:\n")
    pi_approximation()
    print("Problem 5 - convert radians to degrees:\n")
    conversion(3.14)
    print("Problem 6.1 - factorial with iterative:\n")
    factorial_iterative()
    print("Problem 6.2 - factorial with recursive:\n")
    n = 6
    #factorial_recursive(n)
    print(f"Factorial for {n} by our recursive function is {factorial_recursive(n)}")
    print(f"Factorial by math.factorial is", math.factorial(n))
   


if __name__ == "__main__":
    main()
