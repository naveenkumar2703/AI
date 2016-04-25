# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:26:40 2016

@author: naveenkumar2703
"""

from numpy.random import choice as ran

class SampleGenerator(object):
    
    def __init__(self):
        self.clazzName = 'SampleGenerator'
    
def getRandomSample(values,probabilityDist):
    return ran(values,1,p=probabilityDist)[0]

def getSampleNetwork(bayesianNetwork):
    sample = {}
    if bayesianNetwork == None or bayesianNetwork.nodes == None or len(bayesianNetwork.nodes) == 0:
        return sample
        
    for node in bayesianNetwork.nodes:
        probDist = []
        for value in node.values:
            probDist.insert(len(probDist),node.get_cpt(value,sample))
            
            #print(node.name+str(probDist)+str(sample))            
        sample[node.name] = getRandomSample(node.values,probDist)
        
        #print(sample)
    return sample

def getWeightedSample(bayesianNetwork, evidences):
    sample = {}
    weight = 1
    if bayesianNetwork == None or bayesianNetwork.nodes == None or len(bayesianNetwork.nodes) == 0:
        return sample
    
    evidenceVars = evidences.keys()
    
    for node in bayesianNetwork.nodes:
        if node.name in evidenceVars:
            weight = weight * node.get_cpt(evidences[node.name],sample)
            sample[node.name] = evidences[node.name]
        else:
            probDist = []
            for value in node.values:
                probDist.insert(len(probDist),node.get_cpt(value,sample))
            
            sample[node.name] = getRandomSample(node.values,probDist)
    
    #print(sample)
    #print(weight)    
    return sample,weight