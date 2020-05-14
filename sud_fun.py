ve# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:10:08 2019

@author: nawaz
"""

def cross(a, b):
      return [s+t for s in a for t in b]
  
def grid_values(grid,boxes):
    di={}
    for i in range(len(boxes)):
        if(grid[i]=='.'):
            di[boxes[i]]='123456789'
        else:
            di[boxes[i]]=grid[i]
    return di

def display(values,boxes,rows,cols):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(di,peers):
    for i in di.keys():
        #print(di.keys())
        if(len(di[i])==1):
            #print(di[i],end="")
            for peer in peers[i]:
                #print(peer,end="")
                if(len(di[peer])!=1):
                    #print(di[peer],end=";")
                    di[peer]=di[peer].replace(di[i],"")
                    #print(di[peer],end="-")
            #print("")
    return di
                
def onlyCh(di,units):
    for i in di.keys():
        if(len(di[i])!=1):
            num=""
            for j in units[i][2]:
                if(i!=j):
                    num+=di[j]
            num=set(sorted(num))
            num=list(set('123456789')-num)
            if(len(num)==1 and num[0] in di[i]):
                di[i]=num[0]
    return di

def is_err(values,peers):
    for i in values.keys():
        if(len(values[i])==1):
            for peer in peers[i]:
                if(values[peer]== values[i]):
                    return True
            

def search(values,boxes,peers,units):
    "Using depth-first search and propagation, try all possible values."
    values=eliminate(values,peers)
    values=onlyCh(values,units)
    
    if is_err(values,peers):
        return False
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    #print(n,s)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku,boxes,peers,units)
        if attempt:
            return attempt

