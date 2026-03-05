# chaine de markov a temps discret: application 1 

import numpy as np 
import matplotlib.pyplot as plt

def plot_dist(P, pi0s_list, num_steps): 
    B = np.zeros((len(P), num_steps))
    for pi0 in pi0s_list: 
        pi = pi0
        for j in range(num_steps): 
            B[:, j] = pi
            pi = B[:, j]@P
        
        for i in range(len(B)): 
            plt.plot(B[i, :])

    plt.show()

P = np.array([[0.95, 0.04, 0.01, 0], 
              [0, 0.9, 0.05, 0.05],
              [0, 0, 0.8, 0.2],
              [1, 0, 0, 0]])

#two diff initial dist to prove that stationary dist is independent from initial distribution: 
#1st initial distribution
pi0 = np.array([1/4]*4)
#2nd initial distribution
pi0_2 = np.array([1/4, 2/4, 0, 1/4])

pi0s_list = [pi0, pi0_2]
num_steps = 100

plot_dist(P, pi0s_list, num_steps)
