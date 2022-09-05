import numpy as np 
import matplotlib.pyplot as plt  

f = open('alkane.dat','r')
lines = f.readlines()
x, y = [], []

	#read the file  line by line
for i in lines:
	x.append(i.split()[0])
	y.append(i.split()[3])
	#d.append(i.split()[2])
# make the np.array so we can multiply it with a float or else we a string value

x = np.array(x,dtype='float64')
y=np.array(y,dtype='float64')

#x=0.5*x
#y=0.8*y
print('x value is :',x)
print('y value is :',y)
# plotting 

plt.plot(x,y)
plt.ylabel('some numbers')
plt.show()


	