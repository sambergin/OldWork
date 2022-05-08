"""
-----------------------------
CP460 (Fall 2020)
Name: Sam Bergin<---------------------------------- edit this
ID:   170670850<---------------------------------- edit this
Assignment 2
-----------------------------
"""

"""
-----------------------------
CP460 (Fall 2020)
Assignment 2 Solution
-----------------------------
"""
import utilities
import math

"""--------- Constants ----------- """
DICT_FILE = 'engmix.txt'
PAD = 'q'
BLOCK_MAX_SIZE = 20

"""
----------------------------------------------------
            Task 1: Utilities
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   text (str)
              base (str)
Return:       positions (2D list)
Description:  Analyzes a given text for any occurrence of base characters
              Returns a 2D list with characters and their respective positions
              format: [[char1,pos1], [char2,pos2],...]
              Example: get_positions('I have 3 cents.','c.h') -->
              [['h',2],['c',9],['.',14]]
              Text and base are not changed
Asserts:      text and base are strings
---------------------------------------------------
"""
def get_positions(text,base):
    positions = []
    for i in range(len(text)):
        if text[i] in base:
            positions.append([text[i], i])
    
    return positions

"""
----------------------------------------------------
Parameters:   text (str)
              base (str)
Return:       updated_text (str)
Description:  Removes all base characters from text
Asserts:      text and base are strings
---------------------------------------------------
"""
def clean_text(text,base):
    updated_text = ""

    for i in range(len(text)):
        if text[i] not in base:
            updated_text += text[i]
        else:
            updated_text += ""

    return updated_text

"""
----------------------------------------------------
Parameters:   text (str)
              positions (lsit): [[char1,pos1],[char2,pos2],...]]
Return:       updated_text (str)
Description:  Inserts all characters in the positions 2D list into their respective
Asserts:      text is a string and positions is a list
---------------------------------------------------
"""
def insert_positions(text, positions):
    textlist = list(text)
    updated_text = ""

    for i in range(len(positions)):
        textlist.insert(positions[i][1],positions[i][0])

    for i in range(len(textlist)):
        updated_text += textlist[i]
    return updated_text

"""
----------------------------------------------------
Parameters:   text (str)
              block_size (int)
              padding (bool): False/default = no padding, True = padding
              pad (str): default = PAD
Return:       blocks (list)
Description:  Create a list containing strings each of given block size
              if padding flag is set, pad using given padding character
              if no padding character given, use global PAD
Asserts:      text is a string and b_size is a positive integer
---------------------------------------------------
"""
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
Parameters:   text (string): input string
              shifts (int): number of shifts
              direction (str): 'l' or 'r'
Return:       update_text (str)
Description:  Shift a given string by given number of shifts (circular shift)
              If shifts is a negative value, direction is changed
              If no direction is given or if it is not 'l' or 'r' set to 'l'
Asserts:      text is a string and shifts is an integer
---------------------------------------------------
"""
def shift_string(text,shifts,direction ="l"):
    
    updated_text = ""
    tlist = list(text)
    
    if direction != "l" and direction != "r":
        direction = "l"
    
    if shifts < 0:
        shifts = -shifts
        if direction == "l":
            direction = "r"
        else:
            direction = "l"

    if shifts > len(text):
        shifts = shifts - ((shifts // len(text))*len(text))

    
    if direction == "r":
        shifts = len(tlist) - shifts
    
    
    right = tlist[shifts::]
    left = tlist[:shifts:]
    nlist = right + left

    for i in range(len(nlist)):
        updated_text += nlist[i]
    return updated_text

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

"""
----------------------------------------------------
            Task 2: Block Rotation Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   key (b,r): tuple(int,int)
Return:       updated_key (b,r): tuple(int,int)
Description:  Private helper function for block rotate cipher
              Update the key to smallest positive value
              if an invalid key return (0,0)
