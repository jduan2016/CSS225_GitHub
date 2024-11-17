## Professor: Linh Vu
# Student: Jia Duan
# Date: 11/15/2024
# CSS 225 - Assignment 8

def problem_1():
    """
    This function takes two inputs from a user and prints 
    whether they are equal or not.
    """
    while True:
        try:
            num1 = int(input("Give an integer."))
            num2 = int(input("Give another integer."))
        except ValueError:
            print("Not an integer. Please try again.")
            
        else:
            print("Problem 1:")
            if num1 == num2:
                print(f"{num1} and {num2} are equal.\n")
                break
            else:
                print(f"{num1} and {num2} are NOT equal.\n")
                break

def problem_2():
    """
    This function takes two inputs from a user and prints 
    whether the sum is greater than 10, less than 10, or equal to 10.
    """
    while True:
        try:
            num1 = int(input("Give an integer."))
            num2 = int(input("Give another integer."))
        except ValueError:
            print("Not an integer. Please try again.")
            
        else:
            print("Problem 2:")
            num_sum = num1 + num2
            if num_sum < 10:
                print(f"The sum of {num1} and {num2} is LESS than 10.\n")
                break
            elif num_sum == 10:
                print(f"The sum of {num1} and {num2} is EQUAL to 10.\n")
                break
            else:
                print(f"The sum of {num1} and {num2} is GREATER than 10.\n")
                break


def problem_3(target_num, alist):
    """
    This function takes a list and prints if the value 5 is in that list.
    """
    print("Problem 3:")
    if target_num in alist:
        print(f"{target_num} is in list {alist}.\n")
    else:
        print(f"{target_num} is NOT in list {alist}.\n")
    
def problem_4():
    """
    This function takes a year as a parameter and returns True if the year 
    is a leap year, False if it is otherwise.
    Consider the requirements of a leap year:
    -	The year is evenly divisible by 4
    -	If the year can be evenly divided by 100 it is NOT a leap year, unless:
        If the year is also evenly divisible by 400, then it is a leap year.

    """
    while True:
        try:
            test_year = int(input("Give a year you want to test if it is a leap year or not."))
        except ValueError:
            print("Not an integer. Please try again.")
        else:
            if test_year <= 0:
                print("Not a valid year - needs to be positive.")
            else:
                if (test_year % 4 == 0) and (test_year % 100 != 0):
                    print(f"{test_year} is a leap year.")
                    break
                elif (test_year % 400 == 0) and (test_year % 100 == 0):
                    print(f"{test_year} is a leap year.")
                    break
                else:
                    print(f"{test_year} is NOT a leap year.")
                    break

# Problem 5
class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses
    
    def does_player_have_weaknesses(self, bad_weaknesses):
        weaknesses_flag = False
        for weakness in bad_weaknesses:
            if weakness in self.weaknesses:
                weaknesses_flag == True
        return weaknesses_flag

    def does_player_have_required_weapons(self, required_weapons):
        weapons_flag = True
        for weapon in required_weapons:
            if weapon not in self.weapons:
                weapons_flag = False
        return weapons_flag
    
    def task1_climb_mountain(self):
        """
        Task 1: Climb a mountain: needs rope, coat, and first aid kit, cannot have slow
        """
        required_weapons = ['rope','coat','first aid kit']
        bad_weaknesses= ['slow']
        #########################################################
        if (self.does_player_have_weaknesses(bad_weaknesses) == False) and (self.does_player_have_required_weapons(required_weapons) == True):
            print("You climbed the mountain sucessfully!!!\n")
        else:
            print("You failed to climb the mountain!!!\n")
 
    def task2_cook_meal(self):
        """
        Task 2: Cook a meal: needs pan, groceries, cannot have small
        """
        required_weapons = ['pan','groceries']
        bad_weaknesses= ['small']
        #########################################################
        if (self.does_player_have_weaknesses(bad_weaknesses) == False) and (self.does_player_have_required_weapons(required_weapons) == True):
            print("You cooked a meal sucessfully!!!\n")
        else:
            print("You failed to cook a meal!!!\n")

    def task3_write_book(self):
        """
        Task 3: Write a book: needs pen, paper, idea, cannot have confusion
        """
        required_weapons = ['pen','paper','idea']
        bad_weaknesses= ['confusion']
        #########################################################
        if (self.does_player_have_weaknesses(bad_weaknesses) == False) and (self.does_player_have_required_weapons(required_weapons) == True):
            print("You wrote a book sucessfully!!!\n")
        else:
            print("You failed to write a book!!!\n")
        

# player1 = character('','','')
# player1.nickname = 'Dragon Slayer'
# player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
# player1.weaknesses = ['slow']
# for item in player1.weapons:
#     print("Item: ", item)

# for debuff in player1.weaknesses:
#     print("Debuff: ", debuff)

def main():
    problem_1()
    problem_2()
    # Test cases for problem 3
    target_num = 5
    alist1 = [-5,9,10,7,6]
    alist2 = [-5,9,10,7,5,10]
    alist3 = []
    problem_3(target_num, alist1)
    problem_3(target_num, alist2)
    problem_3(target_num, alist3)
    problem_4()
    # Problem 5
    player1 = character('','','')
    player1.nickname = 'Dragon Slayer'
    player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
    player1.weaknesses = ['slow']
    for item in player1.weapons:
        print("Item: ", item)
    for debuff in player1.weaknesses:
        print("Debuff: ", debuff)
    # Tests for different tasks
    player1.task1_climb_mountain()
    player1.task2_cook_meal()
    player1.task3_write_book()



if __name__ == "__main__":
    main()

