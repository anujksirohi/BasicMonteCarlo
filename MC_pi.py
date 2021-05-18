'''---------------------------------------------------------------------
    *****         Written by Anuj Kumar Sirohi, SCIS,JNU            ****
    
    This progrm will calculate the value of pi using Monte Carlo Method
   ---------------------------------------------------------------------
'''
from numpy.random import rand 
N = int(1e2)	# Number of samples 
es_pi= sum((rand(N,2)**2).sum(axis=1)<1)/N *4
print("The value of Pi is = {:.2f}".format(es_pi))
