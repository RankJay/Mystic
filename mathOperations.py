import math
import numpy
import accessNaturalNumbers

access_iter=numpy.nditer([accessNaturalNumbers.NaturalNumbers])

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
    access_iter.reset()
    try:
      while True:
        if (round(outputFromUser**(access_iter.__next__()))==inputFromUser):
          function = 'pow(variable1, '+ str(float(1/(access_iter.__next__()-1))) +')'
          return str(function)
    except:
      pass
    access_iter.reset()
    # REMOVE 1 FROM accessNaturalNumbers to operate log
    try:
      while True:
        base=int(access_iter.__next__())
        if (math.log(inputFromUser, base)==outputFromUser):
          function = 'log(variable1, '+ str(base) +')'
          return str(function)
    except:
      pass
    if(math.floor(inputFromUser)==outputFromUser):
      return 'floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'ceil(variable1)'
    elif(abs(inputFromUser)==outputFromUser):
      return 'abs(variable1)'
    elif(round(math.sin(inputFromUser), 2)==outputFromUser):
      return 'sin(variable1)'
    elif(round(math.cos(inputFromUser), 2)==outputFromUser):
      return 'cos(variable1)'
    elif(round(math.tan(inputFromUser), 2)==outputFromUser):
      return 'tan(variable1)'
    elif(round(math.sinh(inputFromUser), 2)==outputFromUser):
      return 'sinh(variable1)'
    elif(round(math.cosh(inputFromUser), 2)==outputFromUser):
      return 'cosh(variable1)'
    elif(round(math.tanh(inputFromUser), 2)==outputFromUser):
      return 'tanh(variable1)'
    elif(round(math.asinh(inputFromUser), 2)==outputFromUser):
      return 'asinh(variable1)'
    elif(round(math.acosh(inputFromUser), 2)==outputFromUser):
      return 'acosh(variable1)'
    elif(round(math.atanh(inputFromUser), 2)==outputFromUser):
      return 'atanh(variable1)'
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
    access_iter.reset()
    try:
      while True:
        if (round(outputFromUser**(access_iter.__next__()))==inputFromUser):
          function = 'pow(variable1, '+ str(float(1/(access_iter.__next__()-1))) +')'
          return str(function)
    except:
      pass
    access_iter.reset()
    # REMOVE 1 FROM accessNaturalNumbers to operate log
    try:
      while True:
        base=int(access_iter.__next__())
        if (math.log(inputFromUser, base)==outputFromUser):
          function = 'log(variable1, '+ str(base) +')'
          return str(function)
    except:
      pass
    if(math.floor(inputFromUser)==outputFromUser):
      return 'floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'ceil(variable1)'
    elif(abs(inputFromUser)==outputFromUser):
      return 'abs(variable1)'
    elif(round(math.sin(inputFromUser), 2)==outputFromUser):
      return 'sin(variable1)'
    elif(round(math.cos(inputFromUser), 2)==outputFromUser):
      return 'cos(variable1)'
    elif(round(math.tan(inputFromUser), 2)==outputFromUser):
      return 'tan(variable1)'
    elif(round(math.sinh(inputFromUser), 2)==outputFromUser):
      return 'sinh(variable1)'
    elif(round(math.cosh(inputFromUser), 2)==outputFromUser):
      return 'cosh(variable1)'
    elif(round(math.tanh(inputFromUser), 2)==outputFromUser):
      return 'tanh(variable1)'
    elif(round(math.asinh(inputFromUser), 2)==outputFromUser):
      return 'asinh(variable1)'
    elif(round(math.acosh(inputFromUser), 2)==outputFromUser):
      return 'acosh(variable1)'
    elif(round(math.atanh(inputFromUser), 2)==outputFromUser):
      return 'atanh(variable1)'
    else:
      return '0'
  
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
    access_iter.reset()
    try:
      while True:
        if (round(outputFromUser**(access_iter.__next__()))==inputFromUser):
          function = 'math.pow(variable1, '+ str(float(1/(access_iter.__next__()-1))) +')'
          return str(function)
    except:
      pass
    access_iter.reset()
    # REMOVE 1 FROM accessNaturalNumbers to operate log
    try:
      while True:
        base=int(access_iter.__next__())
        if (math.log(inputFromUser, base)==outputFromUser):
          function = 'math.log(variable1, '+ str(base) +')'
          return str(function)
    except:
      pass
    if(math.floor(inputFromUser)==outputFromUser):
      return 'math.floor(variable1)'
    elif(math.ceil(inputFromUser)==outputFromUser):
      return 'math.ceil(variable1)'
    elif(abs(inputFromUser)==outputFromUser):
      return 'abs(variable1)'
    elif(round(math.sin(inputFromUser), 2)==outputFromUser):
      return 'math.sin(variable1)'
    elif(round(math.cos(inputFromUser), 2)==outputFromUser):
      return 'math.cos(variable1)'
    elif(round(math.tan(inputFromUser), 2)==outputFromUser):
      return 'math.tan(variable1)'
    elif(round(math.sinh(inputFromUser), 2)==outputFromUser):
      return 'math.sinh(variable1)'
    elif(round(math.cosh(inputFromUser), 2)==outputFromUser):
      return 'math.cosh(variable1)'
    elif(round(math.tanh(inputFromUser), 2)==outputFromUser):
      return 'math.tanh(variable1)'
    elif(round(math.asinh(inputFromUser), 2)==outputFromUser):
      return 'math.asinh(variable1)'
    elif(round(math.acosh(inputFromUser), 2)==outputFromUser):
      return 'math.acosh(variable1)'
    elif(round(math.atanh(inputFromUser), 2)==outputFromUser):
      return 'math.atanh(variable1)'
    else:
      return '0'
  
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
    access_iter.reset()
    try:
      while True:
        if (round(outputFromUser**(access_iter.__next__()))==inputFromUser):
          function = 'Math.pow(variable1, '+ str(float(1/(access_iter.__next__()-1))) +')'
          return str(function)
    except:
      pass
    access_iter.reset()
    # REMOVE 1 FROM accessNaturalNumbers to operate log
    try:
      while True:
        base=int(access_iter.__next__())
        if (math.log(inputFromUser, base)==outputFromUser):
          function = 'Math.log(variable1, '+ str(base) +')'
          return str(function)
    except:
      pass
    if(math.floor(inputFromUser)==outputFromUser):
      return 'Math.floor(variable1)'
    elif(math.ceil(inputFromUser)+1==outputFromUser):
      return 'Math.ceil(variable1)'
    elif(abs(inputFromUser)==outputFromUser):
      return 'abs(variable1)'
    elif(round(math.sin(inputFromUser), 2)==outputFromUser):
      return 'Math.sin(variable1)'
    elif(round(math.cos(inputFromUser), 2)==outputFromUser):
      return 'Math.cos(variable1)'
    elif(round(math.tan(inputFromUser), 2)==outputFromUser):
      return 'Math.tan(variable1)'
    elif(round(math.sinh(inputFromUser), 2)==outputFromUser):
      return 'Math.sinh(variable1)'
    elif(round(math.cosh(inputFromUser), 2)==outputFromUser):
      return 'Math.cosh(variable1)'
    elif(round(math.tanh(inputFromUser), 2)==outputFromUser):
      return 'Math.tanh(variable1)'
    elif(round(math.asinh(inputFromUser), 2)==outputFromUser):
      return 'Math.asinh(variable1)'
    elif(round(math.acosh(inputFromUser), 2)==outputFromUser):
      return 'Math.acosh(variable1)'
    elif(round(math.atanh(inputFromUser), 2)==outputFromUser):
      return 'Math.atanh(variable1)'
    else:
      return '0'
