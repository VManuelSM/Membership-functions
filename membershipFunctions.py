import numpy as np
import skfuzzy as fuzz

def getAxisValues(axis,stepSize):
    return np.arange(axis['xmin'], axis['xmax'], stepSize)
pass

def linearFunction(points, xrange):
    values = []
    for x in xrange:
        if x<points['a']:
            values.append(0) 
        elif (x>=points['a'] and x<points['b']):
            values.append((x-points['a'])/(points['b'] - points['a']))
        elif x>=points['b']:
            values.append(1)
    return values
pass

def triangleFunction(points, xrange):
    values = []
    for x in xrange:
        if x <= points['a']:
            values.append(0)
        elif (x >= points['a'] and x <= points['b']):
            values.append((x-points['a'])/(points['b'] - points['a']))
        elif x >= points['b'] and x <= points['c']:
            values.append((points['c']-x)/(points['c'] - points['b']))
        elif x >= points['c']:
            values.append(0)
    return values
pass

def trapezoidalFunction(points, xrange):
    values = []
    for x in xrange:
        if x <= points['a']:
            values.append(0)
        elif (x >= points['a'] and x <= points['b']):
            values.append((x-points['a'])/(points['b'] - points['a']))
        elif x >= points['b'] and x <= points['c']:
            values.append(1)
        elif (x >= points['c'] and x <= points['d']):
            values.append((points['d']-x)/(points['d'] - points['c']))
        elif x >= points['d']:
            values.append(0)
    return values
pass

def generalizedBellFunction(generalizedBellData, xrange):
    return fuzz.gbellmf(xrange, generalizedBellData['width'],generalizedBellData['slope'],generalizedBellData['center'])
pass

def gaussianFunction(gaussianData, xrange):
    return fuzz.gaussmf(xrange, gaussianData['mean'], gaussianData['sigma'])
