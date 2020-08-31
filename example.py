#!/usr/bin/python3
import menu
import os
import lib

# making it quicker to use the option class in the menu package
o = menu.option

#define a function for an option (can also be imported from another python script)
def test1fun():
  print('test 1 works')
  
# define a function for another option (again can be imported from another python script)
def test2fun():
  print('test 2 works')

#create the option object for test1
test1 = o(lib.test.test1.main, 'test1')

#create the option object for test2
test2 = o(lib.test.test2.main, 'test2')

#create a list of option objects for the main menu
main_options = [test1, test2]

#create the main menu object
main = menu.menu(main_options, 'main')

#call the display method for the main menu object
main.display()
