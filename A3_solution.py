"""
-----------------------------
CP460 (Fall 2020)
Name: sam bergin<------------------------- edit this
ID:   170670850<------------------------- edit this
Assignment 3
-----------------------------
"""

MAX_KEY_L = 17
CIPHER_SHIFT_FACTOR = 26
PAD = "q"
dict_file = "engmix.txt"

import utilities
import math

"""
----------------------------------------------------
            Task 1: Utilities
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   text1 (str)
              text2 (str)
Return:       matches (int)
Description:  Compares two strings and returns number of matches
Assert:       text1 and text2 are strings
----------------------------------------------------
"""
def compare_texts(text1,text2):
    matches = 0
    length = 0
    

    if len(text1) >= len(text2):
        length = len(text2)

    else:
        length = len(text1)

    for i in range(length):
        if text1[i] == text2[i]:
            matches += 1 
    return matches

"""
----------------------------------------------------
Parameters:   text (str)
              [optional] base: str
Return:       count_list (list of floats) 
Description:  Finds character frequencies (count) in a given text
              Default is English language (counts both upper and lower case)
              Otherwise returns frequencies of characters defined in base
Assert:       text is a string
----------------------------------------------------
"""
def get_freq(text,base = None):
    count_list = []
    
    if base == None:
        base = utilities.get_base("lower")
        
        for i in range(len(base)):
            temp = 0
            for j in range(len(text)):
                if base[i] == text[j].lower():
                    temp += 1
            count_list.append(temp)

    else:
        base = utilities.get_base(base)
        
        for i in range(len(base)):
            temp = 0
            for j in range(len(text)):
                if base[i] == text[j]:
                    temp += 1
            count_list.append(temp)

   


   

    return count_list

"""
----------------------------------------------------
Parameters:   text(str)
              [optional] base_type(str)
Return:       I (float): Index of Coincidence
Description:  Computes and returns the index of coincidence 
              Uses English alphabets, or specified base_type
Asserts:      text is a string
----------------------------------------------------
"""
def index_of_coin(text, base_type = None):
    
    
    l = get_freq(text,base_type)
    x = len(l)
    
    I = 0.0
    N = 0

    if len(text) == 0 or len(l) == 0:
        I = 0.00000
    else:

        for i in range(0,x):
            
            I += l[i] * (l[i]-1)
            N += l[i]
        if N == 0 or N-1 == 0:
            I = 0.00000
        else:

        
            I = I / (N*(N-1))
    
    
    
   

        
    return I

"""
----------------------------------------------------
Parameters:   text (str)
              [optional] language (str)
Return:       result (float)
Description:  Calculates the Chi-squared statistics 
              for given text against given language
              Only alpha characters are considered
Asserts:      text is a string
Errors:        if language is unsupported:
                    print error msg: 'Error(chi_squared): unsupported language'
                    return -1
----------------------------------------------------
"""
def chi_squared(text,language='English'):
    result = 0.0
    
    x = 0
    
    if len(text) != 0 and language == "English":
        E = utilities.get_language_freq(language)
        C = get_freq(text)
        
        for i in range(len(C)):
            x += C[i]
        
        for i in range(len(C)):
            
            result += (C[i] - (E[i] * x))**2 / (E[i] * x)
        
            
    else:
        result = -1.000
    

    
    return result

"""
----------------------------------------------------
            Task 2: Vigenere Cipher
----------------------------------------------------
"""
"""
----------------------------------------------------
Parameters:   None 
Return:       v_square (list of strings)
Description:  Constructs Vigenere square as list of strings
              element 1 = "abcde...xyz"
              element 2 = "bcde...xyza" (1 shift to left)
              ...
----------------------------------------------------
"""
def _vigenere_square():
    v_square = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in range(26):
        temp = utilities.shift_string(alpha, i, "l")
        v_square.append(temp)
        temp = ""

    return v_square

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key (str)
Return:       ciphertext (str)
Description:  Encryption using Vigenere Cipher
              Key could be an autokey or a running key
Asserts:      plaintext is a string
Error:        if invalid key:
                print error msg: Error(e_vigenere): invalid key
                return empty string
