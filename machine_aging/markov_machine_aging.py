
import numpy as np


 # FOR DTMC  
 
def dtmc_stationnaire(P):
    """
    Distribution quasi-stationnaire pour une DTMC absorbante.
    Detecte automatiquement les etats transients et absorbants.
    Retourne pi sur les etats transients (normalise a 1).
    """
    n = P.shape[0]
    absorbants = [i for i in range(n) if P[i, i] == 1.0]
    transients = [i for i in range(n) if i not in absorbants]

    Q = P[np.ix_(transients, transients)]
    t = len(transients)

    #resoudre le systeme stationnaire
    A = (Q.T - np.eye(t))
    A[-1, :] = 1.0
    b = np.zeros(t)
    b[-1] = 1.0
    pi_t = np.linalg.solve(A, b)
    pi_t = np.clip(pi_t, 0, None)
    pi_t /= pi_t.sum()

    #reconstuire pi sur tous les etats (absorbants = 0)
    pi = np.zeros(n)
    for i, idx in enumerate(transients):
        pi[idx] = pi_t[i]

    return pi




def dtmc_production(P, R, T_heures=8.0, periode=1.0):
    """Production journaliere DTMC = (T/periode) * sum(pi_i * R_i)."""
    pi = dtmc_stationnaire(P)
    return (T_heures / periode) * np.dot(pi, R)


# FOR CTMC 


def ctmc_depuis_lambdas(lambdas, n):
    """Construit la matrice Q depuis un dict {(i,j): taux}."""
    Q = np.zeros((n, n))
    for (i, j), val in lambdas.items():
        Q[i, j] = val
    for i in range(n):
        Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
    return Q


def ctmc_stationnaire(Q):
    """Distribution stationnaire pour CTMC : resoudre pi Q = 0, sum(pi) = 1."""
    n = Q.shape[0]
    A = Q.T.copy()
    A[-1, :] = 1.0
    b = np.zeros(n)
    b[-1] = 1.0
    pi = np.linalg.solve(A, b)
    pi = np.clip(pi, 0, None)
    pi /= pi.sum()
    return pi


def ctmc_production(Q, R, T_heures=8.0):
    """Production journaliere CTMC = T * sum(pi_i * R_i)."""
    pi = ctmc_stationnaire(Q)
    return T_heures * np.dot(pi, R)

