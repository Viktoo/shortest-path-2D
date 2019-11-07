import csv
from heapdict import heapdict
import numpy as np

datafile = 'tiny.csv'
data = np.array(list(csv.reader(open(datafile))))

numR = len(data)
numC = len(data[0])

s = np.where(data == str('s'))
sR = int(s[0])
sC = int(s[1])

e = np.where(data == str('e'))
eR = int(e[0])
eC = int(e[1])

dist = np.array([[float('inf') for x in range(numC)] for y in range(numR)])
visited = np.array([[False for x in range(numC)] for y in range(numR)])
prev = {(x,y):0 for x in range(numC) for y in range(numR)}

dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

hd = heapdict()

dist[0,0] = 0
hd[sR,sC] = 0

reached_end = False

def explore(r, c):
	for i in range (0,4):
		rr = r + dr[i]
		cc = c + dc[i]

		if rr < 0 or cc < 0: continue 
		if rr >= numR or cc >= numC: continue
		if visited[rr,cc]: continue
		if data[rr,cc] == 's': continue

		node = (r,c)
		prev[rr,cc] = node 

		if (rr,cc) == (eR, eC):
			global reached_end
			reached_end = True 
			break

		d = int(dist[r,c]) + int(data[rr,cc])
		hd[rr,cc] = d
		dist[rr,cc] = d

		visited[rr,cc] = True

def reconstruct():
    path = []
    xy = (eR, eC)
    while xy != s:
    	path.append(prev[xy]) 
    	xy = prev[xy]
    path.reverse()
    return path

# MAIN

while reached_end == False:
	a = hd.popitem()
	r, c = a[0]
	# print(a[0])
	explore(r, c)

print(reconstruct())
