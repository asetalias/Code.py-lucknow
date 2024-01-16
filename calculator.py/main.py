import os
from calculator_logo import logo
print(logo)
def calculation(op1, op2, operator):
    if operator == '+':
        result = op1 + op2
        return f"{op1} + {op2} = {result}", result
    elif operator == '-':
        result = op1 - op2
        return f"{op1} - {op2} = {result}", result
    elif operator == '*':
        result = op1 * op2
        return f"{op1} * {op2} = {result}", result
    else:
        result = op1 / op2
        return f"{op1} / {op2} = {result}", result

def operations1():
  num1 = float(input("Enter the first number: "))
  print("\n+\n-\n*\n/")
  operator = input("What operation would you like to perform?: ")
  num2 = float(input("Enter the seconde operator: "))
  final_result = calculation(num1, num2, operator)
  print(final_result[0])
  return final_result
def operations2(op1):
    print("\n+\n-\n*\n/")
    operator = input("What operation would you like to perform?: ")
    num2 = float(input("Enter the seconde operator: "))
    num1 = op1
    final_result = calculation(num1, num2, operator)
    print(final_result[0])
    return final_result

final_result2 = operations1()

run = True 
while run:
  choice = input(f"Type 'y' to continue calculating with {final_result2[1]}, or type 'n' to start a new calculation,\n type 'exit' if you want to end the operations:\n")
  if choice == 'y':
     final_result2 = operations2(final_result2[1])
     print("final_result2" in globals())
  elif choice == 'n':
     os.system('cls')
     final_result2 = operations1()
  elif choice == 'exit':
     print("Thank you.")
     break
  else:
     print("You typed something wrong try again.")
     continue