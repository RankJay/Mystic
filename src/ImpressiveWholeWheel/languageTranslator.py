from Module import moduleWriter

def languageRecognizer(inputFromUser, languageFromUser):
  if '#include<stdio.h>' in inputFromUser:
    languageTranslator.cLanguageTranslator(inputFromUser, languageFromUser)
  elif '#include<iostream>' and 'using namespace std' in inputFromUser:
    languageTranslator.cPlusLanguageTranslator(inputFromUser, languageFromUser)
  elif 'input()' or 'import' in inputFromUser:
    languageTranslator.pythonLanguageTranslator(inputFromUser, languageFromUser)
  elif 'public class' or 'public static void main' in inputFromUser:
    languageTranslator.javaLanguageTranslator(inputFromUser, languageFromUser)

class languageTranslator:
  def cLanguageTranslator(inputFromUser, languageFromUser):
    if languageFromUser=='c++':
      languageConvertor.cPlusLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=="python" or languageFromUser=="Python" or languageFromUser=="python3" or languageFromUser=="Python3" or languageFromUser=="python2" or languageFromUser=="Python2" or languageFromUser=="pypy2" or languageFromUser=="Pypy2" or languageFromUser=="pypy3" or languageFromUser=="Pypy3":
      languageConvertor.pythonLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=='java' or languageFromUser=='java8':
      languageConvertor.javaLanguageConvertor(inputFromUser, languageFromUser)


  def cPlusLanguageTranslator(inputFromUser, languageFromUser):
    if languageFromUser=='c':
      languageConvertor.cLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=="python" or languageFromUser=="Python" or languageFromUser=="python3" or languageFromUser=="Python3" or languageFromUser=="python2" or languageFromUser=="Python2" or languageFromUser=="pypy2" or languageFromUser=="Pypy2" or languageFromUser=="pypy3" or languageFromUser=="Pypy3":
      languageConvertor.pythonLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=='java' or languageFromUser=='java8':
      languageConvertor.javaLanguageConvertor(inputFromUser, languageFromUser)


  def pythonLanguageTranslator(inputFromUser, languageFromUser):
    if languageFromUser=='c':
      languageConvertor.cLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=='c++':
      languageConvertor.cPlusLanguageConvertor(inputFromUser, languageFromUser)
      
    elif languageFromUser=='java' or languageFromUser=='java8':
      languageConvertor.javaLanguageConvertor(inputFromUser, languageFromUser)

  
  def javaLanguageTranslator(inputFromUser, languageFromUser):
    if languageFromUser=='c':
      languageConvertor.cLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=='c++':
      languageConvertor.cPlusLanguageConvertor(inputFromUser, languageFromUser)

    elif languageFromUser=="python" or languageFromUser=="Python" or languageFromUser=="python3" or languageFromUser=="Python3" or languageFromUser=="python2" or languageFromUser=="Python2" or languageFromUser=="pypy2" or languageFromUser=="Pypy2" or languageFromUser=="pypy3" or languageFromUser=="Pypy3":
      languageConvertor.pythonLanguageConvertor(inputFromUser, languageFromUser)
    

class languageConvertor:
  def cLanguageConvertor(inputFromUser, languageFromUser):
    pass

  def cPlusLanguageConvertor(inputFromUser, languageFromUser):
    pass

  def pythonLanguageConvertor(inputFromUser, languageFromUser):
    pass
  
  def javaLanguageConvertor(inputFromUser, languageFromUser):
    pass
