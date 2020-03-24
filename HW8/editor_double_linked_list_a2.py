# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:45:23 2019

@author: epinsky
"""

N_PTR = 0; P_PTR = 1; DATA = 2
x = """art
of
war"""
x_list = x.split('\n')

def print_file(n_start):
    if(n_start == None):
        return
    print(n_start[DATA])
    print_file(n_start[N_PTR])

def construct_linked_list(x_list):
    start = None
    end = None
    for e in x_list:
        next_node = [None, None, e]
        if start is None and end is None:
            start = next_node; end   = next_node
#            next_node[P_PTR] = next_node; next_node[N_PTR]=next_node
        else:
            end[N_PTR] = next_node
            next_node[P_PTR] = end
            end = next_node
    return start, end


n_start, n_end = construct_linked_list(x_list)

