import numpy as np
import sys
import csv

filename = sys.argv[1]

prob = float(sys.argv[2])



mazedata = np.genfromtxt(str(filename), delimiter=' ').astype(int)
negation = mazedata == 1
binarymaze  = np.where(negation > 0,0,1)
# print(mazedata,binarymaze,mazedata.shape)
numStates = np.sum(binarymaze)

print "numStates", numStates

myarr = {}
count = 0
for i in range(mazedata.shape[0]) :
	for j in range(mazedata.shape[1]) :
		if(binarymaze[i,j] == 1):
			myarr[i*mazedata.shape[1]+j] = count
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
		if i > 0 :
			num_action_grid[i,j,0] = binarymaze[i-1,j]
		if i < mazedata.shape[1]-1 :
			num_action_grid[i,j,1] = binarymaze[i+1,j]
		if j < mazedata.shape[0]-1 :
			num_action_grid[i,j,2] = binarymaze[i,j+1]
		if j > 0 :
			num_action_grid[i,j,3] = binarymaze[i,j-1]

		if mazedata[i,j] == 2 :
			start = i*mazedata.shape[1] + j	

		if mazedata[i,j] == 3 :
			end.append(myarr[i*mazedata.shape[1] + j])	

numActions = np.sum(num_action_grid)

print "numActions", 4

print "start", myarr[start]

print "end", str(end)[1:-1]

if prob == 1:
	for i in range(mazedata.shape[0]) :
		for j in range(mazedata.shape[1]) :
			if(num_action_grid[i,j,0] == 1) :
				if myarr[(i-1)*mazedata.shape[1] + j] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,1 ,1 
				else :
					print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,0 ,1 
			if(num_action_grid[i,j,1] == 1) :
				if myarr[(i+1)*mazedata.shape[1] + j] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,1 ,1 
				else :
					print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,0 ,1 
			if(num_action_grid[i,j,3] == 1) :
				if myarr[i*mazedata.shape[1] + j-1] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,1 ,1 
				else : 
					print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,0 ,1 
			if(num_action_grid[i,j,2] == 1) :
				if myarr[i*mazedata.shape[1] + j+1] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,1 ,1 
				else :
					print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,0 ,1 

else :
	for i in range(mazedata.shape[0]) :
		for j in range(mazedata.shape[1]) :
			num_transitions = np.sum(num_action_grid[i,j,:])
			if num_transitions == 0 :
				continue
			myP = prob + (1-prob)/num_transitions
			otherP = (1-prob)/num_transitions
			if(num_action_grid[i,j,0] == 1) :
				if myarr[(i-1)*mazedata.shape[1] + j] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,1 ,myP 
				else :
					print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,0 ,myP 
				if(num_action_grid[i,j,1] == 1) :
					if myarr[(i+1)*mazedata.shape[1] + j] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,0 ,otherP 
				if(num_action_grid[i,j,3] == 1) :	
					if myarr[i*mazedata.shape[1] + j-1] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,1 ,otherP 
					else : 
						print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,0 ,otherP 
				if(num_action_grid[i,j,2] == 1) :	
					if myarr[i*mazedata.shape[1] + j+1] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,0 ,otherP 
			if(num_action_grid[i,j,1] == 1) :
				if myarr[(i+1)*mazedata.shape[1] + j] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,1 ,myP 
				else :
					print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,0 ,myP 
				if(num_action_grid[i,j,0] == 1) :
					if myarr[(i-1)*mazedata.shape[1] + j] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,0 ,otherP 
				if(num_action_grid[i,j,3] == 1) :
					if myarr[i*mazedata.shape[1] + j-1] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,1 ,otherP 
					else : 
						print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,0 ,otherP 
				if(num_action_grid[i,j,2] == 1) :	
					if myarr[i*mazedata.shape[1] + j+1] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,0 ,otherP 
			if(num_action_grid[i,j,3] == 1) :
				if myarr[i*mazedata.shape[1] + j-1] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,1 ,myP 
				else : 
					print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,0 ,myP 
				if(num_action_grid[i,j,0] == 1) :
					if myarr[(i-1)*mazedata.shape[1] + j] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,0 ,otherP 
				if(num_action_grid[i,j,1] == 1) :
					if myarr[(i+1)*mazedata.shape[1] + j] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,0 ,otherP 
				if(num_action_grid[i,j,2] == 1) :
					if myarr[i*mazedata.shape[1] + j+1] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,0 ,otherP 

			if(num_action_grid[i,j,2] == 1) :
				if myarr[i*mazedata.shape[1] + j+1] in end :
					print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,1 ,myP 
				else :
					print "transition", myarr[i*mazedata.shape[1]+j] , 3, myarr[i*mazedata.shape[1]+j+1] ,0 ,myP 
				if(num_action_grid[i,j,0] == 1) :
					if myarr[(i-1)*mazedata.shape[1] + j] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 0, myarr[(i-1)*mazedata.shape[1]+j] ,0 ,otherP 
				if(num_action_grid[i,j,1] == 1) :	
					if myarr[(i+1)*mazedata.shape[1] + j] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,1 ,otherP 
					else :
						print "transition", myarr[i*mazedata.shape[1]+j] , 1, myarr[(i+1)*mazedata.shape[1]+j] ,0 ,otherP 
				if(num_action_grid[i,j,3] == 1) :	
					if myarr[i*mazedata.shape[1] + j-1] in end :
						print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,1 ,otherP 
					else : 
						print "transition", myarr[i*mazedata.shape[1]+j] , 2, myarr[i*mazedata.shape[1]+j-1] ,0 ,otherP 
				
print "discount","", 0.9


