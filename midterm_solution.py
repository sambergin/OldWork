"""
-----------------------------
CP460 (Fall 2020)
Name: Sam Bergin <------------------------- edit this
ID:   170670850 <------------------------- edit this
Midterm
-----------------------------
"""

import utilities
import math

"""---------------------------------
        Preparation Section
---------------------------------"""

#---------------------------------------
NAME = 'Samuel_Bergin'         #<------- edit this to be your name, should match your file name
ID = '170670850'            #<------- edit this with your student ID
CERTIFICATION = "I certify that I completed this midterm exam according to academic honesty guidelines. I attest that I did not use any external help, neither in person nor virtually. I understand that failing to abide by the academic honesty guidelines may lead to my failure in the course, in addition to other penalties according to the University policies"   #<------- edit this string with your honor pledge

dict_file = 'engmix.txt'
def comments():
    print('If you have anything that you think the instructor should know about, put it in this print statement')
    print("for task 3 it does not call classify in the test file, and the midterm description says not to edit midterm_test.py")
    print("so I did not test my file, i just kept it as is.")
    return

def references():
    print('References Used:')
    print('1- (Task 2) website: https://www.techcoil.com/blog/how-to-permutate-a-string-in-python-3/')
    #print('2- (Task 3) Code posted by David Smith at the solution sharing forum')
    #...
    return
#---------------------------------------

"""---------------------------------
Task 1: Cipher Detection
---------------------------------"""

# implement this function
def cipher_detector(file_list):
    
    ordered_file_list = [""] * len(file_list)
    
    chi =10000000
    shifti = 0
    for i in range(len(file_list)):
        text = utilities.file_to_text(file_list[i])
        key, ptext, chi2 = utilities.cryptanalysis_shift(text)
        if chi2 < chi:
            chi = chi2
            shifti = i
    ordered_file_list[3] = file_list[shifti]
    file_list.remove(file_list[shifti])
    
    chi =10000000
    eati = 0
    for i in range(len(file_list)):
        text = utilities.file_to_text(file_list[i])
        for j in range(0,4):
            ptext = utilities.d_eatbash(text, j)
            chi2 = utilities.chi_squared(ptext)
            
            if chi2 < chi and len(file_list[i]) < 25:
                chi = chi2
                eati = i
        
        
    
    ordered_file_list[5] = file_list[eati]
    file_list.remove(file_list[eati])

    
    polyi = 0
    
    for i in range(len(file_list)):
        c = 0
        c1 = 0
        text = utilities.file_to_text(file_list[i])
        freqN = utilities.get_freq(text, "num")
        freqC = utilities.get_freq(text, "alpha")
        
        for j in range(len(freqN)):
            c += freqN[j]
        for k in range(len(freqC)):
            c1 += freqC[k]
        
        if c > c1:
            polyi = i


    ordered_file_list[4] = file_list[polyi]
    file_list.remove(file_list[polyi])

    vini = 0
    iocnum = 0.065
    far = 0
    for i in range(len(file_list)):
        text = utilities.file_to_text(file_list[i])
        I = utilities.index_of_coin(text)
        t = abs(iocnum - I)
        
        if t > far:
            far = t
            vini = i
    
    ordered_file_list[1] = file_list[vini]
    file_list.remove(file_list[vini])



    subsi = 0
    fc = 0
    for i in range(len(file_list)):
        fc2 = 0
        text = utilities.file_to_text(file_list[i])
        freq = utilities.get_freq(text, ".:;?-,")
        frs = utilities.get_freq(text, " ")
        
        
        for j in range(len(freq)):
            if freq[j] > frs[0]:
                subsi = i
            
            

    ordered_file_list[0] = file_list[subsi]
    file_list.remove(file_list[subsi])

    

    if len(file_list) == 1:
        ordered_file_list[2] = file_list[0]

    

    
    return ordered_file_list

#Edit This function
def comments_q1():
    print('My method for detecting the ciphers is:')
    print("to find the shift cipher, i used the cryptanalysis function to find the lowest chi value and then removed that file from the list")
    print("to find the atbash cipher, i used the same idea as the shift except i used decrypt, then removed the file from the list")
    print("to find the polybius cipher, i checked to see which one consists of mostly numbers, then removed the file from the list")

    print("to find the vignere cipher, i noticed that it always had the lowest IOC value out of the remaining files")

    print("to find the substitution cipher, i found out which one had the white spaces replaced with another charachter")
    print("the myszkowski cipgher was the only one remaining")
    
    
    return

