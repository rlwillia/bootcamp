"""
Bootcamp utils: A collection of statistical functions
proved useful during Bootcamp
"""
import numpy as np

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

def bootstrap_dist(data, func = np.mean, n_reps = 100000):
    """
    Resamples data n times and computes statistic of interest
    returns
    """

    bs_replicates = np.empty(n_reps)
    for i in range(n_reps):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        bs_replicates[i] = func(bs_sample)

    return bs_replicates
