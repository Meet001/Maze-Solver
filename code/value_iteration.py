import numpy as np
import sys
import csv


filename = sys.argv[1]

# print(filename)

numStates = 0
numActions = 0
start = 0
end = []
transition = []
discount = 0
with open(str(filename)) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=' ')
		for row in readCSV:
				if str(row[0]) == 'numStates' : 
					numStates = int(row[1])
				if str(row[0]) == 'numActions' : 
					numActions = int(row[1])
					# transition = np.zeros((numStates,numActions,numStates,2))
					for i in range(numStates):
					    transition.append([])
					    for j in range(numActions):
					        transition[i].append([])
					# print transition
				if str(row[0]) == 'start' : 
					start = int(row[1])
				if str(row[0]) == 'end' : 
					end = list(map(int, row[1:]))      
				if str(row[0]) == 'transition' :

					transition[int(row[1])][int(row[2])].append(list(map(float, row[3:])))
				if str(row[0]) == 'discount' : 
					discount = float(row[2])

# end = np.array(end)


# print(numStates)
# print(numActions)
# print(start)
# print(end)
# print(transition[0][0])
# print(discount)

t = 0
V_prev = np.zeros(numStates)
V_curr = np.zeros(numStates)
policy = np.zeros(numStates)

while(1) :
	t = t + 1
	for s in range(numStates):
		mymax = 0

		for a in range(numActions):
			mysum = 0
			for sdash in range(len(transition[s][a])) :
				# print transition[s][a][sdash][0]
				mysum = mysum + transition[s][a][sdash][2]*(transition[s][a][sdash][1] + discount*V_prev[int(transition[s][a][sdash][0])])
			if a == 0:
				mymax = mysum
				policy[s] = a
			if mysum > mymax :
				mymax = mysum
				policy[s] = a
		V_curr[s] = mymax
		if (s in end) :
			V_curr[s] = 0
			policy[s] = -1

	if(np.all(np.abs(V_curr-V_prev) < 1e-16)):
		break;
	#print np.max(np.abs(V_curr-V_prev))
	V_prev = np.copy(V_curr)

policy = policy.astype(int)

for i in range(numStates):
	print round(V_curr[i],11), policy[i]


# myarr = []
# for i in range(11):
# 	subarr = []
# 	for j in range(11):
# 		subarr.append(policy[i*11+j])
# 	myarr.append(subarr)
print "iterations", t

# print np.array(myarr)