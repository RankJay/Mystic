from Module import moduleCreator
from languageTranslator import languageRecognizer

print("Enter your Input:")
inputFromUser=input()
if 'stdio.h' or 'iostream' or 'import' or 'public static' in inputFromUser:
  print('Enter language of converted code:')
  languageFromUser=input()
  languageRecognizer(inputFromUser, languageFromUser)
else:
  print("Output you need:")
  outputFromUser=input()
  print("Enter language of code:")
  languageFromUser=input()
  if languageFromUser=="C" or languageFromUser=="c":
    moduleCreator.cModuleCreator(inputFromUser, outputFromUser)
  elif languageFromUser=="C++" or languageFromUser=="c++":
    moduleCreator.cplusModuleCreator(inputFromUser, outputFromUser)
  elif languageFromUser=="python" or languageFromUser=="Python" or languageFromUser=="python3" or languageFromUser=="Python3" or languageFromUser=="python2" or languageFromUser=="Python2" or languageFromUser=="pypy2" or languageFromUser=="Pypy2" or languageFromUser=="pypy3" or languageFromUser=="Pypy3":    
    moduleCreator.pythonModuleCreator(inputFromUser, outputFromUser, languageFromUser)
  elif languageFromUser=="java" or languageFromUser=="Java":
    moduleCreator.javaModuleCreator(inputFromUser, outputFromUser)
