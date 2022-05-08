"""
-----------------------------
CP460 (Fall 2020)
Name:Sam Bergin <------------------------- edit this
ID: 170670850  <------------------------- edit this
Bonus Assignment
-----------------------------
"""

import utilities
import math

"""
----------------------------------------------------
            Task 1: Permutation Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   key (?)
Return:       True/False
Description:  Private helper for Permutation Cipher
              Check if given key is a valid permutation key
----------------------------------------------------
"""
def _is_valid_key_permutation(key):
    base = utilities.get_base("alpha") + utilities.get_base("special")
    if type(key) != tuple or type(key[0]) != str or type(key[1]) != str or len(key) != 2:
        
        return False
    
    if key[1] != "block" and key[1] != "stream":
        
        return False
    
    
    for i in key[0]:
        for j in range(len(base)):
            if i == base[j]:
                
                return False
    
    test = [int(i) for i in key[0]]
    
    lent = []
    for i in range(1,len(test)+1):
        lent.append(i)
    

    for i in test:
        if lent.__contains__(i) == False:

            return False
        
    
    
    return True

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key(k,mode) tuple(str,str)
Return:       ciphertext (str)
Description:  Encryption using permutation cipher
              defined modes: stream and block
              Uses Padding in block mode
Asserts:      plaintext is a string
Errors:       if invalid key: print error msg and return ''
----------------------------------------------------
"""
def e_permutation(plaintext,key):
    ciphertext = ""
    if _is_valid_key_permutation(key) == False:
        print("Error(e_permutation): invalid key")
        return ""
    if key[1] == "stream":
        ciphertext = e_ct(plaintext, key[0])
    else:
        blocks = utilities.text_to_blocks(plaintext, len(key[0]), 1, "q")
        test = [int(i) for i in key[0]]
        
        for i in range(len(blocks)):
            block2 = ""
            
            for j in test:
                block2 += blocks[i][j-1]
            
            ciphertext += block2


    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key(k,mode) tuple(str,str)
Return:       plaintext (str)
Description:  Decryption using permutation cipher
              defined modes: stream and block
              Uses Padding in block mode
Asserts:      ciphertext is a string
Errors:       if invalid key: print error msg and return ''
----------------------------------------------------
"""
def d_permutation(ciphertext,key):
    plaintext = ""
    text = ""
    if _is_valid_key_permutation(key) == False:
        print("Error(d_permutation): invalid key")
        return ""
    if key[1] == "stream":
        text = d_ct(ciphertext, key[0])
        plaintext = text.rstrip("q")
    else:
        blocks = utilities.text_to_blocks(ciphertext, len(key[0]), 1, "q")
        test = [int(i) for i in key[0]]
        k = []
        for i in range(1,len(test)+1):
            for j in range(len(test)):
                if i == test[j]:
                    k.append(j)
        
        
        
        for i in range(len(blocks)):
            block2 = ""
            for l in k:
                block2 += blocks[i][l]
            
            
            

            text += block2

    plaintext = text.rstrip("q")    
    
    return plaintext

"""
----------------------------------------------------
            Task 2: ADFGVX Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   None 
Return:       adfgvx_square (2D list)
Description:  Returns Polybius square to be used in ADFGVX cipher
----------------------------------------------------
"""
def _adfgvx_square():
    # your code here
    return [["F", "L", "1", "A", "O", "2"], 
            ["J", "D", "W", "3", "G", "U"],
            ["C", "I", "Y", "B", "4", "P"],
            ["R","5","Q","8", "V", "E"],
            ["6","K", "7", "Z", "M", "X"],
            ["S","N","H","0","T","9"]]
    
"""
----------------------------------------------------
Parameters:   plaintext(str)
              key (str)
Return:       ciphertext (str)
Description:  Encryption using ADFGVX Cipher
----------------------------------------------------
"""
def e_adfgvx(plaintext, key):
    # your code here
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (str)
Return:       plaintext (str)
Description:  Decryption using ADFGVX Cipher
----------------------------------------------------
"""
def d_adfgvx(ciphertext, key):
    # your code here
    return plaintext

"""
----------------------------------------------------
            Task 3: Myszkowski Cipher
