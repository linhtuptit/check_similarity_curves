import numpy as np 
import math

import frechetdist, procrustes, geometry
from frechetdist import *
from procrustes import *
from geometry import *

def curve_similarity(trajCurve, refCurve, checkRotation=True, rotate=10):
    '''
    Estimate how similar the shapes of 2 curves are to each,
    accounting for translation, scale, and rotation
    '''
    # Normalize two curves
    normTrajCurve = procrustes_normalize_curve(trajCurve)
    normRefCurve = procrustes_normalize_curve(refCurve)
    geoAvgCurveLen = math.sqrt(
        curve_length(normTrajCurve) * curve_length(normRefCurve))

    # Compute angle between two curves using Procrustes analysis
    thetaToCheck = [0]
    if(checkRotation):
        procrustesTheta = find_procrustes_rotation_angle(
            normTrajCurve, normRefCurve)

        if(procrustesTheta > np.pi):
            procrustesTheta = procrustesTheta - 2 * np.pi

        if(procrustesTheta != 0 and abs(procrustesTheta) < np.pi):
            thetaToCheck.append(procrustesTheta)

        for idx in range(rotate):
            theta = -1 * np.pi + (2 * idx * np.pi) / (rotate - 1)
            if(theta != 0 and theta != np.pi):
                thetaToCheck.append(theta)
    
    # Using Frechet distance to check the similarity level 
    minFdist = float('inf')
    for thetaIdx in thetaToCheck:
        rotatedTrajCurve = rotated_curve(normTrajCurve, thetaIdx)
        fdist = frechet_distance(rotatedTrajCurve, normRefCurve)
        if(fdist < minFdist):
            minFdist = fdist

    similarityIdx = max(1 - minFdist / (geoAvgCurveLen / math.sqrt(2)), 0) 
    
    return round(similarityIdx, 4)

    
