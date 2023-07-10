#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    if count == 0:
        print ("Happy New Year!")


def square_integers(int_list):
   new_array = [i*i for i in int_list]
   return new_array
   

def fizzbuzz():
   i = 1
   while i < 101:
        if (i%3 == 0 and i%5 == 0):
           print("FizzBuzz")
        elif (i%5 == 0):
           print("Buzz")
        elif (i%3 == 0):
           print("Fizz")
        else:
           print(i)
        i +=1