# calculator that can add, multiply, subtract, divide and modulus of inputs
def calculator():
  print("Welcome to the calculator")
  print("Please select an operation")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Modulus")
  print("6. Quit")
  try:
    operation = int(input("Enter number: "))
    if operation == 1:
      number1 = int(input("Enter first number: "))
      number2 = int(input("Enter second number: "))
      print("Answer:",number1 + number2)
      calculator()
    elif operation == 2:
      number1 = int(input("Enter first number: "))
      number2 = int(input("Enter second number: "))
      print("Answer:",number1 - number2)
      calculator()
    elif operation == 3:
      number1 = int(input("Enter first number: "))
      number2 = int(input("Enter second number: "))
      print("Answer:",number1 * number2)
      calculator()
    elif operation == 4:
      number1 = int(input("Enter first number: "))
      number2 = int(input("Enter second number: "))
      print("Answer:",number1 / number2)
      calculator()
    elif operation == 5:
      number1 = int(input("Enter first number: "))
      number2 = int(input("Enter second number: "))
      print("Answer:",number1 % number2)
      calculator()
    elif operation == 6:
      print("Goodbye")
      exit()
    else:
      print("Please enter a valid number")
      calculator()
  except ValueError:
    print("Please enter only numbers")
    calculator()
calculator()