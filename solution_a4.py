"""
-----------------------------
CP460 (Fall 2020)
Name: sam bergin<------------------------- edit this
ID:   170670850<------------------------- edit this
Assignment 4
-----------------------------
"""
import math
import string
import mod
import matrix
import utilities

#---------------------------------
# Q1: Modular Arithmetic Library #
#---------------------------------

# solution is available in mod.py

#---------------------------------
#     Q2: Decimation Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (tuple): (base(str), k(int))
# Return:       ciphertext (str)
# Description:  Encryption using Decimation Cipher
#               Encrypts only characters defined in the base
#               Case of characters should be preserved (whenever possible)
# Asserts:      plaintext is a string
# Errors:       if invalid key, e.g. has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_decimation(plaintext,key):
    if mod.has_mul_inv(key[1], len(key[0])) == False:
        print("Error(e_decimation): Invalid key")
        return ""
    
    spec = " "
    base = key[0]
    mul = key[1]
    ciphertext = ""
    
    #text = utilities.clean_text(plaintext, spec)

    text = plaintext.lower()
    x = 0
    
    for i in range(len(plaintext)):
        if text[i] in base:
            for j in range(len(base)):
                if text[i] == base[j]:
                    x = mul * j
                while x >= len(base):
                    x -= len(base)

            if plaintext[i].isupper():    
                ciphertext += base[x].upper()
            else:
                ciphertext += base[x]
        else:
            ciphertext += text[i]
                
    
    

    
            

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (tuple): (base(str), k(int))
# Return:       plaintext (str)
# Description:  Decryption using Decimation Cipher
#               Decrypts only characters defined in the base
#               Case of characters should be preserved (whenever possible)
# Asserts:      ciphertext is a string
# Errors:       if invalid key, e.g. has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_decimation(ciphertext,key):
    plaintext = ""
    if mod.has_mul_inv(key[1], len(key[0])) == False:
        print("Error(d_decimation): Invalid key")
        return ""
    
    
    base = key[0]
    mul = key[1]
    plaintext = ""
    
    

    text = ciphertext.lower()
    x = 0
    
    for i in range(len(ciphertext)):
        if text[i] in base:
            for j in range(len(base)):
                if text[i] == base[j]:
                    x = (j * mod.mul_inv(mul, len(base)))
                    while x >= len(base):
                        x -= len(base)
                
                
                
                

            if ciphertext[i].isupper():    
                plaintext += base[x].upper()
            else:
                plaintext += base[x]
        else:
            plaintext += text[i]
    
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       key (tuple) (base,k)
#               plaintext (str)
#               counter (int): number of attempted keys
# Description:  Cryptanalysis of Decimation Cipher
#               Assumes subset of get_base('lower) + get_base('nonalpha')
#                 starting at 'a' and holding consecutive characters
#               If it fails, return: '','',0
# Asserts:      ciphertext is a non-empty string
#-----------------------------------------------------------
def cryptanalysis_decimation(ciphertext):
    major_base = utilities.get_base("lower") + utilities.get_base("nonalpha")
    base = "abc"
    dic = utilities.load_dictionary("engmix.txt")
    
    plaintext = ""
    c = 0
    keys = []

    

    for i in range(3,len(major_base)):
        base = major_base[:i]
        keys = []
        for i in range(len(major_base)):
            if mod.is_relatively_prime(i, len(base)) and i != 1 and i < len(base):
                keys.append(i)
        
       
           
            
        for k in keys:
                    
            if mod.has_mul_inv(k, len(base)) == True:
                    
                text = d_decimation(ciphertext, [base, k])
                isp = utilities.is_plaintext(text, dic)
                    
                c += 1
                if isp:
                            
                            
                    return [base, k], text, c
                    
       
            




    return '','', 0

