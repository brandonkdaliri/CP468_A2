import matplotlib.pyplot as p
import math
import random
import csv
from q1 import euclidean_distance

def main():
  X = []
  Y = []

  dataset = open('datasetQ2.csv', 'r')

  plots = csv.reader(dataset, delimiter=',')
  next(plots)
  for (x, y) in plots:
    X.append( float(x) )
    Y.append( float(y) )

  p.plot(X, Y, 'yo')
  
  kmeans(dataset, 2)

  p.show()

# Classifies data using the first two points as centroids.
# Repeats until centroids no longer change.
def kmeans(file, k):
  file.seek(0)
  centroids = []
  testing_set = []
  values = csv.reader(file, delimiter=',')
  next(values)

  # read in values
  i = 0
  for (x, y) in values:
    if (i < k):
      centroids.append( [float(x), float(y), i] )
    else:
      testing_set.append( [float(x), float(y), -1] )
    i += 1

  clusters = _kmeans(centroids, testing_set, k) + centroids
  cluster_count = []
  for _ in range(k):
    cluster_count.append(0)
  for (x, y, z) in clusters:
    s = 'r+'
    if z == 1:
      s = 'k+'
    p.plot(x, y, s, markersize=10)

    cluster_count[z] += 1
  
  print("Final cluster sizes:")
  for i in range(len(cluster_count)):
    colour = 'red'
    if i == 1:
      colour = 'black'
    print(f'Cluster {i} ({colour}): {cluster_count[i]}')

# kmeans helper function
def _kmeans(centroids, testing_set, k):
  flag = True
  while flag:
    cluster_sum = []
    for _ in range( k ):
      cluster_sum.append( [0, 0, 0] )

    for point in testing_set:
      distances = []
      for centroid in centroids:
        distances.append( [euclidean_distance(point, centroid, 2), centroid[2]] )
      
      if len(distances) > 0:
        distances.sort(key = lambda dist : dist[0])
        cluster = distances[0][1]
        point[2] = cluster # assign point with its appropriate cluster label
        cluster_sum[cluster] = ( cluster_sum[cluster][0] + point[0], cluster_sum[cluster][1] + point[1], cluster_sum[cluster][2] + 1)

    # create new centroids
    prev_centroids = centroids
    centroids = []
    matches = 0

    for i in range( k ):
      x = cluster_sum[i][0] / cluster_sum[i][2]
      y = cluster_sum[i][1] / cluster_sum[i][2]
      centroid = [round(float(x), 2), round(float(y), 2), i]
      centroids.append( centroid )
      # Check if centroid is the same as the previous iteration
      for (x, y, _) in prev_centroids:
        if (centroid[0] == x and centroid[1] == y):
          matches += 1

    # if no new centroid, then exit 
    if matches == k:
      flag = False
      print(f"kMeans Algorithm with k = {k}")
      print(f'Final centroids:')
      for centroid in centroids:
        print(centroid)

  return testing_set
  
if __name__ == "__main__":
  main()