#Edit This Function (file numbers is necessary correct)
def classify():
    substitution_file = 'ciphertext1_Samuel_Bergin.txt' #<-------- hardcode name of file that contains your substitution cipher file
    vigenerex_file = 'ciphertext3_Samuel_Bergin.txt'    #<------- hardcode name of file that contains your Vigenerex file
    myszkowski_file = 'ciphertext2_Samuel_Bergin.txt'   #<-------- hardcode name of file that contains your Myszkowski cipher file
    return substitution_file, vigenerex_file, myszkowski_file

"""---------------------------------
Task 2: Myszkowski Cipher
---------------------------------"""
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

def cryptanalysis1_myszkwoski(ciphertext,args):
    key = ""
    plaintext = ""
    key_list = []

    klen = args[0]
    base = args[1]

    posskey = ""
    
        

    return key,plaintext,key_list

def cryptanalysis2_myszkowski(ciphertext,args):
    keyp = ""
    key = ''
    plaintext = ""
    text = ""
    alpha = utilities.get_base("lower")
    isp = False
    
    for i in range(len(alpha)):
        if isp == False:
            if alpha[i] != args[0] and alpha[i] != args[1]:

                perml = []
                keyp = args[0] + args[1] + args[1] + alpha[i]  
                utilities.build_permutation_list(keyp, "", perml)  
                
                for i in range(len(perml)):
                    if isp == False:
                        text = d_myszkowski(ciphertext, perml[i])
                        
                        isp = utilities.is_plaintext(text,'engmix.txt')
                        if isp == True:
                            key = perml[i]
                            plaintext = text
                    
    if isp == False:
        for i in range(len(alpha)):
            if alpha[i] != args[0] and alpha[i] != args[1]:
                perml = []
                keyp = args[0] + args[1] + alpha[i] + alpha[i]  
                utilities.build_permutation_list(keyp, "", perml)  
                
                for i in range(len(perml)):
                    if isp == False:
                        text = d_myszkowski(ciphertext, perml[i])
                        
                        isp = utilities.is_plaintext(text,'engmix.txt')
                        if isp == True:
                            key = perml[i]
                            plaintext = text
                        
                        
    if isp == False:
        for i in range(len(alpha)):
            if alpha[i] != args[0] and alpha[i] != args[1]:
                perml = []
                    
                keyp = args[0] + args[0] + args[1] + alpha[i]  
                utilities.build_permutation_list(keyp, "", perml)  
                
                for i in range(len(perml)):
                    if isp == False:
                        text = d_myszkowski(ciphertext, perml[i])
                        
                        isp = utilities.is_plaintext(text,'engmix.txt')
                        if isp == True:
                            key = perml[i]
                            plaintext = text
                        
        

    
    
    return key,plaintext

def comments_q2():
    print('My method for cryptanalysis of Myszkowski:')
    
    print('My brute-force uses 864 keys') #<------ change X
    print('find all permutations for the 3 cases: doube first initial, double last initial, double alpha')
    print('test with keys generated from permutations')
    return

"""---------------------------------
Task 3: Substitution Cipher
---------------------------------"""

def e_substitution(plaintext,key):
    ciphertext = ""
    base = utilities.get_sub_str()
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            for j in range(len(base)):
            
                if plaintext[i].lower() == base[j]:
                    if plaintext[i].isupper():
                        ciphertext += key[j].upper()
                    else:
                        ciphertext += key[j]
        else:
            if plaintext[i] in base:
                for j in range(len(base)):
                
                    if plaintext[i] == base[j]:
                        ciphertext += key[j]
            else:
                ciphertext += plaintext[i]
    
            
    

                
            
    return ciphertext

def d_substitution(ciphertext,key):
    plaintext = ""
    base = utilities.get_sub_str()
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            for j in range(len(key)):
            
                if ciphertext[i].lower() == key[j]:
                    if ciphertext[i].isupper():
                        plaintext += base[j].upper()
                    else:
                        plaintext += base[j]
        else:
            if ciphertext[i] in base:
                for j in range(len(base)):
                
                    if ciphertext[i] == key[j]:
                        plaintext += base[j]
            else:
                plaintext += ciphertext[i]
    


    return plaintext

#only change the key, do not change other lines
def cryptanalysis_substitution(ciphertext):
   
    key = 'dbsigwlahncfxoupjmztrqyvke, ;-?:.' #<----- hard-code key here
    plaintext = d_substitution(ciphertext,key)
    
    
    return key,plaintext

