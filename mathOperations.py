import math
import accessNaturalNumbers

access_iter=iter(accessNaturalNumbers.NaturalNumbers)

class mathOperations:
  def cMathOperations(inputFromUser, outputFromUser):
    inputFromUser=float(inputFromUser)
    outputFromUser=float(outputFromUser)
    try:
      while True:
        if (round(inputFromUser**(access_iter.__next__()))==outputFromUser):
          function = 'pow(variable1, '+ str(access_iter.__next__()-1) +')'
          return str(function)
    except:
      pass
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'sqrt(variable1)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'ceil(variable1)'
    else:
      return '0'

  def cPlusMathOperations(inputFromUser, outputFromUser):
    inputFromUser=float(inputFromUser)
    outputFromUser=float(outputFromUser)
    try:
      while True:
        if (inputFromUser**(access_iter.__next__())==outputFromUser):
          function = 'pow(variable1, '+ str(access_iter.__next__()-1) +')'
          return str(function)
    except:
      pass
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'sqrt(variable1)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'ceil(variable1)'
  
  def pythonMathOperations(inputFromUser, outputFromUser):
    inputFromUser=float(inputFromUser)
    outputFromUser=float(outputFromUser)
    try:
      while True:
        if (inputFromUser**(access_iter.__next__())==outputFromUser):
          function = 'math.pow(variable1, '+ str(access_iter.__next__()-1) +')'
          return str(function)
    except:
      pass
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'math.sqrt(variable1)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'math.floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'math.ceil(variable1)'
  
  def javaMathOperations(inputFromUser, outputFromUser):
    inputFromUser=float(inputFromUser)
    outputFromUser=float(outputFromUser)
    try:
      while True:
        if (round(inputFromUser**(access_iter.__next__()))==outputFromUser):
          function = 'Math.pow(variable1, '+ str(access_iter.__next__()-1) +')'
          return str(function)
    except:
      pass
    if(math.sqrt(inputFromUser)==outputFromUser):
      return 'Math.sqrt(variable1)'
    elif(math.floor(inputFromUser)==outputFromUser):
      return 'Math.floor(variable1)'
    elif(math.ceil(inputFromUser)+1==outputFromUser):
      return 'Math.ceil(variable1)'
