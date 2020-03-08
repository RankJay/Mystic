from mathOperations import mathOperations
from stringOperations import stringOperations
from modularOperations import modularOperations

class moduleCreator:
  def cModuleCreator(inputFromUser, outputFromUser):
    if (inputFromUser):
      charLook = ' '
      if charLook not in outputFromUser:
        function = mathOperations.cMathOperations(inputFromUser, outputFromUser)
        moduleWriter.cWriter(inputFromUser, outputFromUser, function)
        exit(0)

      elif 'a' in outputFromUser or 'e' in outputFromUser or 'i' in outputFromUser or 'o' in outputFromUser or 'u' in outputFromUser:
        function = stringOperations.cStringOperations(inputFromUser, outputFromUser)
        moduleWriter.cWriter(inputFromUser, outputFromUser, function)
        exit(0)
    if len(inputFromUser)>1 and len(outputFromUser)>1:
      function = modularOperations.cModularOperations(inputFromUser, outputFromUser)
      moduleWriter.cWriter(inputFromUser, outputFromUser, function)
  
  def cplusModuleCreator(inputFromUser, outputFromUser):
    if (inputFromUser):
      charLook = ' '
      if charLook not in outputFromUser:
        function = mathOperations.cPlusMathOperations(inputFromUser, outputFromUser)
        moduleWriter.cPlusWriter(inputFromUser, outputFromUser, function)
        exit(0)
      elif 'a' in outputFromUser or 'e' in outputFromUser or 'i' in outputFromUser or 'o' in outputFromUser or 'u' in outputFromUser:
        function = stringOperations.cPlusStringOperations(inputFromUser, outputFromUser)
        moduleWriter.cPlusWriter(inputFromUser, outputFromUser, function)
        exit(0)
    if len(inputFromUser)>1 and len(outputFromUser)>1:
      function = modularOperations.cPlusModularOperations(inputFromUser, outputFromUser)
      moduleWriter.cPlusWriter(inputFromUser, outputFromUser, function)

  def pythonModuleCreator(inputFromUser, outputFromUser, languageFromUser):
    if (inputFromUser):
      charLook = ' '
      if charLook not in outputFromUser:
        function = mathOperations.pythonMathOperations(inputFromUser, outputFromUser)
        moduleWriter.pythonWriter(inputFromUser, outputFromUser, function)
        exit(0)
      elif 'a' in outputFromUser or 'e' in outputFromUser or 'i' in outputFromUser or 'o' in outputFromUser or 'u' in outputFromUser:
        function = stringOperations.pythonStringOperations(inputFromUser, outputFromUser)
        moduleWriter.pythonWriter(inputFromUser, outputFromUser, function)
        exit(0)
    if len(inputFromUser)>1 and len(outputFromUser)>1:
      function = modularOperations.pythonModularOperations(inputFromUser, outputFromUser)
      moduleWriter.pythonWriter(inputFromUser, outputFromUser, function)

  def javaModuleCreator(inputFromUser, outputFromUser):
    if (inputFromUser):
      charLook = ' '
      if charLook not in outputFromUser:
        function = mathOperations.javaMathOperations(inputFromUser, outputFromUser)
        moduleWriter.javaWriter(inputFromUser, outputFromUser, function)
        exit(0)
      elif 'a' in outputFromUser or 'e' in outputFromUser or 'i' in outputFromUser or 'o' in outputFromUser or 'u' in outputFromUser:
        function = stringOperations.javaStringOperations(inputFromUser, outputFromUser)
        moduleWriter.javaWriter(inputFromUser, outputFromUser, function)
        exit(0)
    if len(inputFromUser)>1 and len(outputFromUser)>1:
      function = modularOperations.javaModularOperations(inputFromUser, outputFromUser)
      moduleWriter.javaWriter(inputFromUser, outputFromUser, function)

class moduleWriter:
  def cWriter(inputFromUser, outputFromUser, function):
    f= open("Program.c","a")
    f.write('#include<stdio.h>\n#include<math.h>\n\nint main() {\n\tfloat variable1, output;\n\tscanf("%f", &variable1);\n\toutput='+ function +';\n\tprintf("%f", output);\n}')
    f.close
  
  def cPlusWriter(inputFromUser, outputFromUser, function):
    f= open("Program.cpp","a")
    f.write('#include <iostream>\n#include <math.h>\nusing namespace std;\n\nint main() {\n\tfloat variable1, output;\n\tcin >> variable1;\n\toutput='+ function +';\n\tcout << output;\n}')
    f.close

  def pythonWriter(inputFromUser, outputFromUser, function):
    f= open("Program.py","a")
    f.write('import math\n\nvariable1=float(input())\noutput='+ function +'\nprint(output)')
    f.close

  def javaWriter(inputFromUser, outputFromUser,  function):
    f= open("Program.java","a")
    f.write('import java.util.*;\n\npublic class Main {\n\tpublic static void main(String[] args) {\n\t\tScanner scanner=new Scanner(System.in);\n\t\tfloat variable1 = scanner.nextFloat();\n\t\tfloat output=(float)'+ function +';\n\t\tSystem.out.println(output);\n\t}\n}')
    f.close