#---------------------------------
#      Q3: Affine Cipher         #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (tuple): (base(str), [alpha(int),beta(int)])
# Return:       ciphertext (str)
# Description:  Encryption using Affine Cipher
#               Encrypts only characters defined in the base
#               Case of characters should be preserved (whenever possible)
# Asserts:      plaintext is a string
# Errors:       if invalid key -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_affine(plaintext,key):
    

    ciphertext = ""
    base = key[0]
    a = key[1][0]
    b = key[1][1]

    text = plaintext.lower()
    x = 0
    if (mod.has_mul_inv(key[1][0], len(base))) == False:
        print("Error(e_affine): Invalid key")
        return ""
    
    for i in range(len(plaintext)):
        if text[i] in base:
            for j in range(len(base)):
                if text[i] == base[j]:
                    x = ((a * j) + b) % len(base)
                while x >= len(base):
                    x -= len(base)

            if plaintext[i].isupper():    
                ciphertext += base[x].upper()
            else:
                ciphertext += base[x]
        else:
            ciphertext += text[i]


    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,[int,int])
# Return:       plaintext (str)
# Description:  Decryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_affine(ciphertext,key):
    
    plaintext = ""
    
    
    
    base = key[0]
    a = key[1][0]
    b = key[1][1]
    plaintext = ""
    if (mod.has_mul_inv(key[1][0], len(base))) == False:
        print("Error(e_affine): Invalid key")
        return ""
    
    

    text = ciphertext.lower()
    x = 0
    
    for i in range(len(ciphertext)):
        if text[i] in base:
            for j in range(len(base)):
                if text[i] == base[j]:
                    x = (mod.mul_inv(a, len(base)) * (j - b)) % len(base)
                while x >= len(base):
                    x -= len(base)
                    
                
                
                
                

            if ciphertext[i].isupper():    
                plaintext += base[x].upper()
            else:
                plaintext += base[x]
        else:
            plaintext += text[i]
    
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       key (tuple) (base,k)
#               plaintext (str)
#               counter (int): number of attempted keys
# Description:  Cryptanalysis of Affine Cipher
#               Assumes subset of get_base('lower) + get_base('nonalpha')
#                 starting at 'a' and holding consecutive characters
#               If it fails, return: '','',0
# Asserts:      ciphertext is a non-empty string
#-----------------------------------------------------------
def cryptanalysis_affine(ciphertext):
    major_base = utilities.get_base("lower") + utilities.get_base("nonalpha")
    base = ""
    dic = utilities.load_dictionary("engmix.txt")
    
    plaintext = ""
    c = 0
    keys = []

    

    for i in range(1,len(major_base)):
        

        base = major_base[:i]
        keysa = []
        keysb = []
        for j in range(len(base)):
            
            keysb.append(j)
            if mod.is_relatively_prime(j, len(base)) and j != 0 and j < len(base):
                keysa.append(j)
                
            
        for k in keysa:
            for k2 in keysb:
                    
                if mod.has_mul_inv(k, len(base)) == True:
                    
                    if not (k == 1 and k2 == 0):
                        
                            
                        text = d_affine(ciphertext, [base,[k,k2]])
                        isp = utilities.is_plaintext(text, dic)
                                
                        c += 1
                        if isp:
                                        
                                        
                            return [base, [k, k2]], text, c
                        
       
            




    return '','', 0

#---------------------------------
#      Q4: Matrix Library        #
#---------------------------------

# solution is available in matrix.py

