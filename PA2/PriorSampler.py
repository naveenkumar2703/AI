# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:37:57 2016

@author: naveenkumar2703
"""

from SampleGenerator import getSampleNetwork as sample
from BayesianNetwork import normalize as normalize

class PriorSampler(object):
    
    def __init__(self):
        self.clazzName = 'PriorSampler'
    
    
    
    """sample is pregenerated and query is performed"""
    def askQuery(self,queryVar,evidenceVar,bayesianNetwork,samples):
        distOfQueryVar = []
        if queryVar == None:
            return distOfQueryVar
        #distOfQuery = bn.getDistValuesForVariable(queryVar)
        node = bayesianNetwork.getNode(queryVar)
        for index,value in enumerate(node.values):
            distOfQueryVar.insert(index,0)
        
        
            
        evidenceSampleCount = 0
        #queryGivenEvidenceCount = 0
            #print(extendedEvidVar)
            #print(samples)
        for currentSample in samples:
            evidenceMismatch = False
            #queryGivenEvidenceMismatch = False   
                    
            for evidenceItem in evidenceVar.keys():
                if(evidenceVar[evidenceItem] != currentSample[evidenceItem]):
                        #print('key: '+str(evidenceItem)+'E:'+str(extendedEvidVar[evidenceItem]) +'s: '+ str(sample[evidenceItem]))
                    evidenceMismatch = True
                    break
            if(not evidenceMismatch):
                evidenceSampleCount += 1
                for index, item in enumerate(node.values):
                    if currentSample[node.name] == item:
                        distOfQueryVar[index] += 1 
                        
            
            #print(matchingSampleCount)         
            #pDistOfQueryVar.insert(len(pDistOfQueryVar),matchingSampleCount/len(samples))
            
        #print(str(distOfQueryVar))
        return normalize(distOfQueryVar)
    
    
    def askQueries(self,queryVars,evidenceVar,bayesianNetwork,numberOfSamples):
        pDistOfQueryVars = []
        samples = []
        for item in range(numberOfSamples):
            samples.insert(len(samples),sample(bayesianNetwork))
        for var in queryVars:
            pDistOfQueryVars.insert(len(pDistOfQueryVars),self.askQuery(var,evidenceVar,bayesianNetwork,samples))
        
        #print(pDistOfQueryVars)
        return pDistOfQueryVars
        
        