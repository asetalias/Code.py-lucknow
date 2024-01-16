import os
from calculator_logo import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
# The code `"+": add, "-": subtract, "*": multiply, "/": divide` is creating a dictionary called
# `operations`. Each key in the dictionary represents a mathematical operation symbol (`+`, `-`, `*`,
# `/`), and the corresponding value is the function that performs that operation (`add`, `subtract`,
# `multiply`, `divide`). This dictionary is used later in the code to look up the appropriate function
# based on the user's input.
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:#flag
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls')
      calculator()#recursion

calculator()
