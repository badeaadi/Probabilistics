'''
    Badea Adrian Catalin, grupa 334
    
    
    Sa se genereze prin doua metode variabila Beta(2, 4). 
    Sa se genereze histogramele asociate celor doua metode

'''
from scipy.stats import gamma
from scipy.stats import uniform
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_hist(b, title):
    
    pl, ax = plt.subplots(1, 1)
    
    ax.hist(b, density=True, histtype='stepfilled', alpha=0.2)
    
    ax.set_title(title)
    
    plt.show()


def plot_hist_algorithm(b, title):
        
    b_np = np.array(b)
    
    minim = np.min(b_np)
    maxim = np.max(b_np)
    k = 40
    
    x = np.linspace(minim, maxim, k)
    f = np.zeros(k)
    
    for i in range(0, len(b)):
        for j in range(0, k - 1):
            if x[j] <= b[i] and b[i] <= x[j + 1]:
                f[j] += 1
    
    r = np.zeros(k)
    for j in range(0, k - 1):
        r[j] = f[j] / len(b)
        
    
    pl, ax = plt.subplots(1, 1)

    ax.plot(x, r)
    
    ax.set_title(title)
    

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
            
            
    print('Beta from Gamma:')
    
    print('Mean: {}'.format(np.mean(np.array(b))))
    
    print('Standard deviation: {}'.format(np.std(np.array(b))))
    
    plot_hist(b, 'Beta calculated from gamma distributions')
    
    plot_hist_algorithm(b, 'Beta histogram from gamma')
    
    
def beta_u(a, b, nr_samples):
    
    n = a + b - 1
    b = [] 
    for i in range(0, nr_samples):
        
        u = uniform.rvs(size = n)
        u = sorted(u)
        b.append(u[a - 1])

    print('Beta from uniform:')
    
    print('Mean is {}'.format(np.mean(np.array(b))))
    
    print('Standard deviation is {}'.format(np.std(np.array(b))))
          
    plot_hist(b, 'Beta calculated from uniform distributions')
    
    plot_hist_algorithm(b, 'Beta histogram from uniform')
    
    

if __name__ == '__main__':

    a, b = 2, 4
    
    nr_samples = 1000000
    
    mpl.style.use('seaborn')
    
    print('Generation of Beta variable using Uniform and Gamma random variables for {} samples.'.format(nr_samples))
    
    print('Coefficients : a = {} and b = {}'.format(a, b))
    
    print('Theorical mean is a / (a + b) ')
    print('Expected mean : {}'.format(a / (a + b)))

    print('Theoretical variance is a * b / ((a + b) ^ 2 * (a + b + 1)')
    
    var = a * b / ((a + b) ** 2 * (a + b + 1))
    
    print('Expected variance: {}'.format(var))
    print('Expected standard deviation: {}'.format(np.sqrt(var)))
    
    
    
    beta_va(a, b, nr_samples)
    
    beta_u(a, b, nr_samples)
    
   
    
    
