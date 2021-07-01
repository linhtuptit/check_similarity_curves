import numpy as np 
import math

import geometry
from geometry import *

def find_procrustes_rotation_angle(trajCurve, refCurve):
    '''
    Find the angle to rotate trajectory curve to match the rotation
    of reference curve using procrustes analysis. This matching satisfy
    the Sum of Squared Distance (SSD) between curves is minimized
    '''
    assert len(trajCurve) == len(refCurve)
    # Calculate numerator and denominator
    nume = 0
    deno = 0
    for idx in range(len(trajCurve)):
        nume += refCurve[idx][0]*trajCurve[idx][1] - refCurve[idx][1]*trajCurve[idx][0]
        deno += refCurve[idx][0]*trajCurve[idx][0] + refCurve[idx][1]*trajCurve[idx][1] 

    return np.arctan2(nume, deno)

def procrustes_normalize_rotation(trajCurve, refCurve):
    '''
    Rotate trajectory curve to match the rotation of reference curve 
    using procrustes analysis
    '''
    angle = find_procrustes_rotation_angle(trajCurve, refCurve)
    return rotated_curve(trajCurve, angle)

def procrustes_normalize_curve(curve):
    '''
    Translate and scale curve by Procrustes Analysis
    '''
    curveLen = len(curve)
    meanXCord = sum(curve[:,0])/curveLen
    meanYCord = sum(curve[:,1])/curveLen
    curve = curve - [meanXCord, meanYCord]

    # Processing
    squaredSum = 0
    for idx in range(curveLen):
        squaredSum += (curve[idx][0])**2 + (curve[idx][1])**2
    scale = round(squaredSum / curveLen, 2)

    return (curve / scale)



