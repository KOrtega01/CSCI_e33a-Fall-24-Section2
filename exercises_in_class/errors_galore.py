# This page has python style errors
import datetime, date   //you can't have multiple imports in one line
//line 4 is too long
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Habitant morbi tristique senectus et. Felis eget velit aliquet sagittis id consectetur.
def foo(a,b,c):  // you need a space after commas
   x = a ** c  
   y =b ** c  // need space
   if (x+y)> 400:
      print("It's greater than 400!")
   elif (x+y) < 400:
      print("It's less than 400")
   else:
      print("It's 400")


foo (3, 2, 2)  //there should not be a space

def bar(x, y):
   return x + y  
class AnyClass:   //you need a space
   pass

                  // too many spaces

def foobar(x, y):
   return x * y

def StyleFunction():   /declaration of function it does nothing should be lower case
   pass


baz = foo
if baz == None:  #"is" instead of "==" in python
   pass


if x == 1: print("x is 1") //only one line

#the quotes below
dict = {'key1': 'value1', "key2": "value2", 'key3': 2001}
dict['key1'] = dict ['hello']


def sample (arg2, arg3):
    return arg2 + arg3
