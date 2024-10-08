# Professor: Linh Vu
# Student: Jia Duan
# Date: 10/07/2024
# CSS 225 - Assignment 3

# Remember to comment for each function
import math 

def print_hello():
    # TODO: Print "Hello World"
    # This function prints "Hello World"
    print("\nHello World")
    pass

def hello_user(name="User"):
    # TODO: Print "Hello, their_name"
    # This function asks the user for their name and greets them with their name
    name = str(input("\nWhat is your name? "))
    print("\nHello" + " " + name)
    pass

def hello_user_specific(name="User"):
    # This function asks the user for their name and only greets professor Linh and Jia with their names
    name=str(input("\nWhat is your name? "))
    if name == "Jia":
        print("\nHello" + " " + name)
    elif name == "Linh":
        print("\nHello Professor" + " " +name)
    else:
        print("\nInvalid user")

def get_circle_area(radius=0):
    # TODO: print a message back with the answer
    # This function computes the area of a circle with the user's choice of radius
    radius=float(input("\nWhat is the radius?\n"))
    area = math.pi*pow(radius,2)
    print("\nThe area is: %.2f" % area + ".") # Convert the float with 2 decimal places
    pass

def get_miles_per_gallon(miles=1, gallons=1):
    # TODO: print out the MPG for the car
    # This function calculates MPG with the user's choice of miles driven and gallons used
    miles = float(input("How many miles you've driven? "))
    gallons = float(input("How many gallons of gas you've used? "))
    if miles <= 0 or gallons <= 0 :
        print("\nPlease enter a positive number")
    else:
        mpg = miles/gallons
        print("\nMPG is: %.2f" %mpg + ".") # Convert the float with 2 decimal places
    pass
    
def convert_temperature(temperature_F=32):
    # TODO: return the coverted temperature in Celcius
    # This function converts degrees Fahrenheit to degrees Celsius
    temperature_F = float(input("What is the degrees in Fahrenheit? "))
    temperature_C = (temperature_F - 32)*9/5
    print("\nThe degrees in Celsius is: %.2f" % temperature_C)
    pass

def problem_7(starting_day=0, length_of_stay=0):
    # TODO: Implement the function as the problem statement
    # This program asks for the starting day number, and the length of the stay, and it will tell the user the number of day of the week to return.
    print("\n0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday \n")
    starting_day = int(input("What's number of the day?\n"))
    length_of_stay = int(input("What's the number of days to stay?\n"))
    day_of_week_num = (starting_day + length_of_stay) % 7
    day_of_week = "Sunday"
    if day_of_week_num == 0:
        day_of_week = "Sunday"
    elif day_of_week_num == 1:
        day_of_week = "Monday"
    elif day_of_week_num == 2:
        day_of_week = "Tuesday"
    elif day_of_week_num == 3:
        day_of_week = "Wednesday"
    elif day_of_week_num == 4:
        day_of_week = "Thursday"
    elif day_of_week_num == 5:
        day_of_week = "Friday"
    else:
        day_of_week = "Saturday"

    print("You will be return on " + str(day_of_week_num) + ", which is a " + day_of_week + "\n")
    pass

def extra_credit_problem_1():
    start_year = 1900
    end_year = 2100
    # TODO: Write a program to print leap years from the year 1900 to 2100
    # 5 points extra credits
    # This function checks if the year is a leap year between 1900 abd 2100
    # Leap Year:
    # A leap year is divisible by 4 and not by 100, or it is divisible by 400.
    # https://www.programiz.com/python-programming/examples/leap-year
    def check_leap(year):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            #print(year)
            return year
        else:
            return 0
    # Initiate an empty list for leap year
    leap_year = []
    for year in range(start_year, end_year +1):
        if check_leap(year):
            leap_year.append(year) #Adding leap year to the list
    print("\n The leap years between 1900 and 2100 are: \n")
    print(leap_year)
    print("\n")
    pass

def extra_credit_problem_2(n=1):
    # a prime number is a natural number greater than 1, that can only divisible by itself and 1
    # 10 points extra credits
    # TODO: given the number n, check if n is a prime number
    # This function checks if the given number is a prime number
    n = int(input("\nEnter an integer "))
    # Initiate is_prime as true
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        print("\n" + str(n) + " is a prime.\n")
    else:
        print("\n" + str(n) + " is NOT a prime.\n")






    pass


def main():
    # prompt user to get the input then call functions
    print_hello()
    hello_user()
    hello_user_specific()
    get_circle_area()
    get_miles_per_gallon()
    convert_temperature()
    problem_7()
    extra_credit_problem_1()
    extra_credit_problem_2()
    
main()


    


