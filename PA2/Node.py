# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 23:37:37 2016

@author: naveenkumar2703
"""

class Node(object):
    def __init__(self,name,values,parentNodes,cpt):
        self.name = name
        self.values = values
        self.parentNodes = parentNodes
        self.cpt = cpt
    
    def __str__(self):
        return 'Node:'+str(self.name)+' has parents '+str(self.parentNodes)
    
    
    def get_cpt(self,value,evidenceValues):
        if value == None:
            return 1
        
        #print (evidenceValues)      
        if self.parentNodes != None and isinstance(self.cpt[value], dict):
            #Have not handled evidenceValues == None scenario as it is expected to be handled by calee
            parentNodeList = []
            for item in self.parentNodes:
                parentNodeList.insert(len(parentNodeList),item.name)
                
            peividenceList = []
            for item in evidenceValues.keys():
                if item in parentNodeList:
                    peividenceList.insert(len(peividenceList),str(item)+'='+str(evidenceValues[item]))
            #print(peividenceList)
            
            for item in self.cpt[value].keys():
                parentQueryMatchCount = 0
                for parentEvidence in peividenceList:
                    if item.count(parentEvidence) > 0:
                        parentQueryMatchCount += 1
                if parentQueryMatchCount == len(peividenceList):
                    #print(self.cpt[value][item])
                    return self.cpt[value][item]
        
        else:
            #print(self.cpt[value])
            return self.cpt[value]
            
        