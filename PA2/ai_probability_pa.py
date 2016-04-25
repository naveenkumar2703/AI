# -*- coding: utf-8 -*-
"""
Programming assignment on probability for elements of Artifical intelligence

@author: Naveenkumar Ramaraju - 2000014414
"""

from Node import Node
from BayesianNetwork import BayesianNetwork
from Enumerator import Enumerator
from PriorSampler import PriorSampler
from RejectionSampler import RejectionSampler
from LikelihoodWeightedEstimator import askQueries as likelihoodWeight
from tabulate import tabulate

"""This method gets input from user by displaying method parameter to user"""
def get_input(text_for_user):
    print (text_for_user)
    return input().upper()

user_input_note = "Enter input in the format: \n[<Eveidence node1, value1>,<Eveidence node2, value2...>][Query node1,Query node2...]\nAllowed nodes are A,B,J,M,E and allowed values are t,f"
user_input_warning = "Invalid input:\n"
nodes = ['A','J','M','B','E']
node_values = ['T','F']

"""This method gets query and evidence variables based on imput structure mentioned in user_input_note.
Returns the query and evidence variable in a dict."""    
def getQueryAndEvidenceVariables(input_problem):
    input_processed = {'query':[],'evidence':{}}
    if not (input_problem.startswith('[') and input_problem.endswith(']')):
        return input_processed
    inputs = input_problem.split(']')
    
    if(not ((len(inputs)==3) and len(input_problem.split('['))==3)):
        return input_processed
    inputs.remove(inputs[len(inputs)-1])    
    #print(inputs)
    #for input_v in inputs:
    #print (input_v)
    try:
        evidenceVar = inputs[0]
        evidenceVar = evidenceVar.replace('[','')
        evidenceVar = evidenceVar.replace(' ','')
        
        if not (evidenceVar.startswith('<') and evidenceVar.endswith('>') and evidenceVar.count(',')>0 and (evidenceVar.count('<') == evidenceVar.count('>'))):
            return input_processed
            
        if evidenceVar.count(',')>1:
            evid_v_items = evidenceVar.split('><')
            for evid_v_item in evid_v_items:
                evid_v_item = evid_v_item.replace('<','')
                evid_v_item = evid_v_item.replace('>','')
                input_v_item_atts = evid_v_item.split(',')
                #print(input_v_item_atts)
                if len(input_v_item_atts)>0 and (input_v_item_atts[0] in nodes) and (input_v_item_atts[1] in node_values):
                    #d = {input_v_item_atts[0]:input_v_item_atts[1]}
                    input_processed['evidence'][input_v_item_atts[0]] = input_v_item_atts[1]
                else:
                    input_processed['evidence'] = {}
        else:
            evidenceVar = evidenceVar.replace('<','')
            evidenceVar = evidenceVar.replace('>','')
            input_v_item_atts = evidenceVar.split(',')
            #print(input_v_item_atts)
            if len(input_v_item_atts)>0 and (input_v_item_atts[0] in nodes) and (input_v_item_atts[1] in node_values):
                #d = {input_v_item_atts[0]:input_v_item_atts[1]}
                input_processed['evidence'][input_v_item_atts[0]] = input_v_item_atts[1]
            else:
                input_processed['evidence'] = {}
            
        queryVar = inputs[1]
        queryVar = queryVar.replace('[','')
        queryVar = queryVar.replace(' ','')
        queryVarItems = queryVar.split(',')
        for queryVarItem in queryVarItems:
                
            if(queryVarItem in nodes):
                input_processed['query'].extend(queryVarItem)
            
    
    except:
        #do nothing
        input_problem = None

    return input_processed

"""This method constructs alarm bayesian network, requried for assignment"""
def constructAlarmNetwork():
    #creating nodes from parent to child order.
    cpt_burglary = {'T':0.001,'F':0.999}
    node_burglary = Node('B',['T','F'],None,cpt_burglary)
    cpt_earthquake = {'T':0.002,'F':0.998}
    node_earthquake = Node('E',['T','F'],None,cpt_earthquake)
    cpt_alarm = {'T':{'B=T,E=T':0.95,'B=T,E=F':0.94,'B=F,E=T':0.29,'B=F,E=F':0.001},'F':{'B=T,E=T':0.05,'B=T,E=F':0.06,'B=F,E=T':0.71,'B=F,E=F':0.999}}
    node_alarm = Node('A',['T','F'],[node_burglary,node_earthquake],cpt_alarm)
    cpt_john_c = {'T':{'A=T':0.90,'A=F':0.05},'F':{'A=T':0.1,'A=F':0.95}}
    node_john_c = Node('J',['T','F'],[node_alarm],cpt_john_c)
    cpt_mary_c = {'T':{'A=T':0.70,'A=F':0.01},'F':{'A=T':0.3,'A=F':0.99}}
    node_mary_c = Node('M',['T','F'],[node_alarm],cpt_mary_c)
    
    alarmNetwork = BayesianNetwork([node_burglary,node_earthquake,node_alarm,node_john_c,node_mary_c])
    #print (node_mary_c)
    return alarmNetwork
    
