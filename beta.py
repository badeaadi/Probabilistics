'''
    Badea Adrian Catalin, grupa 334
    
    
    Sa se genereze prin doua metode variabila Beta(2, 4). Sa se genereze histogramele
    asociate celor doua metode

'''
from scipy.stats import gamma
from scipy.stats import uniform
import numpy as np

import matplotlib.pyplot as plt


def plot_hist(b, title):
    
    pl, ax = plt.subplots(1, 1)
    
    ax.hist(b, density=True, histtype='stepfilled', alpha=0.2)
    
    ax.set_title(title)
    
    plt.show()


def gamma_va(a, nr_sub):
    
    pl, ax = plt.subplots(1, 1)
    
    x = np.linspace(gamma.ppf(0.001, a), gamma.ppf(0.999, a), nr_sub)

    ax.plot(x, gamma.pdf(x, a), 'r-', lw=3, alpha=0.6, label='gamma pdf')
    
    ax.set_title('Gamma variable from 0 to 1 with a = {}'.format(a))
    
    return gamma.pdf(x, a)

    
def beta_va(a, b, nr_samples):
    
    gamma_va(a, nr_samples)
    gamma_va(b, nr_samples)
    
    g1 = gamma.rvs(a, size = nr_samples)
    
    g2 = gamma.rvs(b, size = nr_samples)
    

    b = []
    for i in range(0, nr_samples):
        if g1[i] + g2[i] > 0:
            b.append(g1[i] / (g1[i] + g2[i]))
            
            
    print('Mean for Beta from Gamma is {}'.format(np.mean(np.array(b))))
    
    print('Standard deviation for Beta from Gamma is {}'.format(np.std(np.array(b))))
    
    plot_hist(b, 'Beta calculated from gamma distributions')
    
    
def beta_u(a, b, nr_samples):
    
    n = a + b - 1
    b = [] 
    for i in range(0, nr_samples):
        
        u = uniform.rvs(size = n)
        u = sorted(u)
        b.append(u[a - 1])


    print('Mean from Beta from Gamma is {}'.format(np.mean(np.array(b))))
    
    print('Standard deviation for Beta from Gamma is {}'.format(np.std(np.array(b))))
          
    plot_hist(b, 'Beta calculated from uniform distributions')
    
    

if __name__ == '__main__':

    a, b = 2, 4
    nr_samples = 20000
    
    beta_va(a, b, nr_samples)
    
    beta_u(a, b, nr_samples)