#---------------------------------
#       Q5: Hill Cipher          #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str)
# Return:       ciphertext (str)
# Description:  Encryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Encrypts only alphabet characters
#               Deals with plaintext as lower case, 
#               and produces upper case ciphertext
#               If necessary use default padding
# Errors:       if key is is invalid:
#                   print error msg and return empty string
# Asserts:      plaintext is a non-empty string
#-----------------------------------------------------------
def e_hill(plaintext,key):
    nk = ""
    ciphertext = ""
    base = utilities.get_base("lower")
    specs = utilities.get_base("nonalpha") + " "
    keyl = []
    
    if len(key) < 4:
        nk = key
        l = 4-len(nk)
        for i in range(l):
            nk += key[i]
        
    
    elif len(key) > 4:
        for i in range(4):
            nk += key[i]
    else:
        nk = key

    mat = matrix.new_matrix(2,2,0)
    
    for i in range(len(nk)):
        for j in range(len(base)):
            if nk[i] == base[j]:
                keyl.append(j)
    
    
    mat[0][0] += keyl[0]
    mat[0][1] += keyl[1]
    mat[1][0] += keyl[2]
    mat[1][1] += keyl[3]
    
    


    d = matrix.det(mat)
    if (mod.has_mul_inv(d, 26) == False):
        print("Error(e_hill): key is not invertible")
        return ""

    plaintext = plaintext.lower()
    pos = utilities.get_positions(plaintext, specs)
    text = utilities.clean_text(plaintext, specs)
    x = 0
    
    if len(text) % 2 != 0:
        text += "q"
    
    while x < len(text):
        temp = matrix.new_matrix(2,1,0)
        for i in range(len(base)):
            if text[x] == base[i]:
                temp[0] = [i]
            if text[x+1] == base[i]:
                temp[1] = [i]
        
        
        c2 = matrix.mul(mat, temp)
        
        c2 = matrix.matrix_mod(c2, 26)
        


        ciphertext += base[c2[0][0]].upper()
        ciphertext += base[c2[1][0]].upper()

        x += 2
    

    ciphertext = utilities.insert_positions(ciphertext,pos)




        
    
    
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str)
# Return:       plaintext (str)
# Description:  Decryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Decrypts only alphabet characters
#               Deals with ciphertext as upper case, 
#               and produces lower case plaintext
#               If necessary remove paddingpadding
# Errors:       if key is is invalid:
#                   print error msg and return empty string
# Asserts:      ciphertext is a non-empty string
#-----------------------------------------------------------
def d_hill(ciphertext,key):
    nk = ""
    plaintext = ""
    base = utilities.get_base("lower")
    specs = utilities.get_base("nonalpha") + " "
    keyl = []
    
    if len(key) < 4:
        nk = key
        l = 4-len(nk)
        for i in range(l):
            nk += key[i]
        
    
    elif len(key) > 4:
        for i in range(4):
            nk += key[i]
    else:
        nk = key

    mat = matrix.new_matrix(2,2,0)
    
    for i in range(len(nk)):
        for j in range(len(base)):
            if nk[i] == base[j]:
                keyl.append(j)
    
    
    mat[0][0] += keyl[0]
    mat[0][1] += keyl[1]
    mat[1][0] += keyl[2]
    mat[1][1] += keyl[3]
    
    
    mat2 = matrix.inverse(mat, 26)
    mat2 = matrix.matrix_mod(mat2, 26)
    
    

    d = matrix.det(mat)
    if (mod.has_mul_inv(d, 26) == False):
        print("Error(d_hill): key is not invertible")
        return ""

    
    

    ciphertext = ciphertext.lower()
    pos = utilities.get_positions(ciphertext, specs)
    text = utilities.clean_text(ciphertext, specs)
    x = 0
    
    if len(text) % 2 != 0:
        text += "q"
    
    while x < len(text):
        temp = matrix.new_matrix(2,1,0)
        for i in range(len(base)):
            if text[x] == base[i]:
                temp[0] = [i]
            if text[x+1] == base[i]:
                temp[1] = [i]
        
        
        c2 = matrix.mul(mat2, temp)
        
        c2 = matrix.matrix_mod(c2, 26)
        


        plaintext += base[c2[0][0]].lower()
        plaintext += base[c2[1][0]].lower()

        x += 2
    

    plaintext = utilities.insert_positions(plaintext,pos)

    plaintext = plaintext.rstrip("q")




        
    
    
    return plaintext


