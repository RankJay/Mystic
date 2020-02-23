import csv

class PredictionWriter:
  def predictionDataWriter(inputFromuser, outputFromUser):
    with open('data.csv', 'a', newline='') as deepLearningTrainer:
      trainer = csv.writer(deepLearningTrainer)
      try:
        if len(inputFromuser)>1 and float(inputFromuser)==True:
          trainer.writerow([inputFromuser, 0, outputFromUser])
        else:
          trainer.writerow([inputFromuser, 0, outputFromUser])
      except ValueError:
        if len(inputFromuser)>1:
          trainer.writerow([inputFromuser[0], inputFromuser[2], outputFromUser])
          
class GradientDescent:
  pass