input_problem = get_input(user_input_note)
valid_input = False
input_extract = None
while(not valid_input):
    input_extract = getQueryAndEvidenceVariables(input_problem)
    print('Processing:'+str(input_extract))
    if len(input_extract['query']) > 0 and len(input_extract['evidence']) > 0:
        valid_input = True
    if not valid_input:
        input_problem = get_input (user_input_warning+user_input_note)

print('Performing enumeration....')

alarmNetwork = constructAlarmNetwork()

enumerated_result = Enumerator().askQueries(input_extract['query'],input_extract['evidence'],alarmNetwork)


def addArrays(array1, array2):
    return [srcV + targV for srcV, targV in zip(array1, array2)]

def averageQueries(queries,samplesize):
    denominator = [samplesize for x in range(len(queries[0]))]
    returnArray = []
    #print(queries)
    for query in queries:
        returnArray.append([probV/den for probV,den in zip(query,denominator)])
    return returnArray

def addQueriesSamples(arrayOfResp):
    sum_of_query_sample = []
    #print(arrayOfResp)
    query_holder = []
    #creating placehoders for eachquery
    for index in range(len(arrayOfResp[0])):
        query_holder.insert(len(query_holder),[])#this will create number of place holders as per number of queries
        
    for index,query in enumerate(arrayOfResp[0]):
        for sampleResp in arrayOfResp:
            #print(sampleResp)
            query_holder[index].append(sampleResp[index])
            #print(query_holder)
    #print('printing query holder')
    #print(query_holder)
    
    for queryItem in query_holder:
        sum_holder = [0 for x in range(len(queryItem[0]))]
        for sample in queryItem:
            sum_holder = addArrays(sum_holder,sample)
        
        sum_of_query_sample.insert(len(sum_of_query_sample),sum_holder)
        #print(sum_of_query_sample)    
    
    return sum_of_query_sample

number_of_samples = [10,50,100,200,500,1000,10000]
for_output_table = []
for sample_size in number_of_samples:
    for_output_row = []
    for_output_row.append(sample_size)
    #print('******************Calculating for sample size: '+str(sample_size)+'******************')
    prior_sample_prob_value_resp = []
    rejection_sample_prob_value_resp = []
    likelihood_prob_value_resp = []
    for index in range(10):
        #print ('Performing prior sampling for sample size: '+ str(sample_size) + ' for iteration: '+str(index+1))
        prior_sample_prob_value_resp.insert(index,PriorSampler().askQueries(input_extract['query'],input_extract['evidence'],alarmNetwork,sample_size))
        #print ('Performing rejection sampling for sample size: '+ str(sample_size) + ' for iteration: '+str(index+1))
        rejection_sample_prob_value_resp.insert(index,RejectionSampler().askQueries(input_extract['query'],input_extract['evidence'],alarmNetwork,sample_size))
        #print ('Performing likelihood weighting for sample size: '+ str(sample_size) + ' for iteration: '+str(index+1))
        likelihood_prob_value_resp.insert(index,likelihoodWeight(input_extract['query'],input_extract['evidence'],alarmNetwork,sample_size))
    
    #print('Average of prior sample for sample size: ' + str(sample_size)+' :')
    prior_sample_average = averageQueries(addQueriesSamples(prior_sample_prob_value_resp),10)
    #print(str(prior_sample_average))
    for_output_row.append(prior_sample_average)
    #print('Average of rejection sample for sample size: ' + str(sample_size)+' :')   
    rejection_sample_average = averageQueries(addQueriesSamples(rejection_sample_prob_value_resp),10)
    #print(str(rejection_sample_average))
    for_output_row.append(rejection_sample_average)
    #print('Average of likelihood weight sample for sample size: ' + str(sample_size)+' :')  
    likelihood_average = averageQueries(addQueriesSamples(likelihood_prob_value_resp),10)
    #print(str(likelihood_average))
    for_output_row.append(likelihood_average)
    for_output_table.append(for_output_row)

print_row = ["Sample size","Prior sampling","Rejection sampling", "Likelihood weight"]
print_table = [print_row]
print_table.extend(for_output_table)
print("*************************Results-in - same order as query.*********************")
print("************ Results in same order as values fed into network. 'T', then 'F'. **********************")
print(input_extract)
enumerate_row = ["Enumeration","q2"]
print_table_1 = [enumerate_row,enumerated_result]
print(tabulate(print_table_1))
print (tabulate(print_table))