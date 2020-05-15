import functools as fp
import time

class Fibonacci:
  def __init__(self, fibonacciNumber):
    self.fibonacciNumber = fibonacciNumber
  def process(fibonacciNumber):
    fibonacciProcess = lambda fibonacciNumber: fp.reduce(lambda x, y: [x[1], x[0]+x[1]], range(fibonacciNumber), [0, 1])[0]
    print(fibonacciProcess(fibonacciNumber))
  def fibonacci(self):
    Fibonacci.process(self.fibonacciNumber-1)
  def fibonacciArray(self):
    fibonacciProcess = lambda fibonacciNumber: fp.reduce(lambda x, _: x+[x[-1]+x[-2]], range(fibonacciNumber-2), [0, 1])
    print(fibonacciProcess(self.fibonacciNumber))

class Exponent:
  def __init__(self, base):
    self.base = base
  def process(base, exponent):
    powerProcess = lambda base, exponent: fp.reduce(lambda x, y: [x[0], x[1]*base], range(exponent), [base, 1])[1]
    print(powerProcess(base, exponent))
  def power(self, exponent):
    Exponent.process(self.base, exponent)

class Factorial:
  def __init__(self, factorialNumber):
    self.factorialNumber = factorialNumber
  def process(factorialNumber):
    factorialProcess = lambda fibonacciNumber: fp.reduce(lambda x, y: [x[0]+1, x[1]*(x[0]+1)], range(factorialNumber-1), [1, 1])[1] 
    print(factorialProcess(factorialNumber))
  def factorial(self):
    Factorial.process(self.factorialNumber)

class upcoming:
  def __init__(self):
    pass


new = Fibonacci(555556)
new.fibonacci()