###########################################################################
#                                                                         #
#                               LECTURE NO. 1                             #  
#                          [Variables & Data Types]                       #
#                                                                         #
###########################################################################


###################################################################

# practicing strings

###################################################################

# print("my name is muhammad awais aslam")
# print("i am expert in python")

# print("my name is awais aslam.", "i am python expert")
# print(25)
# print(20+25)



###################################################

# practicing variables

###################################################

# name = "awais"
# age = 27
# price = 28.5

# print(name)
# print(age)
# print("my name is", name, "my age is", age)

# age2 = age
# print(age)
# print(age2)

# print(type(name))
# print(type(age))
# print(type(price))

##################################################

# variable types

##################################################


# name = "awais"
# age = 27
# old = True
# a = None

# print(type(name))
# print(type(age))
# print(type(old))
# print(type(a))


##################################################

# print sum

##################################################

# a = 15
# b = 10

# sum = a + b
# div = a / b
# diff = a - b
# mutiply = a * b

# print(sum)
# print(diff)
# print(div, mutiply)


"""

WE are adding this test comment
to test
multi-line comment,

We can add it by using triple quotes (either single or double, both works)

"""

###################################################

# OPERATORS

# arithmetic operators

###################################################

# a = 5
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)  # remainder
# print(a ** b) # a^b


####################################################

# relational operators

####################################################

# a = 50
# b = 20

# print(a == b) # it should say False, as a is not equal to b
# print(a != b) # True
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)


####################################################

# assignment operators

# when we assign a=5, num=10, etc...

####################################################

# num = 10
# # num = num + 10 ######---> same like +=
# num += 10  # will give  20
# num -= 10  # will give result by subtracting 10 from value of num
# num *= 10  # will give value by multiplying 10 with value of num
# num /= 10  # read above and so on...
# num %= 4
# num **= 5
# print("num :", num)


####################################################

# logical operators

# ---> and, or , not
####################################################

# print(not True)   # not operator will reverse the output each time
# print(not False)

# a = 50
# b = 20
# print(not (a > b))

# val1 = True
# val2 = False
# val3 = True

# print("AND operator:", val1 and val2)  # "and" only returns true if all values are True
# print("OR operator:", val1 or val2)  # "OR" will return True if any value  is True

# print("OR operator:", (a == b) or (a >= b))


####################################################

# Type Conversion (automatic type conversion and type casting)

####################################################

## type conversion


# a = 2
# a = "2"
# """
# here, if we write a = "2", here the value becomes string, som function will not run

# so in this case we use type casting to forcefully change the type of a value as:

# a = int("2")

# """

# n = int("2")
# b = 4.5
# sum1 = a + b
# sum2 = n + b

# print(type(n))
# print(type(sum1), sum1)
# print(type(sum2), sum2)


####################################################

# INPUTS

####################################################

# input("enter you name: ")

# name = input("enter your name: ")
# print("Welcome ", name)

# age = input("enter your age: ")
# print("you entered ", age)

# val = input("enter some value :")  # test with inputs like abc(str), 123(int), 99.99(float), etc
# print(type(val), val)    # by default whenever input() takes any value, it converts its type to str, so if we want another type we use type case for our input function as below:

# val = int(input("enter some value: "))   # it will now only accept int as input
# print(type(val), val)

# val = float(input("enter some value: "))   # it will now only accept int and float as input but will change their type to float
# print(type(val), val)


# name = str(input("enter name: "))
# age = int(input("enter age: "))
# marks = float(input("enter marks: "))

# print("your name is", name)
# print("your age is", age)
# print("your marks is", marks)

#########################################################

# PRACTICE TIME

#########################################################

# Q1: Write a prg to input 2 numbers and print their sum.

# val1 = float(input("first number: "))
# val2 = float(input("second number: "))
# sum = val1 + val2
# print("sum of your two numbers is ", sum)

# Q2: WAP(write a program) to input side of a square and print its area.

# a = float(input("enter one side of square "))
# area = a * a
# print("area of your square is ", area)

# Q3: WAP to input 2 float numbers and print their average

# a = float(input("first number: "))
# b = float(input("second number: "))
# avg = (a + b) / 2
# print("average of your two numbers is", avg)

# Q4: WAP to input 2 int numbers a and b, print True if a is greater than or equal to b, if not print False.

# a = int(input("first number: "))
# b = int(input("second number: "))
# print(a >= b)

###########################################################################
#                                                                         #
#                               LECTURE NO. 2                             #  
#                     [Strings & Conditional Stetements]                  #
#                                                                         #
###########################################################################


'''
String:
It is a data type that stores a sequence of characters.

Basic Operations may include:

- Concatenation

    "hello" + "world"  ------> "helloworld"

- lenth of str

    len(str)

    
Escape Sequence Character:
used for special purposes like next line(\n), etc

'''

# str1 = "This is a string."
# str2 = 'Devops'
# str3 = """this is also a string"""
# str4 = "this is Pakistan's flag"

# print(str3)

str0 = "This is the first line. This will not be second line"
print(str0)

# to insert next line we user \n
str5 = "This is the first line.\n This should be second line"
print(str5)

str6 = "This is the first line.\nThis should be second line"
print(str6)

# to insert tab space we use \t
str7 = "This is the first line.\tThis line is after tab"
print(str7)