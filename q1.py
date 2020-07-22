import matplotlib.pyplot as p
import math
import random
import csv

# Calculates the Euclidean distance between 2 vectors
# row1 and row2 must be the same legnth
# n = number of attributes to consider (must be less than len)
def euclidean_distance(v1, v2, n = None):
  if n == None or n >= len(v1):
    n = len(v1) - 1

  distance = 0
  for i in range(n):
    distance += (v1[i] - v2[i])**2
  return math.sqrt(distance)
  
def fnKNN(file, k, accuracy):
  file.seek(0)
  training_set = []
  testing_set = []
  values = csv.reader(file, delimiter=',')
  next(values)

  # read in coordinates and store tuples in training list
  for (x, y, c) in values:
    training_set.append( [float(x), float(y), int(c)] )
  
  # move tuples from training to testing list based on accuracy
  testing_count = int(len(training_set) * round( (1 - accuracy), 2) )

  for _ in range(testing_count):
    index = random.randint(0, len(training_set) - 1)
    testing_set.append( training_set.pop(index) )

  # iterate through tuples in testing list and apply kNN algorithm
  correct = 0
  for point in testing_set:
    if point[2] == _knn(point, training_set, k):
      correct += 1

  # print results
  print(f'kNN with {accuracy * 100}% accuracy and k = {k}')
  print(f'  Total Data Points: {len(testing_set) + len(training_set)}')
  print(f'  Testing Set: {len(testing_set)}')
  print(f'  Training Set: {correct}/{len(testing_set)} estimated correctly')

  return

def _knn(point, training_set, k):
  if len(training_set) == 0:
    return

  dist = []
  for test_point in training_set:
    edist = euclidean_distance(point, test_point, 2)
    dist.append( (edist, test_point[2]) )
  
  if k > len(dist):
    k = len(dist)

  dist.sort

  type_0 = 0
  type_1 = 0
  for i in range(k):
    if dist[i] == 0:
      type_0 += 1
    else:
      type_1 += 1
  
  if type_0 > type_1:
    return 0
  elif type_0 < type_1:
    return 1
  else:
    return random.randint(0, 1)


def main():
  blueX = []
  blueY = []
  redX = []
  redY = []

  dataset = open('datasetQ1.csv', 'r')

  plots = csv.reader(dataset, delimiter=',')
  next(plots)
  for (x, y, c) in plots:
    # If class = 0, plot blue
    if int(c) == 0:
      blueX.append( float(x) )
      blueY.append( float(y) )
    else:
      redX.append( float(x) )
      redY.append( float(y) )

  p.plot(blueX, blueY, 'bo')
  p.plot(redX, redY, 'ro')

  for k in range(1, 4):
    fnKNN(dataset, k, 0.9)
    print('-' * 40)
    fnKNN(dataset, k, 0.7)
    print('-' * 40)
    fnKNN(dataset, k, 0.6)
    print('=' * 40)
  
  p.show()
  return

if __name__ == "__main__":
  main()