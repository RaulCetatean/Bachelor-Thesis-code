import random
import sys

for i in range(1,31):

	control = open("control"+str(i)+"h3k4m1.fa","w")

	with open("gm12878h3k4m1.fa") as f:
	#with open("control1.fa") as f:
		for line in f:
			if ">" in line:
				line = line.rstrip("\n")
				control.write(line + "\n")
			elif ">" not in line:
				line = line.rstrip("\n")
				s = ''.join(random.sample(line,k=len(line)))
				control.write(s + "\n")
			
			
control.close()