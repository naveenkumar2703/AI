# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 23:33:29 2016

@author: naveenkumar2703
"""
from SampleGenerator import getSampleNetwork as sample
from BayesianNetwork import normalize as normalize

class RejectionSampler(object):
    def __init__(self):
        self.clazzName = 'RejectionSampler'
        
    """sample is generated on the go and discarded. Only count was kept for calculation"""    
    def askQuery(self,queryVar,evidenceVar,bayesianNetwork,numberOfSamples):
        distOfQueryVar = []
        if queryVar == None:
            return distOfQueryVar
        #distOfQuery = bn.getDistValuesForVariable(queryVar)
        qnode = bayesianNetwork.getNode(queryVar)
        for index,value in enumerate(qnode.values):
            distOfQueryVar.insert(index,0)
        
        #extendedEvidVar = evidenceVar.copy()
        
                
        for item in range(numberOfSamples):
            currentSample = sample(bayesianNetwork)
            
            evidenceNotMatch = False
            for evidence in evidenceVar.keys():
                if str(evidenceVar[evidence]) != str(currentSample[evidence]):
                    evidenceNotMatch = True
                    break
            if (not evidenceNotMatch):
                for index,value in enumerate(qnode.values):
                    if value == currentSample[qnode.name]:
                        distOfQueryVar[index] += 1
    
        
        return normalize(distOfQueryVar)
    
    def askQueries(self,queryVars,evidenceVar,bayesianNetwork,numberOfSamples):
        pDistOfQueryVars = []
        
        for var in queryVars:
            pDistOfQueryVars.insert(len(pDistOfQueryVars),self.askQuery(var,evidenceVar,bayesianNetwork,numberOfSamples))
        
        #print(pDistOfQueryVars)
        return pDistOfQueryVars