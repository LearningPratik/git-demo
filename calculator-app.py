from helper_functions import *

def calc():

  print('Welcome to calculator app')
  usr = input('''Choose an operation
              1. type 1 for add
              2. type 2 for subtract
              ''')
  num1 = int(input('Enter first number : '))
  num2 = int(input('Enter second number : '))

  if usr == '1':
    res = do_add(num1, num2)
  elif usr == '2':
    res = do_sub(num1, num2)

  return res


if __name__ == '__main__':
  print(calc())