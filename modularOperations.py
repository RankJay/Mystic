class modularOperations:
  def cModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.c","w+")
      f.write('')
      f.close
      function = 'pass'
      return str(function)

  def cPlusModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.cpp","w+")
      f.write('')
      f.close
      function = 'pass'
      return str(function)
  
  def pythonModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.py","w+")
      f.write('')
      f.close
      function = 'pass'
      return str(function)
  
  def javaModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.java","w+")
      f.write('')
      f.close
      function = 'pass'
      return str(function)