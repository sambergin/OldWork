"""
-----------------------------
CP460 (Fall 2020)
Utilities
Bonus Assignment
-----------------------------
"""
import string
import math

PAD = 'q'

# 1-    get_base(base_type)
# 2-    file_to_text(filename)
# 3-    text_to_file(text,filename)
# 4-    text_to_block(text,b_size,padding=0,pad=PAD)
# 5-    get_positions(text,base)
# 6-    clean_text(text,base)
# 7-    insert_positions(text, positions)
# 8-    new_matrix(r,c,fill)
# 9-    index_2d(input_list,item)
def file_to_text(filename):
    infile = open(filename,'r')
    contents = infile.read()
    infile.close()
    return contents
def get_positions(text,base):
    positions = []
    for i in range(len(text)):
        if text[i] in base:
            positions.append([text[i], i])
    
    return positions
def insert_positions(text, positions):
    textlist = list(text)
    updated_text = ""

    for i in range(len(positions)):
        textlist.insert(positions[i][1],positions[i][0])

    for i in range(len(textlist)):
        updated_text += textlist[i]
    return updated_text
def clean_text(text,base):
    updated_text = ""

    for i in range(len(text)):
        if text[i] not in base:
            updated_text += text[i]
        else:
            updated_text += ""

    return updated_text

def text_to_file(text, filename):
    outfile = open(filename,'w')
    outfile.write(text)
    outfile.close()
    return
def new_matrix(r,c,fill):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[fill] * c for i in range(r)]
def text_to_blocks(text,b_size,padding = 0,pad =PAD):
    blocks = []
    tempstr = ""
    c = 1
    for i in range(len(text)):
        if c <= b_size and i != len(text)-1:
            tempstr += text[i]
            c += 1
        
        elif i == len(text)-1 and padding != 1:
            if len(tempstr) == b_size:
                blocks.append(tempstr)
                tempstr = ""
                tempstr += text[i]
                blocks.append(tempstr)
            else:
                tempstr += text[i]
                blocks.append(tempstr)



        elif c <= b_size and i == len(text)-1 and padding == 1:
            tempstr += text[i]
            c += 1
            while c <= b_size:
                tempstr += pad
                c += 1
            blocks.append(tempstr)

        
        else:
            blocks.append(tempstr)
            tempstr = ""
            tempstr += text[i]
            c = 2

        


    return blocks

"""
----------------------------------------------------
Parameters:   input_list (list): 2D list
              item (?)
Return:       i,j (int,int)
Description:  Performs linear search on input list to find "item"
              returns i,j, where i is the row number and j is the column number
              if not found returns -1,-1
Asserts:      input_list is a list
---------------------------------------------------
"""
def index_2d(input_list,item):
    i1 = -1
    
    for i in range(len(input_list)):
        if item in input_list[i]:
            i1 = i
    for i in range(len(input_list[i1])):
        if item == input_list[i1][i]:
            return i1, i
    

    return -1,-1

def get_base(base_type):
    lower = "".join([chr(ord('a')+i) for i in range(26)])
    upper = lower.upper()
    num = "".join([str(i) for i in range(10)])
    special = ''
    for i in range(ord('!'),127):
        if not chr(i).isalnum():
            special+= chr(i)
            
    result = ''
    if base_type == 'lower':
        result = lower
    elif base_type == 'upper':
        result = upper
    elif base_type == 'alpha':
        result = upper + lower
    elif base_type == 'num':
        result = num
    elif base_type == 'lowernum':
        result = lower + num
    elif base_type == 'uppernum':
        result = upper + num
    elif base_type == 'alphanum':
        result = upper + lower + num
    elif base_type == 'special':
        result = special
    elif base_type == 'nonalpha':
        result = special + num
    elif base_type == 'all':
        result = upper + lower + num + special
    else:
        print('Error(get_base): undefined base type')
        result = ''
    return result