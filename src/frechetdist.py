import numpy as np 
import math

import geometry
from geometry import *

def frechet_distance(polyP, polyQ):
    '''
    Args:
        polyP: polynomial representing curve 1
        polyQ: polynomial representing curve 2
    Returns:
        Frechet distance between two curves
    Descriptions:
        Calculate Frechet distance between two curves
    '''
    p = np.array(polyP, np.float64)
    q = np.array(polyQ, np.float64)
    pLen = len(p)
    qLen = len(q)

    assert pLen == qLen

    ca = (np.ones((pLen, qLen), dtype=np.float64) * -1)
    fdist = ca_func(ca, pLen-1, qLen-1, p, q)

    return fdist

def ca_func(ca, idx, jdx, p, q):

    if ca[idx, jdx] > -1:
        return ca[idx, jdx]
    elif idx == 0 and jdx == 0:
        ca[idx, jdx] = euclidian_dist(p[idx], q[jdx])
    elif idx > 0 and jdx == 0:
        ca[idx, jdx] = max(ca_func(ca, idx-1, 0, p, q), euclidian_dist(p[idx], q[jdx]))
    elif idx == 0 and jdx > 0:
        ca[idx, jdx] = max(ca_func(ca, 0, jdx-1, p, q), euclidian_dist(p[idx], q[jdx]))
    elif idx > 0 and jdx > 0:
        ca[idx, jdx] = max(min(
            ca_func(ca, idx-1, jdx, p, q),
            ca_func(ca, idx-1, jdx-1, p, q),
            ca_func(ca, idx, jdx-1, p, q)), 
            euclidian_dist(p[idx], q[jdx]))
    else:
        ca[idx, jdx] = float('inf')

    return ca[idx, jdx]