# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 04:42:45 2022

this script is written as a homework for "Learning from Data" lecture.

The detailed information about hw1 can be reached from the current directory

@author: emirc
"""
import random as rd

class coin:
    id_coin=0
    heads=0
    tails=0
    
    def __init__(self,id_coin):
        self.id_coin=id_coin
    
    def increase_head(self):
        self.heads+=1
        
    def increase_tail(self):
        self.tails++1
    
    def reset(self):
        self.heads=0
        self.tails=0
        

def create_coins():
    coins=[]
    for i in range(1000):
        coins.append(coin(i))
        
    return coins


def flip(coin):
    flip=rd.Random().randint(0, 1)
    if flip==0:
        coin.increase_head()
    else:
        coin.increase_tail()
        
        
def experiment(coins):
    min_head_coin=coins[0]
    result=[]
    for coin in coins:
        for i in range(10):
            flip(coin)
            
        if min_head_coin.heads>coin.heads:
            min_head_coin=coin
    
    random_coin=rd.Random().randint(0, 999)
    result.append([coins[0],coins[0].heads/10])
    result.append([coins[random_coin],coins[random_coin].heads/10])
    result.append([min_head_coin,min_head_coin.heads/10])

    return result
    

def reset_coins(coins):
    for coin in coins:
        coin.reset()

def main():
    
    coins=create_coins()
    
    experiment_results=[]
    
    #doing experiment 1.000 times in order to get a full distrubition 
    sum_Vmin=0.0  
    print("Experiment is working... ")
    for i in range(1000):
        one_experiment=experiment(coins)
        sum_Vmin+=one_experiment[2][1]
        experiment_results.append(one_experiment)
        reset_coins(coins)
        
    print("E(Vmin)"+str(sum_Vmin/1000))

    
main()