import numpy as np
import pandas as pd


N = 1000

# Large overlap
df = pd.DataFrame({
    'Method A': np.random.normal(10., 2., N),
    'Method B': np.random.normal(11., 2., N)
})
df.to_pickle('example1.pkl')

# Smaller overlap
df = pd.DataFrame({
    'Method A': np.random.normal(10., .5, N),
    'Method B': np.random.normal(11., .5, N)
})
df.to_pickle('example2.pkl')

# Very small overlap
df = pd.DataFrame({
    'Method A': np.random.normal(10., .2, N),
    'Method B': np.random.normal(11., .2, N)
})
df.to_pickle('example3.pkl')

# Skewed distributions
x1 = np.sum(np.random.randn(N,6)**2,axis=1)
x2 = -np.sum(np.random.randn(N,6)**2,axis=1)
x1 *= .5/np.std(x1)
x2 *= .5/np.std(x2)
x1 += 11. - np.mean(x1)
x2 += 10. - np.mean(x2)
df = pd.DataFrame({
    'Method A': x1,
    'Method B': x2
})

df.to_pickle('example4.pkl')

# Bimodal distributions
x1 = np.random.normal(10., .5, N)
x2 = np.concatenate((
    np.random.normal(1., .25, N//2),
    np.random.normal(-.1,.25,N//2)))
x2 /= np.std(x2)
x2 += 10.-np.mean(x2)
df = pd.DataFrame({
    'Method A': x1,
    'Method B': x2
})

df.to_pickle('example5.pkl')


# Uncorrelated data
df = pd.DataFrame({
    'Measurement A': np.random.normal(10., 2., N),
    'Measurement B': np.random.normal(11., 2., N)
})
df.to_pickle('example6.pkl')



# Correlated data
A = np.array([[1, .2],[1,.8]])
x = np.matmul(np.random.randn(N,2),A) + 10


df = pd.DataFrame({
    'Measurement A': x[:,0],
    'Measurement B': x[:,1]
})
df.to_pickle('example7.pkl')





# Mixture data
A = np.array([[1, .2],[1,.8]])
x = np.matmul(np.random.randn(N,2),A) + 10
x[0:N//4,0] = (x[0:N//4,0] -10)*.35 + 11
x[0:N//4,1] = (x[0:N//4,1] -10)*.6 + 8.5


df = pd.DataFrame({
    'Measurement A': x[:,0],
    'Measurement B': x[:,1]
})
df.to_pickle('example8.pkl')

# Multidimensional
df = pd.DataFrame({
    'A': np.random.normal(10., 2., N),
    'B': np.random.normal(11., 2., N),
    'C': np.random.normal(10.2, 2., N),
    'D': np.random.normal(11.5, 3., N),
    'E': np.random.normal(8, 1., N),
    'F': np.random.normal(3, 1.5, N)
})
df.to_pickle('example9.pkl')



# Prediction of categorical data
phn = [
 'h#',
 'sh',
 'ix',
 'hv',
 'eh',
 'dcl',
 'jh',
 'ih',
 'dcl',
 'd',
 'ah',
 'kcl',
 'k',
 's',
 'ux',
 'q',
 'en',
 'gcl',
 'g',
 'r',
 's',
 'w',
 'ao',
 'sh',
 'epi',
 'w',
 'ao',
 'dx',
 'axr',
 'ao',
 'l',
 'y',
 'ih',
 'axr' ]
confusion = np.zeros([len(phn),len(phn)])
for k in range(len(phn)):
    confusion[:,k] = np.random.randint(low=0,high=100,size=len(phn))
for k in range(len(phn)):
    confusion[k,k] = np.random.randint(low=30,high=400)