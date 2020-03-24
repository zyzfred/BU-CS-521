# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:49:17 2019

@author: epinsky
"""

# text editor

x = 'defining decade'

x = """the book of 
unknown 
Americans is
the book I am
reading"""


x_list = list(x)
cur = 5

z = x.split('\n')

line_id = 2
delta = 2


def print_list_file(z,line_id, delta, sep='$'):
    mid_line = z[line_id]
    mid_str= mid_line[0: delta] + sep + mid_line[delta:]
    left_list = z[  : line_id]
    left_str = '\n'.join(left_list) 
    right_list = z[line_id + 1 : ]
    right_str = '\n'.join(right_list)
    print(left_str + '\n' + mid_str  + '\n' + right_str)
    print('\n ----------------- ')
 



# print_list_file(z, line_id, delta, '$')

"""
def cmd_h(z, line_id, delta):       # move left by one char
    if delta > 0:
        delta = delta -1
    elif line_id > 0:
        line_id = line_id -1
        delta = len(z[line_id])
    return z, line_id, delta


z, line_id, delta = cmd_h(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_h(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_h(z, line_id, delta)
print_list_file(z, line_id, delta, '$')

"""
"""
def cmd_I(z, line_id, delta):       # move right by one char
    current_line = z[line_id]
    if delta < len(current_line):
        delta = delta + 1
    elif line_id < len(z)-1 :
        line_id = line_id + 1
        delta = 0
    return z, line_id, delta

line_id =1
delta = 2
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_I(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_I(z, line_id, delta)
print_list_file(z, line_id,  delta, '$')
z, line_id, delta = cmd_I(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_I(z, line_id, delta)
print_list_file(z, line_id,  delta, '$')
z, line_id, delta = cmd_I(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
"""

"""
def cmd_X(z, line_id, delta):    # delete char to left of current
    if delta > 0:
        current_line = z[line_id]    
        left = current_line[0 : delta -1]
        right = current_line[delta : ]
        updated_current_line = left + right
        z[line_id] = updated_current_line
        delta = delta - 1
    return z, line_id, delta
    
    
line_id =1
delta = 2
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_X(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_X(z, line_id, delta)
print_list_file(z, line_id,  delta, '$')
z, line_id, delta = cmd_X(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
"""
"""
def cmd_ddp(z, line_id, delta):        # transpose two lines
    if line_id > 0:
        cur_line = z[line_id]
        prev_line = z[line_id -1]
        z[line_id]  = prev_line
        z[line_id -1] = cur_line
        line_id = line_id -1
    return z, line_id, delta
    
        
line_id =4
delta = 2
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_ddp(z, line_id, delta)
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_ddp(z, line_id, delta)
print_list_file(z, line_id,  delta, '$')
z, line_id, delta = cmd_ddp(z, line_id, delta)
print_list_file(z, line_id, delta, '$')   
z, line_id, delta = cmd_ddp(z, line_id, delta)
print_list_file(z, line_id,  delta, '$')
z, line_id, delta = cmd_ddp(z, line_id, delta)
print_list_file(z, line_id, delta, '$')      
"""


"""
def cmd_n(z, line_id, delta, target):   # find target
    for i in range(line_id, len(z)):
        next_line = z[i]
        if i == line_id:
            pos = next_line.find(target, delta, len(next_line)-1)
        else:
            pos = next_line.find(target)
        if pos >=0:
            return(z, i, pos)
    return z, line_id, delta
        
line_id =1
delta = 2
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_n(z, line_id, delta, 'can')
print_list_file(z, line_id, delta, '$')   
"""  


# assume that if you are at the beginning of a last line
#then you do nothing
def cmd_dd(z, line_id, delta):      # delete rest of the line
    cur_line = z[line_id]           # move pos to start next line
    new_cur_line = cur_line[0 : delta]
    z[line_id] =  new_cur_line
    if delta > 0:
        if line_id < len(z)-1:
            line_id = line_id + 1
            delta = 0
        else:
            delta = 0
    else:
        if line_id < len(z) -1:
            z.pop(line_id)
    return z, line_id, delta
        
    
line_id =1
delta = 2
print_list_file(z, line_id, delta, '$')
z, line_id, delta = cmd_dd(z, line_id, delta)
print_list_file(z, line_id, delta, '$') 
z, line_id, delta = cmd_dd(z, line_id, delta)
print_list_file(z, line_id, delta, '$') 






