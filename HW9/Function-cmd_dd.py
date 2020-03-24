N_PTR = 0; P_PTR = 1; DATA = 2
x_str = """Monday
Tuesday
Wednesday"""

def construct_linked_list(y_str):
    y_list = y_str.split('\n')
    new_start = None
    new_end = None
    for e in y_list:
        new_node = [None, None, e]
        if new_start is None and new_end is None:
            new_start = new_node
            new_end = new_node
        else:
            new_node[P_PTR] = new_end
            new_end[N_PTR] = new_node
            new_end = new_node
    return new_start, new_end
    
def print_sublist(first, last):
    next_node = first
    while next_node is not None:
        print(next_node[DATA])
        if next_node == last:
            break
        next_node = next_node[N_PTR]
    return

def get_record(first, last, pos):
    next_node = first
    counter = -1
    while next_node is not None:
        counter = counter + 1
        if counter == pos:
            break
        else:
            next_node = next_node[N_PTR]
    return next_node

def print_file(start, end, cur_node, delta):
    if cur_node is not start:
        end_left_sublist = cur_node[P_PTR]
        print_sublist(start, end_left_sublist)
    cur_line = cur_node[DATA]
    print(cur_line[ : delta] + '$' + cur_line[delta : ])    
    if cur_node is not end:    
        start_right_sublist = cur_node[N_PTR]
        print_sublist(start_right_sublist, end)
    print('\n')
    return
	
def cmd_dd(start, end, z, delta): # delete till end of line
   cur_line = z[DATA]
   new_line = cur_line[ : delta]
   z[DATA] = new_line
   return start, end, z, delta

# this function looks for a target in a double linked list
# if it finds it, it will return record and delta
# otherwise it will return None, -1
def helper_find(x_start, x_end, target):
    if x_start is not None:
        next_record = x_start
        while next_record is not None:
            cur_line = next_record[DATA]
            pos = cur_line.find(target)
            if pos >= 0:
                return next_record, pos
            else:
                next_record = next_record[N_PTR]
        return None, -1
    else:
        return None, -1
   
    
new_start, new_end = construct_linked_list(x_str)
z = get_record(new_start, new_end, 1)
delta = 3

print_file(new_start, new_end, z, delta)

new_start, new_end, z, delta = cmd_dd(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta)