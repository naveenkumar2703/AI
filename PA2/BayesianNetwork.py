# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 23:52:16 2016

@author: naveenkumar2703
"""

class BayesianNetwork:
    def __init__ (self,nodes):
        self.nodes = nodes
    
    """This method will give distribution of values for given variable. For eg. 'H' and 'T' for coin toss."""    
    def getDistValuesForVariable(self,var):
        
        if self.nodes == None or var == None or len(var) == 0:
            return
        
        for node in self.nodes:
            if var == node.name:
                distValues = []
                for value in node.values:
                    distValues.insert({node.name:value})
                return distValues
        
        return
    
    
    def getNode(self, nodeName):
        if self.nodes == None or nodeName == None or len(nodeName) == 0:
            return None
            
        for node in self.nodes:
            if nodeName == node.name:
                return node
        
        #if nothing is found return None
        return None
    
    def getProbabilityForSpecificValues(self,sample):
        if self.nodes == None or len(sample.keys())!= len(self.nodes):
            return 0
        
        parentEvidences = {}
        probability = 1        
        for node in self.nodes:
            probability = probability * node.get_cpt(sample[node],parentEvidences)
            parentEvidences[node.name] = sample[node]
        
        print (str(probability))
        
        return probability
        
def normalize(enumeratedVals):
    sum_enumVals = 0
    for val in enumeratedVals:
        sum_enumVals += val
        
    ret_val = []
    if sum_enumVals == 0:
        for val in enumeratedVals:
            ret_val.insert(len(ret_val),0)
    else:    
        for val in enumeratedVals:
            ret_val.insert(len(ret_val),(val/sum_enumVals))
        
    return ret_val