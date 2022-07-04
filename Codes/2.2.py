import numpy as np
import matplotlib.pyplot as plt
import scipy
import mpmath as mp
x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list

#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def Q(x):
    return mp.erfc(x/mp.sqrt(2))/2
def gau_cdf(x):
	return 1-Q(x)
		
vec_gau_cdf = scipy.vectorize(gau_cdf, otypes=[float])	
plt.plot(x.T,err,'o')
plt.plot(x, vec_gau_cdf(x))
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])
plt.savefig('gau_cdf.pdf')
plt.savefig('gau_cdf.eps')
plt.show()