Asserts:      None
---------------------------------------------------
"""
def _adjust_key_block_rotate(key):
    updated_key = (0,0)

    if (type(key) != tuple) or (type(key[0])!= int) or type(key[1]) != int:
        return (0,0)
    elif key[0] <=1:
        return (0,0)
    
    else:
        if key[0] < key[1]:
            

            newr = (key[1] % key[0])
            updated_key = (key[0], newr)

        elif key[1] < 0:
            new = -key[1]
            newr = (key[1] % key[0])
            updated_key = (key[0], newr)
        else:
            updated_key = key

    return updated_key

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key (tuple(int,int))
Return:       ciphertext (str)
Description:  Encryption using Block Rotation Cipher
              Uses left circular rotation + padding
Asserts:      plaintext is a string
Errors:       if invalid key: 
                print: "Error(e_block_rotate): invalid key"
                return empty string
---------------------------------------------------
"""
def e_block_rotate(plaintext,key):
    ciphertext = ""

    if key == (0,0):
        print("invalid key")
    
    
    else:
        newkey = _adjust_key_block_rotate(key)
        base = ["\n"]
        pos = get_positions(plaintext, base)
        plaintext = clean_text(plaintext, base)

        blocks = text_to_blocks(plaintext,newkey[0], 1, PAD)

        for i in range(len(blocks)):
            s = shift_string(blocks[i], newkey[1])
            ciphertext += s

        ciphertext = insert_positions(ciphertext, pos)

    







    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key (tuple(int,int))
Return:       plaintext (str)
Description:  Decryption using Block Rotation Cipher
              Removes padding if it exist
Asserts:      ciphertext is a string
Errors:       if invalid key: 
                print: "Error(d_block_rotate): invalid key" 
                return empty string
---------------------------------------------------
"""
def d_block_rotate(ciphertext,key):


    plaintext = ""
    if key == (0,0):
        print("invalid key")
    
    else:
        base = ["\n"]
        pos = get_positions(ciphertext, base)
        ciphertext = clean_text(ciphertext, base)
        newkey = _adjust_key_block_rotate(key)
        blocks = text_to_blocks(ciphertext,newkey[0], 0, 0)
        base = PAD
        clean_text(blocks[len(blocks)-1], base)

        for i in range(len(blocks)):
            s = shift_string(blocks[i], newkey[1], "r")
            
            plaintext += s

        plaintext = plaintext.rstrip("q")

        plaintext = insert_positions(plaintext, pos)



    
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (string)
              arguments (list): [b0,bn,r] default = [0,0,0]
                          b0: minimum block size
                          bn: maximum block size
                          r: rotations
Return:       key,plaintext
Description:  Cryptanalysis of Block Rotate Cipher
              Returns plaintext and key (r,b)
              Attempts block sizes from b1 to b2 (inclusive)
              If bn is invalid or unspecified use BLOCK_MAX_SIZE
              Minimum valid value for b0 is 1
---------------------------------------------------
"""
def cryptanalysis_block_rotate(ciphertext,arguments=[0,0,0]):
    plaintext = ""
    plain = ""
    isp = False
    key = (0,0)
    b0 = arguments[0]
    bn = arguments[1]
    r = arguments[2]
    dict_list = utilities.load_dictionary(DICT_FILE)

    
    if b0 < 1:
        b0 = 1
    if bn < 1 or bn > BLOCK_MAX_SIZE:
        bn = BLOCK_MAX_SIZE
    if r < 1:
        r = BLOCK_MAX_SIZE

    if r == BLOCK_MAX_SIZE and b0 != bn:
        for i in range(b0,bn):
            for j in range(1,r):
                plain = d_block_rotate(ciphertext, (j,i))
                isp = utilities.is_plaintext(plain, dict_list, threshold=0.9)
                if isp == True:
                    key = _adjust_key_block_rotate((j,i))
                    plaintext = plain
    
    elif r >= 1 and b0 != bn:
        for i in range(b0,bn):
            
            plain = d_block_rotate(ciphertext, (r,i))
            isp = utilities.is_plaintext(plain, dict_list, threshold=0.9)
            if isp == True:
                key = _adjust_key_block_rotate((r,i))
                plaintext = plain
    
    elif b0 == bn:
        for i in range(1,r):
            
            plain = d_block_rotate(ciphertext, (b0,i))
            isp = utilities.is_plaintext(plain, dict_list, threshold=0.9)
            if isp == True:
                key = _adjust_key_block_rotate((b0,i))
                plaintext = plain




    return key,plaintext

