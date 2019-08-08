import sys
import csv
import numpy as np
np.random.seed(1)

filename = sys.argv[1]
prob = float(sys.argv[3])

mazedata = np.genfromtxt(str(filename), delimiter=' ').astype(int)
negation = mazedata == 1
binarymaze  = np.where(negation > 0,0,1)
# print(mazedata,binarymaze,mazedata.shape)
numStates = np.sum(binarymaze)

# print "numStates", numStates

myarr = {}
newarr = {}
count = 0
for i in range(mazedata.shape[0]) :
	for j in range(mazedata.shape[1]) :
		if(binarymaze[i,j] == 1):
			myarr[i*mazedata.shape[1]+j] = count
			newarr[count] = [i,j]
			count = count + 1

# print(myarr)

num_action_grid = np.zeros((mazedata.shape[0],mazedata.shape[1],4))

start = 0
end = []

for i in range(mazedata.shape[0]) :
	for j in range(mazedata.shape[1]) :
		ans = 0
		if(binarymaze[i,j] == 0):
			continue

		if mazedata[i,j] == 2 :
			start = [i,j]

		if mazedata[i,j] == 3 :
			end.append([i,j])	

num_action_grid = np.zeros((mazedata.shape[0],mazedata.shape[1],4))

start = 0
end = []

for i in range(mazedata.shape[0]) :
	for j in range(mazedata.shape[1]) :
		ans = 0
		if(binarymaze[i,j] == 0):
			continue
		if i > 0 :
			num_action_grid[i,j,0] = binarymaze[i-1,j]
		if i < mazedata.shape[1]-1 :
			num_action_grid[i,j,1] = binarymaze[i+1,j]
		if j < mazedata.shape[0]-1 :
			num_action_grid[i,j,2] = binarymaze[i,j-1]
		if j > 0 :
			num_action_grid[i,j,3] = binarymaze[i,j+1]

		if mazedata[i,j] == 2 :
			start = [i,j]

		if mazedata[i,j] == 3 :
			end.append([i,j])	


filename = sys.argv[2]
# print numStates
mynew = [0]*numStates
count = 0
with open(str(filename)) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=' ')
		for row in readCSV:
			if str(row[0]) == 'iterations' :
				continue 
			else :
				x = int(row[1])
				mynew[count] = x 
				count = count + 1


path = ""
curr = start
iter = 0
#print mynew
#print myarr
while 1:
	iter+= 1
	if(curr in end) :
		break
	# print curr
	if iter != 1:
		path = path + " "
	num_transitions = np.sum(num_action_grid[curr[0],curr[1],:])
	x = mynew[myarr[curr[0]*mazedata.shape[1]+curr[1]]]
	prob_array = num_action_grid[curr[0],curr[1],:]
	prob_array = prob_array*(1 - prob)/num_transitions
	prob_array[x] = prob_array[x] + prob
	#print curr[0]*mazedata.shape[1]+curr[1]
	y = np.random.choice(4,1,p=prob_array)
	#print curr,y,prob_array
	if y == 0 :
		path = path + 'N'
		curr = [curr[0]-1,curr[1]]
	if y == 1 :	
		path = path + 'S'
		curr = [curr[0]+1,curr[1]]
	if y == 2 :
		path = path + 'W'
		curr = [curr[0],curr[1]-1]
	if y == 3 :
		path = path + 'E'
		curr = [curr[0],curr[1]+1]

print path