----------------------------------------------------
"""
"""
----------------------------------------------------
Parameters:   plaintext(str)
              key (str)
Return:       ciphertext (str)
Description:  Encryption using Myszkowsi Transposition Cipher
              Applied to all characters, except white space chars
              Uses padding if necessary (default PAD)
Asserts:      plaintext is a string
Errors:       If key is invalid, return empty string and
                    print 'Error(e_myszkowski): invalid key'
----------------------------------------------------
"""
def e_myszkowski(plaintext,key):
    # your code here
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (str)
Return:       plaintext (str)
Description:  Decryption using Myszkowsi Transposition Cipher
              Applied to all characters, except white space chars
              Uses padding if necessary (default PAD)
Asserts:      ciphertext is a string
Errors:       If key is invalid, return empty string and
                    print 'Error(d_myszkowski): invalid key'
----------------------------------------------------
"""
def d_myszkowski(ciphertext,key):
    plaintext = ""
    text = ""
    pos = utilities.get_positions(ciphertext, " \n\t")
    ciphertext = utilities.clean_text(ciphertext, " \n\t")

    rows = math.ceil(len(ciphertext) / len(key))
    cols = len(key)
    key2 = sorted(key)
    key2 = list(dict.fromkeys(key2))
    
    
    mat = utilities.new_matrix(rows, cols, utilities.PAD)
    
    
    c = 0
    
    
    for i in range(len(key2)):
        for j in range(rows):
            for k in range(cols):
                if key2[i] == key[k] and c < len(ciphertext):
                    mat[j][k] = ciphertext[c]
                    c += 1
        
        

    for i in range(rows):
        for j in range(cols):
            plaintext += mat[i][j]
    
    plaintext = utilities.insert_positions(plaintext, pos)
    
    plaintext = plaintext.rstrip("q")




    return plaintext

"""
----------------------------------------------------
Parameters:   key (str)
Return:       key_order (list)
Description:  Construct a list corresponding to the order of characters
                in the key
              Key should be a string that:
                contains at least one repeated character
                contains at least one non-repeated character
                Ignores non-lower case characters
              If key is invalid, returns empty list
----------------------------------------------------
"""
def _get_order_myszkowski(key):
    # your code here
    return key_order


"""
----------------------------------------------------
            Columnar Transposition Cipher
----------------------------------------------------
"""

# Add code from A2 here
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
def e_ct(plaintext,key):
    ciphertext = ""
    keyt = type(key)
    if keyt != str or key == "":
        print("Error(e_ct): invalid key")
    
    else:
        base = [" ", "\t", "\n", "\r"]
        
        pos = utilities.get_positions(plaintext, base)
        plaintext = utilities.clean_text(plaintext, base)
        x = 0

        key_order = _get_order_ct(key)
        
        cols = len(key_order)
        rows = math.ceil(len(plaintext)/cols)

        mat = utilities.new_matrix(rows,cols,"q")

        for i in range(rows):
            
            for j in range(cols):
                
                if x < len(plaintext):
                    mat[i][j] = plaintext[x]
                    x += 1
                
                    
            

        for i in range(cols):
            
            for j in range(rows):
                ciphertext += mat[j][key_order[i]]

        ciphertext = utilities.insert_positions(ciphertext, pos)

    



    

    
    
    return ciphertext

def d_ct(ciphertext,key):
        plaintext = ""
        keyt = type(key)
        
        if keyt != str or key == "":
            print("Error(d_ct): invalid key")

        else:
            base = [" ", "\t", "\n", "\r"]
            
            pos = utilities.get_positions(ciphertext, base)
            ciphertext = utilities.clean_text(ciphertext, base)
            x = 0

            key_order = _get_order_ct(key)
            
            
            rows = len(key_order)
            cols = math.ceil(len(ciphertext)/rows)

            mat = utilities.new_matrix(rows,cols, "q")

            for i in range(rows):
                
                for j in range(cols):
                    
                    if x < len(ciphertext):
                        mat[i][j] = ciphertext[x]
                        x += 1

            
            for i in range(cols):
                
                for j in range(rows):
                    plaintext += mat[key_order.index(j)][i]

            plaintext = utilities.insert_positions(plaintext, pos)
            



        
        return plaintext