#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:41:08 2020

Functional programming in python 


@author: travis nevins
"""
import math
from functools import reduce
from functools import partial
#imutablity will be mostly done by me not reasigning a varaibles
print("functional todo list exteremlly basic")
todo =[{
    "title": "code NumPy and Pandas",
    "done": False
    },{
    "title": "code basic ML using NumPy and Pandas",
    "done": False
    } ,{
    "title": "code Maze game using different ML solvers",
    "done": False 
    }]

def todo_list(todo_list):
    for i in todo_list:
        for key,value in i.items() :
            if key == "title":
                print(value)
            if key == "done" and value == True :
                print("completed task")
            elif key == "done" and value == False :
                print("not completed")
         
app = todo_list

app(todo)

print("functional with ternary operator")
ENV = "dev"

def fetching_real_data():
    print("fecthing real data")

def fetching_fake_data():
    print("ENV is in dev mode so fetching fake data")
    return   {
        "name" : "john doe",
        "age": 34
        }

fetching_data = fetching_real_data if ENV == "prod" else fetching_fake_data
data = fetching_data()
print("data returned: " ,data)
print("------------------------------------")
print("starting storing functions is lists")
#dispalying how to store functions in list 
def addOne(x):
     return x + 1
 
def squareIt(x):
    return x * x

def toThePowerOf(x):
    return x**2

def divide(x):
    return x / 7

num = 42
fun_list = [
    addOne,
    squareIt,
    divide,
    math.sqrt,
    toThePowerOf
    ]
for func in fun_list:
    print(func(num))

#function that gets passeda function 
print("--------------------")
print("function that takes in a parameter of a fucntion ")
def add(x , y):
    return x + y 
def subtract(x, y ):
    return x - y

def combine_2_and_3(func):
    return func(2,3)

print("add result: ", combine_2_and_3(add) )
print("subtract result: ", combine_2_and_3(subtract) )
#I think my python version ins pdier is messed up because it didn't recongize the f string formating
print("using strings example")
def change_Name(func):
    return func("Travis", "Nevins")
def nameWithSpace(str1 ,str2):
    return "{} {}".format(str1,str2)
def lastFirst(str1,str2):
    return "{}, {}".format(str2.upper() ,str1.upper())
print(change_Name(nameWithSpace))
print(change_Name(lastFirst))
print("--------------------------")
print("creating a function that makes other fucntions ")
print("in this casee I made a multipler function that created double - quardruple function ")
def create_maltiplier(x):
    def multiplier(y):
        return x * y 
    return multiplier 

double = create_maltiplier(2)
triple = create_maltiplier(3)
quadruple = create_maltiplier(4)
multiplier_list = [
    double,
    triple,
    quadruple
    ]
for func in multiplier_list:
    print(func(3))
    
print("--------------------------------")
print("functional count an exmaple of closure in python")

def create_counter():
    count = 0
    
    def get_count():
        return count
    def increment():
        #tell python use upper scopre coutne 
        nonlocal count 
        count += 1 
    return (get_count, increment)

get_count, increment = create_counter()
print(get_count())
i = 0 
while i < 6:
    increment()
    i += 1
print(get_count())  
for i in range(4):
    increment()
print(get_count())
print("------------------------")  
print("some more high order functions lets go!")
def unchecked_divide(x, y):
    return x / y
def check_input(func):
    def checking(*args):
        if args[1] == 0 :
            print("warning: second number is a zero and you can't divide by 0")
            return 
        return func(*args)
    return checking
checked_divide = check_input(unchecked_divide )
print("result: " , checked_divide(5, 14))
print( checked_divide(2,0) )
print("result: ", checked_divide(10,35))         
print("--------------------\-----------")
print("using map, filter, and reduce functions")

#calling the double function from eariler
#map returns map object rpa in a list to make python convert it to that 
test_data = [10,21,32,4,53,44,6,73,88,9,10,22]
print("orginal data list: ", test_data)
res = list(map(double,test_data))
print("map result: ", res)

def is_even(x):
    return x % 2 == 0
#filter 
res = list(filter(lambda x: x % 2 == 0 , test_data) )
print("is even filter with lambda resulte: ", res)

# accumulator then elements and last the starting point for accumulator  
# reduce(func , list, 0 )   func(acc , element )
def sum( acc, el):
    return acc + el 

res = reduce(sum, test_data)
print("reduce sumation result: ", res )

print("--------------------------")

"""
exmaple 1:  lambda x , y : x + y 
exmaple 2: def cretae_multiplier(x)
                return lambda x: x * a 
the above is the smae as eariler code but using lambdas 
using list comprehensions example:
        doubled = [x * 2 for x in test_data]
        even = [x for x in test_data if x % 2 == 0 ]
                ^ expression          ^ if true passes to element to epxression
 do all three in one line 
 developer_salaries = [employee["salary"] for employee in employees if employee['job_title'] == 'developer']

partial application 
basically if the parameters of say x y z and y and z mostly stay the same unless specified then we can write it functionally 
example: 
    def add_partial(x):
        def add_others(y,z)
            return x + y + z 
        return add_others
  add_5 = addpartial(5)
  print(add_5(6,7)) # return 18 this will add the others to 5 but this could be called anywhere which is pretty nice

you can also nest more than two 
 def out(x):
     def inner_1(y):
         def inner_2(z):
            return x + y +z
         return inner_2
     return inner_1  

calling the above 
    x = outer(5) # setting x
    y = x(6) #now setting y
    z = y(7) # setting z
"""

employees = [
    { 
     "name": "emp 1 ",
     "salary": 60000,
     "job_title": "developer"
     },
      { 
     "name": "emp 2 ",
     "salary": 70000,
     "job_title": "developer"
     },
        { 
     "name": "emp 3 ",
     "salary": 80000,
     "job_title": "developer"
     },
          { 
     "name": "emp 4 ",
     "salary": 76000,
     "job_title": "HR"
     },  { 
     "name": "emp 5 ",
     "salary": 60000,
     "job_title": "HR"
     }
    ]
    
#return salary of every eomployee that is a developer
         
#dev_salaries = [employee["salary"] for employee in employees if employee["job_title"] == "developer" ] 
# sum was defined earlier

def get_dev_salary():
    def get_salaary() :
        return [employee["salary"] for employee in employees if employee["job_title"] == "developer" ] 
    def avg(x, l) :
        return x / l
    return (get_salaary, avg)
        
get_salaries , avg = get_dev_salary()
salaries = get_salaries()
res = reduce( sum , salaries)

print("sum of salaries: ", res)
result = avg(res, len(salaries))
print("average of the salaries: ", result)

def adding_more(x , y ,z):
    return x + y + z

add_number_to_5 = partial(adding_more, 5,6)
result = add_number_to_5(7)
print("partil functools result: ", result)






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  






















































  
    
    
    
    
    
    
    