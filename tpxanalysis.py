import csv
import numpy as np 
import pylab
import scipy.stats as stats
from scipy.stats import shapiro
from scipy.stats import wilcoxon
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt 

triplexes = []
original_sequence = 28861363 #triplexes in the original dna sequence

for i in range(1,31):
	with open("control"+str(i)+".tpx", newline='') as control:
		next(control) #skips header line if needed
		reader = csv.reader(control, delimiter='\t')
		#score = 0
		counter = 0
		for line in reader:
			#score += int(line[6])
			counter += 1
		#print("Control "+str(i)+": ",score,counter, score/counter)
		triplexes.append(counter)
#print(triplexes)

#Z-SCORE analysis

mean = np.mean(triplexes)
std = np.std(triplexes)

z = (original_sequence - mean) / std



#SHAPIRO-WILK TEST

'''shapiro_test = shapiro(triplexes)
print(shapiro_test)
#(0.6547862887382507, 3.6539009329317196e-07)

#qq plot

#stats.probplot(triplexes,dist="norm", plot=pylab)
#pylab.show()


#histogram
#plt.hist(triplexes, bins=int(100000/1000)) 
#pylab.show()

#WILCOXON non parametric test
wilcoxon_test = wilcoxon(triplexes)
print(wilcoxon_test) #it seems that WilcoxonResult(statistic=0.0, pvalue=1.1741945398998534e-06)
#so i have to reject null hypotesis, so they do not belong to the same sample, how is it possible?'''

rnas={}

def find_rnas():
	
	for i in range(1,31):
		with open("control"+str(i)+".tpx", newline='') as di:
			next(di)
			reader = csv.reader(di, delimiter='\t')
			for line in reader:
				if line[0] not in rnas:
					rnas[line[0]] = 1
				else:
					rnas[line[0]] += 1
	return rnas

rnas=find_rnas()
#print(find_rnas())

def div_d(dicts):
	sum_d = sum(dicts.values())

	for i in dicts:
		dicts[i] = float(dicts[i]/30)
	return dicts

print(div_d(rnas))