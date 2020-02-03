from mathOperations import mathOperations
from stringOperations import stringOperations

class moduleCreator:
  def cModuleCreator(inputFromUser, outputFromUser):
    if ord(inputFromUser)>=48 and ord(inputFromUser)<=57:
      if ord(outputFromUser)>=48 and ord(outputFromUser)<=57:
          function = mathOperations.cMathOperations(inputFromUser, outputFromUser)
          moduleWriter.cWriter(inputFromUser, outputFromUser, function)
      else:
        pass
    else:
      function = stringOperations.cStringOperations(inputFromUser, outputFromUser)
      moduleWriter.cWriter(inputFromUser, outputFromUser, function)
  
  def cplusModuleCreator(inputFromUser, outputFromUser):
    if ord(inputFromUser)>=48 and ord(inputFromUser)<=57:
      if ord(outputFromUser)>=48 and ord(outputFromUser)<=57:
        function = mathOperations.cPlusMathOperations(inputFromUser, outputFromUser)
        moduleWriter.cPlusWriter(inputFromUser, outputFromUser, function)
      else:
        pass
    else:
      function = stringOperations.cPlusStringOperations(inputFromUser, outputFromUser)
      moduleWriter.cPlusWriter(inputFromUser, outputFromUser, function)

  def pythonModuleCreator(inputFromUser, outputFromUser, languageFromUser):
    if ord(inputFromUser)>=48 and ord(inputFromUser)<=57:
      if ord(outputFromUser)>=48 and ord(outputFromUser)<=57:
        function = mathOperations.pythonMathOperations(inputFromUser, outputFromUser)
        moduleWriter.pythonWriter(inputFromUser, outputFromUser, function)
      else:
        pass
    else:
      function = stringOperations.pythonStringOperations(inputFromUser, outputFromUser)
      moduleWriter.pythonWriter(inputFromUser, outputFromUser, function)

  def javaModuleCreator(inputFromUser, outputFromUser):
    if ord(inputFromUser)>=48 and ord(inputFromUser)<=57:
      if ord(outputFromUser)>=48 and ord(outputFromUser)<=57:
        function = mathOperations.javaMathOperations(inputFromUser, outputFromUser)
        moduleWriter.javaWriter(inputFromUser, outputFromUser, function)
      else:
        pass
    else:
      function = stringOperations.javaStringOperations(inputFromUser, outputFromUser)
      moduleWriter.javaWriter(inputFromUser, outputFromUser, function)

class moduleWriter:
  def cWriter(inputFromUser, outputFromUser, function):
    f= open("Program.c","w+")
    f.write('#include<stdio.h>\n#include<math.h>\n\nint main() {\n\tint variable1, output;\n\tscanf("%d", &variable1);\n\toutput='+ function +';\n\tprintf("%d", output);\n}')
    f.close
  
  def cPlusWriter(inputFromUser, outputFromUser, function):
    f= open("Program.cpp","w+")
    f.write('#include <iostream>\n#include <math.h>\nusing namespace std;\n\nint main() {\n\tint variable1, output;\n\tcin >> variable1;\n\toutput='+function+';\n\tcout << output;\n}')
    f.close

  def pythonWriter(inputFromUser, outputFromUser, function):
    f= open("Program.py","w+")
    f.write('import math\n\nvariable1=int(input())\noutput='+ function +'\nprint(output)')
    f.close

  def javaWriter(inputFromUser, outputFromUser,  function):
    f= open("Program.java","w+")
    f.write('import java.util.*;\npublic class Main {\n\tpublic static void main(String[] args) {\n\t\tScanner scanner=new Scanner(System.in);\n\t\tint variable1 = scanner.nextInt();\n\t\tint output=(int)'+ function +';\n\t\tSystem.out.println(output);\n\t}\n}')
    f.close