# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 03:06:11 2022

this script is written as a homework for "Learning from Data" lecture.

The detailed information about hw1 can be reached from the current directory.

@author: emirc
"""
import numpy as np
import math

#this variable is intented to set randomness accuracy of the computations.
#increasing it gets more computational cost.


NUMBER_OF_ELEMENTS_IN_SET=15
def get_random_point():
        x=round(np.random.uniform(-1,1),2)
        y=round(np.random.uniform(-1,1))
        return [x, y]
    
def get_random_line():
    p1=get_random_point()
    p2=get_random_point()
    ##Even if it has a less probability, to have a valid line preventing they would be same
    while(p2[0]==p1[0]):
        p2=get_random_point()
        
    a=p1[1]-p2[1]/(p1[0]-p2[0])
    return a, p1[1]-(a*p1[0])


def check_point(line,point):
    if((line[0]*point[0])+line[1]<point[1]):
        return -1
    else:
        return 1
    
          

def create_set(random_line):
    x=[]
    for i in range(NUMBER_OF_ELEMENTS_IN_SET):
        point=get_random_point()
        x.append([point,check_point(random_line,point)]) 
        
    return x


def check_completed_classification(input_X,vector):
    for input_x in input_X:
        if(check_point(vector, input_x[0])!=input_x[1]):
            return False
        
    return True

def PLA(input_X):
    #ordered to initialize vector as 0 vector
    vector=[0.0,0.0]
    iterations=0
    while not check_completed_classification(input_X, vector):
        iterations+=1
        #choosing random input
        random_index=np.random.randint(0, len(input_X))
        input_x=input_X[random_index]
        p1=[0,vector[1]]
        p2=[vector[0],0]
        a=0.0
        try:
            a=p1[1]-p2[1]/(p1[0]-p2[0])
        except ZeroDivisionError:
            pass
        vector_line=[a, p1[1]-(a*p1[0])]
        if(check_point(vector_line, input_x[0])!=input_x[1]):
            print(vector)
            value1=math.fabs(input_x[0][1])*input_x[1]
            value=math.fabs(input_x[0][0])*input_x[1]

            vector[0]+=float(float(value1)/10)
            vector[1]+=float(float(value1)/10)
            
    return vector, iterations

random_line=get_random_line()

print("randomly created line value: "+str(random_line[0])+" * X + "+str(random_line[1]))
input_X=create_set(random_line)
print("\n\nrandomly created data set is as follows\n")
print(input_X)
vector_learned=PLA(input_X)
print("\n\nThe learned vector after "+str(vector_learned[1])+" iterations is as follows")
print(vector_learned[0])