"""
----------------------------------------------------
            Task 3: Wheatstone Playfair Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   text (str)
Return:       f_text (str): formatted text
Description:  Formats a plaintext
              1- Every W/w is converted to VV/vv
              2- Append an x if the text length is odd (excluding non-alpha chars)
              3- Convert every double character pair ## to #x or #X
----------------------------------------------------
"""
def _format_playfair(plaintext):
    nonalpha = utilities.get_base("nonalpha") + " "
    upper = utilities.get_base("upper")
    upper = list(upper)
    lower = utilities.get_base("lower")
    lower = list(lower)
    f_plaintext = ""

    pos = get_positions(plaintext, nonalpha)
    

    
    
    
    tlist = text_to_blocks(plaintext, 2, 0)
    
    

    

    

    for i in range(len(tlist)):
        tlist[i] = list(tlist[i])
        if tlist[i][0] == "W":
            tlist[i][0] = "VV"
        
        if len(tlist[i]) == 2 and tlist[i][1] == "W":
            tlist[i][1] = "VV"
        
        if len(tlist[i]) == 2 and tlist[i][1] == "w":
            tlist[i][1] = "vv"
        
        if tlist[i][0] == "w":
            tlist[i][0] = "vv"


        
    for i in range(len(tlist)):
        if len(tlist[i]) == 2 and tlist[i][0] == tlist[i][1]:
            if tlist[i][1] in upper:
                tlist[i][1] = "X"
            elif tlist[i][1] in lower:
                tlist[i][1] = "x"
        
        if tlist[i][0] == "VV":
            
                tlist[i][0] = "VX"
        
        if len(tlist[i]) == 2 and tlist[i][1] ==  "VV":
            
                tlist[i][1] = "VX"
        
        if tlist[i][0] ==  "vv":
            
                tlist[i][0] = "vx"
        
        if len(tlist[i]) == 2 and tlist[i][1] ==  "vv":
            
                tlist[i][1] = "vx"
            
                


    for i in range(len(tlist)):
        tlist[i] = ''.join(tlist[i])
        for j in range(len(tlist[i])):
            f_plaintext += tlist[i][j]

    
    f_plaintext = f_plaintext.rstrip("~")
    

    p2 = get_positions(f_plaintext, nonalpha)

    f_plaintext = clean_text(f_plaintext, nonalpha)

    if len(f_plaintext) % 2 != 0:
        f_plaintext += "x"
    
    f_plaintext = insert_positions(f_plaintext, p2)

    


                
                
            

    
    
    


        





    
    return f_plaintext

"""
----------------------------------------------------
Parameters:   text (str)
Return:       r_text (str): restored text
Description:  Restores a plaintext by:
              1- Converting VV/vv back to W/w
              2- Append an x if the text length is odd (excluding non-alpha chars)
              3- Convert every double character pair ## to #x or #X
Asserts:      None
----------------------------------------------------
"""
def _restore_playfair(text):   
    r_text = ""
    return r_text

"""
----------------------------------------------------
Parameters:   word (str)
              dict_list (list): 2d dictionary list
Return:       r_word (str): restored word
Description:  Restores a word by removing the 'x' character whenever necessary
              Assumes a word has no more than two x's
              Assumes word is either lower, UPPER or Capitalized
Asserts:      None
----------------------------------------------------
"""
def _restore_word_playfair(word,dict_list):
      if not utilities.is_plaintext(word, dict_list, 1):
        # Generate all permutations of x-indices
        x_positions = get_positions(word, 'Xx')
        x_position_combinations = []
        for pos_1 in x_positions:
            x_position_combinations.append([pos_1])
            for pos_2 in x_positions:
                if pos_1 != pos_2 and [pos_2, pos_1] not in x_position_combinations:
                    x_position_combinations.append([pos_1, pos_2])
        # Loop through all indices combinations
        for combination in x_position_combinations:
            cur_word_lst = [char for char in word]
            for x_position in combination:
                if x_position[1] < len(word):
                    cur_word_lst[x_position[1]] = cur_word_lst[x_position[1] - 1]
                
                cur_word = ''.join(cur_word_lst)
                if utilities.is_plaintext(cur_word, dict_list, 1):
                    return cur_word
                elif utilities.is_plaintext(cur_word[:-1].lower(), dict_list, 1):
                    return cur_word[:-1]
    return word

