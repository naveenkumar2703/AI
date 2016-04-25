# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 00:43:25 2016

@author: naveenkumar2703
"""
from SampleGenerator import getWeightedSample as weightedSample
from BayesianNetwork import normalize as normalize

class LikelihoodWeightedEstimator(object):
    def __init__(self):
        self.cn = 'LikelihoodWeightedEstimator'
    
def likelihoodWeighting(queryVar,evidenceVar,bayesianNetwork,numberOfSamples):
    #distOfQueryVar = []
    weightOfQueryVar = []
    if queryVar == None:
        return weightOfQueryVar
    qnode = bayesianNetwork.getNode(queryVar)
    
    for index,value in enumerate(qnode.values):
        #distOfQueryVar.insert(index,0)
        weightOfQueryVar.insert(index,0)
    
    for index in range(numberOfSamples):
        currentSample,weight = weightedSample(bayesianNetwork, evidenceVar)
        for index,value in enumerate(qnode.values):
            if value == currentSample[qnode.name]:
                #distOfQueryVar[index] += 1
                weightOfQueryVar[index]  = weightOfQueryVar[index] + weight
        
    #print(str(distOfQueryVar))
    #print(str(weightOfQueryVar))
    #print(str(weightOfQueryVar * distOfQueryVar))
    return normalize(weightOfQueryVar)
    
    
def askQueries(queryVars,evidenceVar,bayesianNetwork,numberOfSamples):
    pDistOfQueryVars = []
        
    for var in queryVars:
        pDistOfQueryVars.insert(len(pDistOfQueryVars),likelihoodWeighting(var,evidenceVar,bayesianNetwork,numberOfSamples))
        
    #print(pDistOfQueryVars)
    return pDistOfQueryVars