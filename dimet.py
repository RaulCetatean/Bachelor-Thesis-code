import csv
import numpy as np 
import pylab
import scipy.stats as stats
from scipy.stats import shapiro
from scipy.stats import wilcoxon
import seaborn as sns
import matplotlib.pyplot as plt 

rnas={}

def find_rnas():
	
	for i in range(35):
		with open("gm12878h3k4m2-"+str(i)+".tpx", newline='') as di:
			next(di)
			reader = csv.reader(di, delimiter='\t')
			for line in reader:
				if line[0] not in rnas:
					rnas[line[0]] = 1
				else:
					rnas[line[0]] += 1
	return rnas

#rnas = find_rnas()
#plt.bar(list(rnas.keys()),rnas.values(), color='g')
#plt.show()

'''for keys, values in rnas.items():
	if values > 10000:
		print(keys,values)'''


def count_lines():
	counter = 0
	for i in range(35):
		with open("gm12878h3k4m2-"+str(i)+".tpx", newline='') as di:
			next(di)
			reader = csv.reader(di, delimiter='\t')
			for line in reader:
				counter += 1
	return counter

#print(count_lines())   16916181

'''RNAs more than 20000 times
chr19:14939433-16638094 45530 lnc-OR7C2-1:2 NONHSAG024979.2
chr19:14939434-16638095 22765  NONHSAT179489.1'''

'''RNAs more than 10000 times
chr1:827590-859446 16506 NONHSAT000158.2 long intergenic non-protein coding RNA 1128
chr12:105479454-105579919 14490 NONHSAT231550.1
chr12:121195247-121788902 10364 NONHSAG012540.2
chr14:105527918-106874878 12822 NONHSAG016106.2 lnc-BRF1-42 Gene lncRNA
chr16:5239801-6776014 13407 NONHSAG018484.2
chr19:14939433-16638094 45530 NONHSAG024979.2
chr19:14939434-16638095 22765 NONHSAT179489.1
chr2:58427774-59063958 14109 NONHSAT240610.1
chr21:16194539-16627303 10452 NONHSAT244128.1
chr3:165206947-165539430 15282 NONHSAT246008.1
chr4:180058940-180282181 10806 NONHSAT247982.1 NONHSAT247983.1 NONHSAT247984.1
chr5:151253051-151705182 17360 NONHSAG041966.2
chr5:69640296-70225632 11200 NONHSAT204278.1
chr5:93409355-93581320 17046 NONHSAT204466.1 NONHSAT204467.1    LncRNA NR2F1-AS1 regulates hepatocellular carcinoma oxaliplatin resistance by targeting ABCC1 via miR-363
chr6:21666443-22206433 12762 NONHSAT250887.1 NONHSAT250888.1 NONHSAT250889.1
chr7:65140370-65770810 14324 NONHSAG047815.3
chr8:95268835-95810143 19224 NONHSAT1278[29].2  il numero tra parentesi varia da 29 a 38'''
#C8orf37-AS1 Gene last one

#x =[1,2,3,4,5,6,7,8,9,10]
x = [45530,22765,19224,17360,17046,16506,15282,14490,14324,14109]
y = ['NONHSAG024979.2','NONHSAT179489.1','NONHSAT127829.2','NONHSAG041966.2','NONHSAT204466.1','NONHSAT000158.2',
'NONHSAT246008.1','NONHSAT231550.1','NONHSAG047815.3','NONHSAT240610.1']

'''plt.bar(x,y)
plt.xticks(x,rotation=90)
plt.barh(y,x)
plt.title('Recurrent RNAs')
plt.ylabel('RNA')
plt.xlabel('Number of occurrences')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.show()'''


m2=[10992,13779,6450,70990,12763,7645,7277,6713,11590,6504,10801,5358,5142, 12850,5273,4952,5737,11636,11290,15203]

'''
Z-score

mean=np.mean(m2)
std=np.std(m2)
og = 16916181
z = (og-mean)/std
1217.8983939602506'''

'''SHAPIRO-WILKS'''
shapiro_test = shapiro(m2)
#print(shapiro_test)
#(0.43958377838134766, 9.445992077417031e-08)

'''WILCOXON TEST'''
wilcoxon_test = wilcoxon(m2)
print(wilcoxon_test)

#qq plot
#stats.probplot(m2,dist="norm", plot=pylab)
#pylab.show()


#histogram
'''bins=range(0,75000,5000)
plt.hist(m2) 
pylab.show()'''