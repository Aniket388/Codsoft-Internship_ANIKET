def calculator():
  print("Simple Calculator")

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  print("Select operation: +, -, *, /")
  operation = input("Enter operation: ")

  if operation == '+':
      print(f"The result is: {num1 + num2}")
  elif operation == '-':
      print(f"The result is: {num1 - num2}")
  elif operation == '*':
      print(f"The result is: {num1 * num2}")
  elif operation == '/':
      if num2 != 0:
          print(f"The result is: {num1 / num2}")
      else:
          print("Error! Division by zero.")
  else:
      print("Invalid operation!")

if __name__ == "__main__":
  calculator()
