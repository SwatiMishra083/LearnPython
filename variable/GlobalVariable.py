#30-1-2022
#global variable
#declare a variable and initialize it
x=101

#global variable in function
def mainFunction():
  #printing a global variable
  global x
  print(x)
  #modifying a global variable
  x = "Welcome To swati's python series"
  print(x)

mainFunction()
print(x)