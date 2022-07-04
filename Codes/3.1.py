import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,30)#points on the x axis
X1 = np.linspace(-4,4,30)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
emp_cdf = []
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('rand.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
for i in X1:
    count = 0
    for value in randvar:
        if value <= i:
            count += 1
    emp_cdf.append(count/simlen)

	
plt.plot(x.T,err,label = 'Theoritical')#plotting the CDF
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid() #creating the grid
plt.legend()
plt.savefig('rand_cdf.pdf')
plt.savefig('rand_cdf.eps')
plt.show()