----------------------------------------------------
"""
def e_vigenere(plaintext,key):
    ciphertext = []
    plaintext2 = []
    square = _vigenere_square()
    x = 0
    y = 0
    c = 0
    base = utilities.get_base("nonalpha")
    base += " \n"
    
    pos = utilities.get_positions(plaintext, base)
    plaintext = utilities.clean_text(plaintext, base)
    

    if len(key)==0:
        print("Error(e_vigenere): invalid key")
        ciphertext = ""

    elif len(key) == 1:
        plaintext = list(plaintext)
        plaintext2 = plaintext.copy()
        plaintext2.insert(0, key)
        plaintext2.pop()
        
        while len(ciphertext) != len(plaintext):

            for i in range(26):
                if square[i][0] == plaintext[c].lower():
                    x = i
            for j in range(26):
               
                if square[0][j] == plaintext2[c].lower():
                    y = j
            
            
           
               
            ciphertext.append(square[x][y])
            c += 1
    else:
        plaintext = list(plaintext)
        while len(plaintext2) != len(plaintext):
            if c >= len(key):
                c = 0
            plaintext2.append(key[c])
            c+= 1
        c = 0
        
        while len(ciphertext) != len(plaintext):

            for i in range(26):
                if square[i][0] == plaintext[c].lower():
                    x = i
            for j in range(26):
               
                if square[0][j] == plaintext2[c].lower():
                    y = j
            ciphertext.append(square[x][y])
            c += 1

    
    if len(key) != 0:
        ciphertext = "".join(ciphertext)
        ciphertext = utilities.insert_positions(ciphertext, pos)
        ciphertext = list(ciphertext)
        plaintext = "".join(plaintext)
        plaintext = utilities.insert_positions(plaintext, pos)
        
        for i in range(len(plaintext)):
            if plaintext[i].isupper():
                ciphertext[i] = ciphertext[i].upper()

        
        ciphertext = "".join(ciphertext)




    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key (str)
Return:       plaintext (str)
Description:  Decryption using Vigenere Cipher
              Key could be an autokey or a running key
Asserts:      ciphertext is a string
Error:        if invalid key:
                print error msg: Error(e_vigenere): invalid key
                return empty string
----------------------------------------------------
"""
def d_vigenere(ciphertext,key):
    plaintext = []
    plaintext2 = []
    square = _vigenere_square()
    c = 0
    

    base = utilities.get_base("nonalpha")
    base += " \n"
    pos = utilities.get_positions(ciphertext, base)
    ciphertext = utilities.clean_text(ciphertext, base)

    if len(key) == 0:
        print("Error(d_vigenere): invalid key")
        plaintext = ""

    elif len(key) == 1:
        plaintext2.append(key)

        while len(ciphertext) != len(plaintext):

            for i in range(26):
                if square[0][i] == plaintext2[c].lower():
                    y = i
            for j in range(26):
               
                if square[j][y] == ciphertext[c].lower():
                    x = j

            plaintext.append(square[x][0])
            plaintext2.append(square[x][0])
            c += 1
    else:
        ciphertext = list(ciphertext)
        while len(plaintext2) != len(ciphertext):
            if c >= len(key):
                c = 0
            plaintext2.append(key[c])
            c+= 1
        c = 0
        while len(plaintext) != len(ciphertext):
            for i in range(26):
                if square[0][i] == plaintext2[c].lower():
                    y = i
            for j in range(26):
               
                if square[j][y] == ciphertext[c].lower():
                    x = j

            plaintext.append(square[x][0])
            plaintext2.append(square[x][0])
            c += 1



            


    if len(key) != 0:
        plaintext = "".join(plaintext)
        plaintext = utilities.insert_positions(plaintext, pos)
        plaintext = list(plaintext)
        ciphertext = utilities.insert_positions(ciphertext, pos)
        
        for i in range(len(plaintext)):
            if ciphertext[i].isupper() == True:
                plaintext[i] = plaintext[i].upper()

        
        plaintext = "".join(plaintext)
    

    





    
    return plaintext


