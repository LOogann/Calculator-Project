#add function
def add(a,b):
  return a + b

#subtraction fucntion
def sub(a,b):
  return a-b

#multiplication function
def mul(a,b):
  return a * b

#division function
def div(a,b):
  return a/b

#exponent functon
def exp(a,b):
  return a ** b

#function used for the input and final outputs
def calculate():
  
  typeCalc = str(input("Type of Calulation: "))

  #if "add" in typeCalc or "sub" in typeCalc or "mul" in typeCalc or "div" in typeCalc or "exp" in typeCalc and number2 <= 10:

  number1 = int(input("First Number: "))
  number2 = int(input("Second Number: ")) 
  finaloutput = None

#if statements for adding etc 
  if "add" in typeCalc:
      finaloutput = int(add(number1, number2))

  if "sub" in typeCalc:
      finaloutput = sub(number1, number2)

  if "mul" in typeCalc:
      finaloutput = mul(number1, number2)

  if "div" in typeCalc:
      finaloutput = div(number1, number2)

  if "exp" in typeCalc and number2 <= 10:
      finaloutput = exp(number1, number2)
  else:
    print("second number is not less than or equal to 10")


  # finaloutput = int(add(number1, number2))
  # print(finaloutput)
  # print(type(finaloutput))
  print(str(finaloutput))

calculate()
#calculate2()