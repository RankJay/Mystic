import math

class mathOperations:
  def cMathOperations(inputFromUser, outputFromUser):
    inputFromUser=float(inputFromUser)
    outputFromUser=float(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'pow(variable1, 2)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'ceil(variable1)'

  def cPlusMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'pow(variable1, 2)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'ceil(variable1)'
  
  def pythonMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'math.sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'math.pow(variable1, 2)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'math.floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'math.ceil(variable1)'
  
  def javaMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'Math.sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'Math.pow(variable1, 2)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'Math.floor(variable1)'
    elif(math.ceil(inputFromUser)+1==outputFromUser):
      return 'Math.ceil(variable1)'