"""
----------------------------------------------------
            Task 3: Shift Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key (int,str): (shifts,base)
Return:       ciphertext (str)
Description:  Encryption using shift cipher
              The base is applied to circular left shift by "shifts"
              if shifts is None, The shift is done on lower case alphabet
                  case of the characters is preserved.
Asserts:      plaintext is a string
Error:        if invalid key:
                print error msg: Error(e_shift): invalid key
                return empty string
----------------------------------------------------
"""
def e_shift(plaintext,key):
    ciphertext = []
    
    if type(key) != tuple or type(key[0]) != int or (key[1]!=None and type(key[1]) != str) or (key[1]!=None and len(key[1]) == 0):
        print("Error(e_shift): invalid key")
        ciphertext = ""
    else:
        if key[1] == None:
            base = utilities.get_base("lower")
        else:
            base = key[1]

        
        
        base2 = utilities.shift_string(base, key[0], "l")
        base2 = list(base2)
        base = list(base)
        
        plaintext = list(plaintext)

        if key[1] == None:
            for i in range(len(plaintext)):
                if plaintext[i].lower() in base:
                    for j in range(len(base)):
                        if plaintext[i].lower() == base[j]:
                            if plaintext[i].isupper():

                                ciphertext.append(base2[j].upper())
                            else:
                                ciphertext.append(base2[j])
                else:
                    ciphertext.append(plaintext[i])
        else:
            
            for i in range(len(plaintext)):
                if plaintext[i] in base:
                    for j in range(len(base)):
                        if plaintext[i] == base[j]:
                            ciphertext.append(base2[j])
                else:
                    ciphertext.append(plaintext[i])

        ciphertext = "".join(ciphertext)





    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key (int,str): (shifts,base)
Return:       plaintext (str)
Description:  Decryption using shift cipher
              The base is applied to circular left shift by "shifts"
              if shifts is None, The shift is done on lower case alphabet
                  case of the characters is preserved.
Asserts:      ciphertext is a string
Error:        if invalid key:
                print error msg: Error(d_shift): invalid key
                return empty string
----------------------------------------------------
"""
def d_shift(ciphertext,key):
    plaintext = []
    
    
    if type(key) != tuple or type(key[0]) != int or (key[1]!=None and type(key[1]) != str) or (key[1]!=None and len(key[1]) == 0):
        print("Error(d_shift): invalid key")
        plaintext = ""
    else:
        if key[1] == None:
            base = utilities.get_base("lower")
        else:
            base = key[1]

        
        
        base2 = utilities.shift_string(base, key[0], "l")
        base2 = list(base2)
        base = list(base)
        
        ciphertext = list(ciphertext)

        if key[1] == None:
            for i in range(len(ciphertext)):
                if ciphertext[i].lower() in base:
                    for j in range(len(base)):
                        if ciphertext[i].lower() == base2[j]:
                            if ciphertext[i].isupper():

                                plaintext.append(base[j].upper())
                            else:
                                plaintext.append(base[j])
                else:
                    plaintext.append(ciphertext[i])
        else:
            
            for i in range(len(ciphertext)):
                if ciphertext[i] in base:
                    for j in range(len(base)):
                        if ciphertext[i] == base2[j]:
                            plaintext.append(base[j])
                else:
                    plaintext.append(ciphertext[i])

        plaintext = "".join(plaintext)
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              [optional] base_type (str/None)
Return:       key (int)
              plaintext (str)
Description:  Uses chi_squared method to restore plaintext
              Assume 
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def cryptanalysis_shift(ciphertext,base_type = None):
    key = 0
    plaintext = ""
    chi = 1000000000
    temp = 0

    if base_type != None:
        base_type = utilities.get_base(base_type)

    for i in range(1,25):
        text = d_shift(ciphertext, (i,base_type))
        temp = chi_squared(text)
        if temp < chi:
            chi = temp
            key = i
            plaintext = text




    
    
    
    return key,plaintext

"""
----------------------------------------------------
            Task 4: Vigenere Cryptanalysis
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   blocks (list of str)
Return:       baskets: (list of str)
Description:  Create k baskets, where k = key length = block size
              basket[i] contains character ith from each block in consecutive order
              Assume all blocks are of the same type
