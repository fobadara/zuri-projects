def add_integers():
  try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    
    print("Answer:",number1 + number2)
  except ValueError:
    print("Please enter only numbers")

add_integers()