import os
import sys
import numpy as np
import csv
# from m
import matplotlib.pyplot as plt

X = []
for i in range(21):
	p = str(i*0.05)
	os.system('./encoder.sh data/maze/grid10.txt ' + p + ' > mdpfile')
 	os.system('./valueiteration.sh mdpfile > value_and_policy_file')
	os.system('./decoder.sh data/maze/grid10.txt value_and_policy_file ' + p + ' > mypath')
	os.system('cat mypath')
	with open("mypath") as csvfile:
		readCSV = csv.reader(csvfile, delimiter=' ')
		for row in readCSV:
			X.append(len(row))

print X
plt.plot(X)
plt.show()