"""
----------------------------------------------------
Parameters:   plaintext(str)
              key (list): Playfair Square
Return:       ciphertext (str)
Description:  Encryption using Wheatstone Playfair Cipher
              Preserves all non-alpha characters
              Preserves case of characters
              Uses vv for w
              Invokes _format_playfair utility function
Asserts:      plaintext is a string and key is a list
----------------------------------------------------
"""
def e_playfair(plaintext, key):
    ciphertext = ""
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (list): Playfair Square
Return:       plaintext (str)
Description:  Decryption using Wheatstone Playfair Cipher
              Invokes _restore_playfair function to restore plaintext
Asserts:      ciphertext is a string and key is a list
----------------------------------------------------
"""
def d_playfair(ciphertext, key):
    plaintext = ""
    return plaintext

"""
----------------------------------------------------
        Task 4: Columnar Transposition Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   key (str)           
Return:       key_order (list)
Description:  Returns key order, e.g. [face] --> [1,2,3,0]
              If invalid key --> return []
              Applies to all ASCII characters from space to ~
Asserts:      None
----------------------------------------------------
"""
def _get_order_ct(key):
    key_order = []
    base = " " + utilities.get_base("all")
  

    
    keyt = type(key)
    if keyt != str or key == "":
        return key_order
    
    
    else:

        keyl = list(set(key))
            
        key3 = sorted(set(key), key=key.index)
        key = ''.join(key3)

            
        for i in range(len(keyl)):
            lvi = i
            for j in range(i + 1, len(keyl)):
                if base.find(keyl[j]) < base.find(keyl[lvi]):
                    lvi = j

            keyl[i], keyl[lvi] = keyl[lvi], keyl[i]

        
        for i in range(len(keyl)):
            key_order.append(key.find(keyl[i]))
                    


        
    return key_order

"""
----------------------------------------------------
Parameters:   plaintext (str)
              kye (str)
Return:       ciphertext (list)
Description:  Encryption using Columnar Transposition Cipher
              Does not include whitespaces in encryption
              Uses padding
Asserts:      plaintext is a string
Errors:       if key is invalid:
                print: Error(e_ct): invalid key
----------------------------------------------------
"""
def e_ct(plaintext,key):
    ciphertext = ""
    keyt = type(key)
    if keyt != str or key == "":
        print("Error(e_ct): invalid key")
    
    else:
        base = [" ", "\t", "\n", "\r"]
        
        pos = get_positions(plaintext, base)
        plaintext = clean_text(plaintext, base)
        x = 0

        key_order = _get_order_ct(key)
        
        cols = len(key_order)
        rows = math.ceil(len(plaintext)/cols)

        mat = utilities.new_matrix(rows,cols, PAD)

        for i in range(rows):
            
            for j in range(cols):
                
                if x < len(plaintext):
                    mat[i][j] = plaintext[x]
                    x += 1
                
                    
            

        for i in range(cols):
            
            for j in range(rows):
                ciphertext += mat[j][key_order[i]]

        ciphertext = insert_positions(ciphertext, pos)

    



    

    
    
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              kye (str)
Return:       plaintext (list)
Description:  Decryption using Columnar Transposition Cipher
Asserts:      ciphertext is a string
Errors:       if key is invalid:
                print: Error(d_ct): invalid key
----------------------------------------------------
"""
def d_ct(ciphertext,key):
    plaintext = ""
    keyt = type(key)
    
    if keyt != str or key == "":
        print("Error(d_ct): invalid key")

    else:
        base = [" ", "\t", "\n", "\r"]
        
        pos = get_positions(ciphertext, base)
        ciphertext = clean_text(ciphertext, base)
        x = 0

        key_order = _get_order_ct(key)
        
        
        rows = len(key_order)
        cols = math.ceil(len(ciphertext)/rows)

        mat = utilities.new_matrix(rows,cols, PAD)

        for i in range(rows):
            
            for j in range(cols):
                
                if x < len(ciphertext):
                    mat[i][j] = ciphertext[x]
                    x += 1

        
        for i in range(cols):
            
            for j in range(rows):
                plaintext += mat[key_order.index(j)][i]

        plaintext = insert_positions(plaintext, pos)
        



    
    return plaintext