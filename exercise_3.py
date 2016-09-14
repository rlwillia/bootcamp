import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Exercise 3.2 Data Collapse

# Load data, remove first three lines
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

# Assign IPTG and fold change arrays
wt_lac_IPTG = wt_lac[:,0]
q18m_lac_IPTG = q18m_lac[:,0]
q18a_lac_IPTG = q18a_lac[:,0]
wt_lac_fc = wt_lac[:,1]
q18m_lac_fc = q18m_lac[:,1]
q18a_lac_fc = q18a_lac[:,1]

# Plot IPTG vs. fold change
plt.plot(wt_lac_IPTG, wt_lac_fc, marker= '.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(q18m_lac_IPTG, q18m_lac_fc, marker= '.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(q18a_lac_IPTG, q18a_lac_fc, marker= '.', linestyle='none', markersize=20, alpha=0.5)
plt.xlabel('IPTG conc (mM)')
plt.xlabel('IPTG conc (mM)')
plt.xlabel('IPTG conc (mM)')
plt.ylabel('fold change')
plt.xscale('log')
#plt.show()
plt.close()

# Function for computing theoretical fold change

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Computes theoretical fold change of fluorescence
    fold change=[1+RK(1+c/KAd)2(1+c/KAd)2+Kswitch(1+c/KId)2]−1
    """
    numerator = RK * (1 + c/KdA)**2
    denominator = (1 + c/KdA)**2 + Kswitch*((1 + c/KdI)**2)
    theor_fc = (1 + numerator/denominator)**-1

    return theor_fc

# Plot theoretical fold changes of mutants

#Calculate theoretical fold change
IPTG_vals = np.logspace(-6, 2, num=100, endpoint=True, base=10.0)
wt_theor = fold_change(IPTG_vals, 141.5)
q18m_theor = fold_change(IPTG_vals, 16.56)
q18a_theor = fold_change(IPTG_vals, 1332)

#Plot theoretical and experimental data
plt.plot(wt_lac_IPTG, wt_lac_fc, marker= '.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(q18m_lac_IPTG, q18m_lac_fc, marker= '.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(q18a_lac_IPTG, q18a_lac_fc, marker= '.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(IPTG_vals, wt_theor, marker='', linestyle='solid', alpha=0.5)
plt.plot(IPTG_vals, q18m_theor, marker='', linestyle='solid', alpha=0.5)
plt.plot(IPTG_vals, q18a_theor, marker='', linestyle='solid', alpha=0.5)
plt.xlabel('IPTG conc (mM)')
plt.xlabel('IPTG conc (mM)')
plt.xlabel('IPTG conc (mM)')
plt.ylabel('fold change')
plt.xscale('log')
#plt.show()
plt.close()

# Function to compute Bohr parameter

def bohr_parameter()
