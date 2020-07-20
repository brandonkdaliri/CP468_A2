import matplotlib.pyplot as p
import math
import csv

# Calculates the Euclidean distance between 2 vectors
# row1 and row2 must be the same legnth
# n = number of attributes to consider (must be less than len)
def euclidean_distance(row1, row2, n = None):
  if n == None or n >= len(row1):
    n = len(row1) - 1

  distance = 0
  for i in range(n):
    distance += (row1[i] - row2[i])**2
  return math.sqrt(distance)
  
# TODO: figure out what coordinate to use as reference and finish function
def fnKNN(file, k):
  kplot = []
  dist = []
  plots = []
  values = csv.reader(file, delimiter=',')
  next(values)

  # read in coordinates and store tuples in array
  i = 0
  for (x, y, c) in values:
    if i == k:
      kplot = (x, y, c)
    plots.append( (float(x), float(y), int(c)) )
  
  # calculate euclidean distance of each point w.r.t. k
  for plot in plots:
    edist = euclidean_distance(kplot, plot, 2)
    dist.append(edist)
  
  # find the k minimum distances

def main():
  blueX = []
  blueY = []
  redX = []
  redY = []

  with open('datasetQ1.csv', 'r') as file:
    plots = csv.reader(file, delimiter=',')
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
  p.show()

if __name__ == "__main__":
  main()