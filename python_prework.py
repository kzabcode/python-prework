# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of 
# the function.

def hello_name(user_name):
    print("hello_" + user_name.upper())

name = input("Please enter your username: ")
hello_name(name)

# Question 2
# Write a python function, first_odds that prints the odd numbers from
# 1-100 and returns nothing

def first_odds():
    numbers = list(range(1,100,2))
    print(numbers)

print(first_odds())

# Question 3
# Please write a Python function, max_num_in_list to return the max
# number of a given list.

def max_num_in_list(a_list):
    print(max(a_list))

number = 23,56,89
max_num_in_list(number)

# Question 4
# Write a function to return if the given year is a leap year. A leap
# year is divisible by 4, but not divisible by 100, unless it is also
# divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0:
        print("true")
    elif a_year % 100 == 0:
        print("false")
    elif a_year % 4 == 0:
        print("true")
    else:
        print("false")

year = int(input("Which year would you like to check is a leap year? "))
is_leap_year(year)

# Question 5
# Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers. The return should
# be boolean Type.


def is_consecutive(a_list):
    output = "false"
    for i in range(0, len(a_list)-1):
        if a_list[i]+1 == a_list[i+1]:
            output = "true"
        else:
            output = "false"
    print(output)

print("\n")
numbers = [1,2,3,4,5,6,7,8,9,11]
is_consecutive(numbers)

