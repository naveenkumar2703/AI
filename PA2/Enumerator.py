# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:29:14 2016

@author: naveenkumar2703
"""
from BayesianNetwork import normalize as normalize

class Enumerator(object):
    
    def __init__(self):
        self.a = 1
    
     
    def getNodeValueIfInEvidence(self, node, evidences):
        if node == None or evidences == None or len(evidences) == 0:
            return None
        
        
        if node.name in evidences.keys():
            return evidences[node.name]
        
        return None
        
    
    def enumerateAll(self,nodes,evidences):
        #Todo
        if nodes == None or len(nodes) == 0:
            return 1.0
        
        firstNode = nodes[0]
        restNodes = []
        if len(nodes) > 1:
            restNodes = nodes[1:]
        
        nodeValueInEvidence = self.getNodeValueIfInEvidence(firstNode,evidences)
        
        #condition to handle hidden variables        
        if nodeValueInEvidence == None:
            extendedEvidVar = evidences.copy()
            sum_cpt_first_Node = 0
            for value in firstNode.values:
                extendedEvidVar[firstNode.name] = value
                sum_cpt_first_Node += ((firstNode.get_cpt(value,extendedEvidVar))* self.enumerateAll(restNodes,extendedEvidVar))
            return sum_cpt_first_Node
        #handling evidence/query variables    
        else:
            return ((firstNode.get_cpt(nodeValueInEvidence,evidences)) * self.enumerateAll(restNodes,evidences))
        
    
    
    def askQuery(self,queryVar,evidenceVar,bn):
        pDistOfQueryVar = []
        if bn == None or queryVar == None:
            return pDistOfQueryVar
        #distOfQuery = bn.getDistValuesForVariable(queryVar)
        node = bn.getNode(queryVar)
        
        extendedEvidVar = evidenceVar.copy()
        for item in node.values:
            extendedEvidVar[node.name] = item
            #print('calculating:'+item+' for node'+node.name)
            pDistOfQueryVar.insert(len(pDistOfQueryVar),self.enumerateAll(bn.nodes,extendedEvidVar))
        
        return normalize(pDistOfQueryVar)
    
    
    def askQueries(self,queryVars,evidenceVar,bn):
        pDistOfQueryVars = []
        for var in queryVars:
            pDistOfQueryVars.insert(len(pDistOfQueryVars),self.askQuery(var,evidenceVar,bn))
        
        print(pDistOfQueryVars)
        return pDistOfQueryVars