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
