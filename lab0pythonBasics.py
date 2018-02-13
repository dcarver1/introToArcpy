'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Purpose: Introduction to python
*********************************************'''

#Declaring variables:
#variables are declared with a single equal sign
#numbers:
a = 3
b = 4
c = 1.5
#characters (referred to as strings and enclose in quotes)
#single (') and double (") quotes are treated the same"
d = 'hello'
e = " world"
#note: a space is also a character, as well as numbers

#this is a string, not a number:
f = '123'
#you can convert between data types:
cc = str(c)
ff = int(f)
aa = float(a)
#note: int is for integer, str is for string, float is for ... guess

#and only if logically possible: you can't convert letters to numbers, but you can
#convert numbers to characters (i.e. a string object):
dd = int(d)

#note: Don't use names for variables that already exist in python. Obviously you 
#don't know all the names you cannot use, but just be aware of this as you learn
#python (e.g., don't use int, str, or float as variable names)
#Also, variable names cannot start with a number (i.e. 1stVar is not valid)

#arithmetic:
a+b
b-c
a*b

a/b
a/c
#Do these two operations return what you were expecting?

#this is a build-in function:
type(a)
type(c)
#these are called data types. There are many and you will
#become more familiar with how each behaves as we move along

#raise a number to a power with **
a**2

a+d
#what happend here? Why?
d+e
#why does this work?

#concatenation:
cat1 = d+e
#we already saw this
cat2 = d+e+str(c)
#you must convert numbers to a string before concatenation

#lists:
l1 = [1,2,3]
#this is a list, simply it is a collection of objects,
#referred to as elements of the list
l2 = ['a','b','c']
#lists can contain numbers or strings (or any other data type)
l3 = ['abcd',1,'2',3.4,'3d']
#or a combination of different data types
#you can access the elements of a list by what is called indexing:
l1[0]
#this returns the first.
#note: indexing (and counting in general) starts at zero in Python,
#more on this later 

l1[1]
#this returns the second element of the list, from now on
#lets call this index 1 rather than element 2, to avoid
#confusion
l1+l2
#this joins the two lists together

#You can use the range function to create a sequenced list:
r1 = range(5)
#this is just an easy way of creating a list of a sequence of integers
#the range function starts at 0 if only one parameter is given, and it creates
#a sequenced list up to BUT NOT including that number.
r2 = range(1,5)
#if you give two parameters, the first is the starting number and the second is
#the stopping number, BUT it counts up to but not including the stop number
#in formal notation it is: [1,5)
#this is consistent across Python and external modules
r3 = range(0,10,2)
#if you give a third parameter, it will count in increments of the third 
#parameter. Why isn't 10 included in the list?
#Think about the logic of this function and play around with it.

l4 = []
#this is an empty list
l4.append(1)
#this is one way of populating the list, and is your first method
#Objects have methods and properties, these terms are intuitive
#a method is something the object can do, a property tells you 
#something about the object. We will come back to methods and 
#properties throughout the semester.
l5 = [4,2,5,2,3,5,55]
l5.sort()
l5
#this is a method, which changes the order of the object

#certain functions can also tell you things about an object
len(l3)
#this returns the number of elements in the list
len(d)
#what does this return?
len(l3[0])
#what about this?

#Booleans:
#boolean is a datatype, and an important one
#take this simple example:
g = 3
a==g
#the double equal sign tests if the two objects are equal
#this is a logical operator
b==g
h = a==g
#h is a boolean object
i = b==g
#be careful with single and double equal signs, they are
#very different

#boolean variables are a little odd, they are True/False values,
#but they can be calculated as numeric values, in which case True is 1 and
#False is 0
h+i
h*i
h/i
#can't divide by zero
#how about "not equal", another logical operator. ! means "not"
a!=g
b!=g
#think about the logic behind this
b<>g
#this is the same as !=
a<g
h>i
a<=g
#more logical operators

#what were these variables again?
a;g;h;i
#you can return the values of multiple variables at once with the semicolon
j,k = 123,'abcdef'
#you can declare multiple variables on the same line with commas
#don't do this too much, it can become hard to read with complicated programming

#back to logical operators
'a' in k
#this tests if the character 'a' is in the string k
'abcd' in l3
#works with lists as well
'a' in l3
#why is this False?
l3
'a' in l3[4]
#How about this?

#the print function
print a
#or
print(a)
print d+e+str(c)
#to concatenate these in a print statement, all must be the same data type
print d,e,c
#or you can use commas to print multiple object together on the same line

#looping:
#there are two kinds of loops: for and while
#for loops:
for i in k:
    print i

#this is a fundamental structure in programming
#you can read this as "For each element in k, print that element."
#you just learned about the 'in' operator, now we use it with interation
#'for' and 'in' establish the structure of the for loop
#i is what we call the iterator variable. You can call it anything you want, i
#is just a convention. But don't use names that already exist in python
#k is an iterable object. An iterable object is one that is a collection of
#objects, such as lists or strings. Numbers are not iterable objects.
for elem in l3:
    print elem

for i in range(len(l3)):
    print 'index:'
    print i
    print 'value:'
    print l3[i]

#Think about how these two examples are different. What is the iterator variable
#in each?
#This seems like a simple difference, but it's powerful in application.

#an enumeration is a listing of the elements in an iterable object
#you can use the function enumerate() within a loop
for i,elem in enumerate(l3):
    print 'the i iterable is:',i,'the elem iterable is:',elem

for i,elem in enumerate(l3):
    print i,elem

#enumerate() creates a counter starting at 0 for each element of the iterable
#object (the i iterator variable) and iterates through each element of the
#object (the elem iterator variable), so you have two iterator variables.
#enumerate() is an odd function, you probably won't use it in another way, but
#understanding the concept of enumeration is fundamental.

#How about a more complicated example
myList = []
for char in d:
    myList.append(char)

myList
#this splits the string d into a list

#a little more complicated:
l4 = [-3,-2,-1,0,1,2,3]
for i,num in enumerate(l4):
    print i,'is less than',abs(num)
    #abs() is a builtin function for absolute value    
    print i<abs(num)
    #This just prints the result of the logical operator, a boolean.

#a while loop tests a condition before each iteration and only continues if that
#condition is true.
cntr = 0
while cntr<5:
    print cntr
    cntr = cntr+1

#while loops do not have explicit iterator variables like for loops. Sometimes
#a counter is used instead, like I did in this example. cntr is initiated at 0
#and then it is redeclared as the value it had previously plus 1. Think through
#the logic in this example. The while loop stops when the condition is no longer
#true (i.e. when cntr is no longer less than 5).

l4 = [-3,-2,-1,0,1,2,3]
i = 0
while i<abs(l4[i]):
    print i,'is less than',abs(l4[i])
    i += 1
    #this syntax is the same as i = i+1

#one more while loop example
l5 = [7,6,5,4,3,2,1] 
cntr = 0
while abs(l4[cntr])<l5[cntr]:
    print abs(l4[cntr]),'is less than',l5[cntr]
    cntr += 1

#think through the logic.

#Branching:
#branching is a way of setting up different procedures for different conditions.
#The if statement is tested. If it is true, then python enters the indented lines.
#If it is false, python continues to the else and enters those indented lines.
x = 3
if type(x)==int:
    print 'x is an integer'
else:
    print 'x is not an integer'

#read this as: if x is an integer print 'x is an integer', if not then print
#'x is not an integer'

x = 1.5
if type(x)==int:
    print 'x is an integer'
elif type(x)==str:
    print 'x is a string'
else:
    print 'x is not an integer nor a string'

#you can have as many elif statements as you want and you don't actually even
#need the else statement.

years = range(2000,2013)
if 2013 not in years:
    years.append(2013)

#not can be used with the in operator

#the raw_input() function:
yourName = raw_input('What is your name? ')
yourName
#this allows the user to enter a value during the execution of a script.
#by default it will be a string, no matter what is entered.
myFloat = float(raw_input('Enter a floating point number: '))
#of course you can convert this variable to any type you want.

#looping and branching:
cont = True
number = 4
while cont:
    guess = int(raw_input('guess a number: '))
    if guess==number:
        cont = False
        print 'Correct!'
    else:
        print 'Try again.'

#the structure: while cont: means that as long at cont is True, the loop will
#continue. This is a special use of a while loop and a Boolean variable. Notice
#that True (with capital T) is a Boolean value in python, as is False.

#more data types
#Tuples:
t1 = (1,2,3)
#this is a tuple, its just like a list, but it's immutable
#a list is mutable, meaning that the elements can be changes
l5
l5[0] = -99
l5
#list elements can be changed; a list is mutable

t1[0] = -99
#tuple elements cannot be changed; a tuple is immutable
#otherwise, lists and tuples behave about the same

#Dictionaries:
dict1 = {'one':0.3423,'two':1.3432,'three':2.42134}
#dictionaries are similar to lists and tuples in that they store sets of values.
#dictionaries are organized by keys. Think of each element as a variable name
#and a variable value. Keys can be strings or numbers. Dictionaries are declared
#using {}, and each element follows the key:value structure, separated by commas
dict1['three']
#to access a value, you use square brackets and the key

dict2 = {1:312,'2':5234,22:'bob','seven':1432}
#dictionaries can hold any data type and keys can be strings or numbers.
#You should have some sort of system though and avoid the above example

dict3 = {'set1':[1,2,3],'set2':[4123,3214,551],'set3':2}
#dictionaries can have lists as values, for example

#There are many other data types. We will continue to introduce new ways of 
#storing data.

#another for loop example
samples = range(2000,2013)
results = [0.23,0.31,0.4,0.43,0.41,0.45,0.51,0.5,0.57,0.61,0.66,0.71,0.76]
outDict = {}
for i,yr in enumerate(samples):
    outDict[yr] = results[i]

outDict
outDict[2002]

#modules
#there are many modules that come installed with python which you can import and
#use. Other modules you will have to install first if you want to use them. You
#can also create your own modules.
import math
#this is the simplest way to import modules. You need to use the name of the
#module first, then dot (.), and the function or property from the module.
math.pi
#the number pi is stored in the math module as a property
n1 = 123
math.sqrt(n1)
#this method (aka function) takes the square root of a numeric variable
n1**0.5
#this does the same thing without the math module
math.cos(n1)
#return the cosine of n1

from math import pi
pi
#pi can now be used without typing math.pi
from math import *
sqrt(n1)
#this means from the math module import everything. This can be overwhelming
#with large modules. It also can cause problems when two modules have a function
#with the same name. I usually only import everything from modules I write.
#Stick with the first two import options at first.

import os
#This is the operating system module. It's very useful.
path = r'C:\GEOG4303\labs2013'
#This is a string, just a string. However, it points to a path or directory on
#my computer. Change this path to a directory on your computer
#You put the r before the string to specify what is called a 'raw' string. This
#is necessary when using Python on a Windows machine because Windows uses back
#slashes to separate elements of the path. You can also use double back slashes
#(\\) instead of the raw string. It would look like this: path = 'C:\\gis3\\lab0'
#raw strings cannot end with a back slash. If you want your path to end with a
#backslash, use a double backslash (i.e. r'C:\gis3\lab0\\'
files = os.listdir(path)
#this will create a list with all the files and folders in that directory.
sorted(files)
#sort that list
os.mkdir(path+'\newFolder')
#This creates a new directory (folder) in my path directory
os.listdir(path)
#List contents of path
os.rmdir(path+'\newFolder')
#Remove the directory we just made
os.listdir(path)

os.remove(path+'\junk.txt')
#removes the file junk.txt, if it exists. Otherwise python throws an error.
#os has a number of miscellaneous functions that interact with the operating
#system. Play around with it a little, but don't delete anything important.

#opening text files:
txt = open(path+'/lab0/data/lab0.txt','r')
#the open function simply opens the text file and saves it as a file object in Python
#the second argument specifies that you are in 'reading' mode
firstLine = txt.readline()
#readline is a method of a file object; it reads the next line (the first line).
secondLine = txt.readline()
#this continues and reads the next line of the file object

#read all lines at once:
txt.seek(0)
#reset to the first line of the text file. Otherwise it will read all lines from
#where it was, i.e. the third line)
txt.readlines()
#this reads all lines into a list.

txt.close()
#when you are done with the file object, you should always close the file.

#list comprehensions:
years
lc1 = [yr-2000 for yr in years]
#create a new list of just the last two digits of the years.
#list comprehensions are just a short cut for building a list
#here is how you would do it without using a list comprehension:
lc1 = []
for yr in years:
    lc1.append(yr-2000)

#Examine this example to understand how the list comprehension works as
#a short cut for the loop.

lc2 = [(i,elem) for i, elem in enumerate(l3)]
#This will create a list of tuples each containing the index and element of
#each element is l3.

#list comprehension with branching:
t2 = ('a',1,'b',1.32,'c',3.2,'d',22,'e',43.23,'f',32.32,'g')
letters = [i for i in t2 if isinstance(i,str)]
#you can combine looping and branching within a list comprehension

letters = []
for i in t2:
    if type(i)==str:
        letters.append(i)

#this is the same thing without using a list comprehension

#The end!
