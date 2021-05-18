'''---------------------------------------------------------------------
    *****         Written by Anuj Kumar Sirohi, SCIS,JNU            ****
    
    This progrm will generate Gaaussian distributed random variables x,y
    with N(0,1) using Box-Muller algorithm.
   ---------------------------------------------------------------------
'''
# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(101)
u1 = np.random.uniform(size = 1000)
u2 = np.random.uniform(size = 1000)
r = np.sqrt(-2 * np.log(u1))
theta = 2 * np.pi * u2
x = r * np.cos(theta);y = r * np.sin(theta)
# Draw the plot
fig,(ax1,ax2) = plt.subplots(1,2)
sns.distplot(x, color='green',ax = ax1, hist_kws={"edgecolor": 'black'}).set_title('X')
sns.distplot(y, color='blue', ax =ax2,hist_kws={"edgecolor": 'black'}).set_title('Y')
plt.show()