----------------------------------------------------
"""
def _blocks_to_baskets(blocks):
    k = len(blocks[0])
    baskets = []

    for i in range(k):
        baskets.append("")

    for i in range(k):
        for j in range(len(blocks)):
            if len(blocks[j]) == k:
                baskets[i] += blocks[j][i]
            else:
                for x in range(len(blocks[j])):
                    if x == i:
                        baskets[i] += blocks[j][x]



    

    

    return baskets

"""
----------------------------------------------------
Parameters:   ciphertext(str)
Return:       list of two key lengths [int,int]
Description:  Uses Friedman's test to compute key length
              returns best two candidates for key length
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def friedman(ciphertext):
    L = len(ciphertext)
    
    I = index_of_coin(ciphertext, None)
   

    top = 0.0265 * L
    bot = (0.065 - I) + (L * (I - 0.0385))

    k = top / bot
    
    if (k % 1) > 0.5:
        
        k = math.ceil(k)
        k1 = k
        k2 = k-1
        return [k1,k2]
    else:
        
        k = math.floor(k)
        k1 = k
        k2 = k + 1
        return [k1,k2]

    
    
    return [k1,k2]

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              [optional] max_key_length (int)
Return:       list of two key lengths [int,int]
Description:  Uses Cipher shifting to compute key length
              returns betw two candidates for key length
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def cipher_shifting(ciphertext,max_key = MAX_KEY_L):
    k1 = -1 
    k2 = -1
    matches = 0
    matches2 = 0
    base = utilities.get_base("nonalpha") + " \n\t"
    ciphertext = utilities.clean_text(ciphertext, base)

    ciphertext = list(ciphertext)
    text = ciphertext.copy()

    for i in range(1, CIPHER_SHIFT_FACTOR):
        text.insert(0, " ")
        text.pop()
        
        temp = compare_texts("".join(ciphertext), "".join(text))
        
        
        if temp > matches:
            if matches > matches2:
                k2 = k1
                matches2 = matches
            
            matches = temp
            if i <= max_key:
                k1 = i
            else:
                k1 = i % max_key
            
        elif temp > matches2:
            matches2 = temp
            if i <= max_key:
                k2 = i
            else: k2 = i % max_key
            

    return [k1,k2]

"""
----------------------------------------------------
Parameters:   ciphertext (str)
Return:       list of two key lengths
Description:  Combines results of Friedman and Cipher shifting
              to produce a list of best candidates
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def _cryptanalysis_vigenere_key_length(ciphertext):
    l1, l2 = friedman(ciphertext)
    l3, l4 = cipher_shifting(ciphertext)
    k = []

    if l1 == l3 or l1 == l4:
        k.append(l1)
       
        if l2 not in k:
            k.append(l2)
        if l3 not in k:
            k.append(l3)
        if l4 not in k:
            k.append(l4)
    
    elif l2 == l3 or l2 == l4:
        k.append(l2)
        if l1 not in k:
            k.append(l1)
        if l3 not in k:
            k.append(l3)
        if l4 not in k:
            k.append(l4)
    
    else:
        k.append(l1)
        if l2 not in k:
            k.append(l2)
        if l3 not in k:
            k.append(l3)
        if l4 not in k:
            k.append(l4)

    


    

    return k

"""
----------------------------------------------------
Parameters:   ciphertext (str)
Return:       key (str)
              plaintext (str)
Description:  Cryptanalysis of Vigenere cipher
              If cryptanalysis fails, return two empty strings
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def cryptanalysis_vigenere(ciphertext):
    key = ""
    plaintext = ""
    """
    base = utilities.get_base("nonalpha") + " \n\t"
    base2 = utilities.get_base("lower")
    pos = utilities.get_positions(ciphertext, base)
    ciphertext = utilities.clean_text(ciphertext, base)
    text = ciphertext.lower()
    dict_list = utilities.load_dictionary(dict_file)
    isp = False

    key_ls = _cryptanalysis_vigenere_key_length(ciphertext)

    
    
    for i in range(len(key_ls)):
        blocks = utilities.text_to_blocks(ciphertext, key_ls[i])
        baskets = _blocks_to_baskets(blocks)

        for j in range(len(baskets)):
            k, _ = cryptanalysis_shift(baskets[j])
            key += base2[k]

        ciphertext = utilities.insert_positions(ciphertext, pos)
        
        plaintext = d_vigenere(ciphertext, key)
            
        ptc = utilities.is_plaintext(plaintext, dict_list)
        if ptc == True:
            return key,plaintext
    """







    return key, plaintext

"""----------------------------
Columnar Transposition Cipher
----------------------------"""