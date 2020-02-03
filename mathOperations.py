import math

class mathOperations:
  def cMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'pow(variable1, 2)'

  def cPlusMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'pow(variable1, 2)'
  
  def pythonMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'math.sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'math.pow(variable1, 2)'
  
  def javaMathOperations(inputFromUser, outputFromUser):
    inputFromUser=int(inputFromUser)
    outputFromUser=int(outputFromUser)
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'Math.sqrt(variable1)'
    elif(inputFromUser**2==outputFromUser):
      return 'Math.pow(variable1, 2)'