#do not change this function
def comments_q3():
    print('Comments:')
    filename = NAME + '_sub_log.txt'
    text = utilities.file_to_text(filename)
    print(text)
    return

"""---------------------------------
Task 4: Vigenerex Cipher
---------------------------------"""
def e_swapt(plaintext,key):
    ciphertext = ""
    text = ""
    pos = utilities.get_positions(plaintext, " \n\t")
    plaintext = utilities.clean_text(plaintext, " \n\t")
    blocks = utilities.text_to_blocks(plaintext, 2)
    for i in range(len(blocks)):
        blocks[i] = blocks[i][::-1]
        text += blocks[i]
    blocks2 = utilities.text_to_blocks(text, 4)
    text = ""
    for i in range(len(blocks2)):
        bl = list(blocks2[i])
        if len(bl) == 4:
            temp = bl[0]
            temp2 = bl[1]
            bl[0] = bl[2]
            bl[1] = bl[3]
            bl[2] = temp
            bl[3] = temp2
        blocks2[i] = "".join(bl)
        text += blocks2[i]
    blocks3 = utilities.text_to_blocks(text, 6)
    text = ""
    for i in range(len(blocks3)):
        bl = list(blocks3[i])
        if len(bl) == 6:
            temp = bl[0]
            temp2 = bl[1]
            temp3 = bl[2]
            bl[0] = bl[3]
            bl[1] = bl[4]
            bl[2] = bl[5]
            bl[3] = temp
            bl[4] = temp2
            bl[5] = temp3
        blocks3[i] = "".join(bl)
        text += blocks3[i]
    blocks4 = utilities.text_to_blocks(text, 8)
    text = ""
    for i in range(len(blocks4)):
        bl = list(blocks4[i])
        if len(bl) == 8:
            temp = bl[0]
            temp2 = bl[1]
            temp3 = bl[2]
            temp4 = bl[3]
            bl[0] = bl[4]
            bl[1] = bl[5]
            bl[2] = bl[6]
            bl[3] = bl[7]
            bl[4] = temp
            bl[5] = temp2
            bl[6] = temp3
            bl[7] = temp4
        blocks4[i] = "".join(bl)
        ciphertext += blocks4[i]
    ciphertext = utilities.insert_positions(ciphertext, pos)



    
    
    return ciphertext

def d_swapt(ciphertext,key):
    plaintext = ""
    text = ""
    pos = utilities.get_positions(ciphertext, " \n\t")
    ciphertext = utilities.clean_text(ciphertext, " \n\t")
    
    blocks4 = utilities.text_to_blocks(ciphertext, 8)
    
    for i in range(len(blocks4)):
        bl = list(blocks4[i])
        
        if len(bl) == 8:
            temp = bl[0]
            temp2 = bl[1]
            temp3 = bl[2]
            temp4 = bl[3]
            bl[0] = bl[4]
            bl[1] = bl[5]
            bl[2] = bl[6]
            bl[3] = bl[7]
            bl[4] = temp
            bl[5] = temp2
            bl[6] = temp3
            bl[7] = temp4
        blocks4[i] = "".join(bl)
        text += blocks4[i]
    blocks3 = utilities.text_to_blocks(text, 6)
    
    text = ""
    for i in range(len(blocks3)):
        bl = list(blocks3[i])
        if len(bl) == 6:
            temp = bl[0]
            temp2 = bl[1]
            temp3 = bl[2]
            bl[0] = bl[3]
            bl[1] = bl[4]
            bl[2] = bl[5]
            bl[3] = temp
            bl[4] = temp2
            bl[5] = temp3
        blocks3[i] = "".join(bl)
        text += blocks3[i]
    blocks2 = utilities.text_to_blocks(text, 4)
    
    text = ""
    for i in range(len(blocks2)):
        bl = list(blocks2[i])
        if len(bl) == 4:
            temp = bl[0]
            temp2 = bl[1]
            bl[0] = bl[2]
            bl[1] = bl[3]
            bl[2] = temp
            bl[3] = temp2
        blocks2[i] = "".join(bl)
        text += blocks2[i]

    blocks = utilities.text_to_blocks(text, 2)
    
    for i in range(len(blocks)):
        blocks[i] = blocks[i][::-1]
        
        plaintext += blocks[i]
    
    plaintext = utilities.insert_positions(plaintext, pos)
    

    return plaintext

def cryptanalysis_vigenerex(ciphertext):
    key = ""
    plaintext = ""
    return key,plaintext

def comments_q4():
    print('This is how I broke the vigenerex cipher:')
    print('Write your description inside print statements')
    return