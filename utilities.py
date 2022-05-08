"""
-----------------------------
CP460 (Fall 2020)
Name: <------------------------- edit this
ID:   <------------------------- edit this
Midterm Utilities
-----------------------------
"""

import math

PAD = 'q'
DICT_FILE = 'engmix.txt'

MAX_KEY_L = 17 # you can edit me
CIPHER_SHIFT_FACTOR = 26 # you can edit me

# only selected functions are given to you
# you may add functions to this file as needed

"""
----------------------------------------------------
Parameters:   No parameters
Return:       substitution_string (str)
Description:  Generates Base String for simple substitution cipher
---------------------------------------------------
"""
def get_sub_str():
    return 'abcdefghijklmnopqrstuvwxyz ,;-:?.'

"""
----------------------------------------------------
Parameters:   No parameters
Return:       No returns
Description:  Debugging tool for Substitution Cipher
---------------------------------------------------
"""
def debug_substitution(ciphertext, size = 200):
    base_str = get_sub_str()
    sub_str = ['-' for i in range(len(base_str))]
    
    positions = get_positions(ciphertext,'\n')
    ciphertext = clean_text(ciphertext,'\n')
    
    plaintext = ['-' for i in range(len(ciphertext))]
    print('Ciphertext:')
    print(ciphertext[:size])
    print()
    command = input('Debug Mode: Enter Command: ')
    description = input('Description: ')
    print()
    
    while command != 'end':
        sub_char = command[8].lower()
        base_char  = command[15].lower()
            
        if base_char in base_str:
            indx = base_str.index(base_char)
            sub_str[indx] = sub_char
        else:
            print('(Error): Base Character does not exist!\n')

        print('Base:',end='')
        for i in range(len(base_str)):
            print('{} '.format(base_str[i]),end='')
        print()
        print('Sub :',end='')
        for i in range(len(sub_str)):
            print('{} '.format(sub_str[i]),end='')
        print('\n')

        print('ciphertext:')
        print(ciphertext[:size])
        for i in range(len(plaintext)):
            if ciphertext[i].lower() == sub_char:
                plaintext[i] = base_char
        print('plaintext :')
        #print(plaintext[:size])
        print("".join(plaintext[:size]))
        print('\n_______________________________________\n')
        command = input('Enter Command: ')
        if command != 'end':
            description = input('Description: ')
        print()
    return

"""
----------------------------------------------------
Parameters:   base_type (str) 
Return:       result (str)
Description:  Return a base string containing a subset of ASCII charactes
              Defined base types:
              lower: lower case characters
              upper: upper case characters
              alpha: upper and lower case characters
              num: numerical characters
              lowernum: lower case and numerical characters
              uppernum: upper case and numerical characters
              alphanum: upper, lower and numerical characters
              nonalpha: all non alphabetical characters
              special: punctuations and special characters (no white space)
              all: upper, lower, numerical and special characters
---------------------------------------------------
"""
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

"""
----------------------------------------------------
Parameters:   filename (str)
Return:       contents (str)
Description:  Utility function to read contents of a file
              Can be used to read plaintext or ciphertext
---------------------------------------------------
"""
def file_to_text(filename):
    infile = open(filename,'r')
    contents = infile.read()
    infile.close()
    return contents

"""
----------------------------------------------------
Parameters:   text (str)
              filename (str)            
Return:       no returns
Description:  Utility function to write any given text to a file
              If file already exist, previous content will be erased
---------------------------------------------------
"""
def text_to_file(text, filename):
    outfile = open(filename,'w')
    outfile.write(text)
    outfile.close()
    return

"""
----------------------------------------------------
Parameters:   dict_file (str): filename
Return:       dict_list (list): 2D list
Description:  Reads a given dictionary file
              dictionary is assumed to be formatted: each word in a separate line
              Returns a list of lists, list 0 contains all words starting with 'a'
              list 1 all words starting with 'b' and so forth.
Asserts:      dict_file is a non-empty string
---------------------------------------------------
"""
def load_dictionary(dict_file):
    assert type(dict_file) == str and len(dict_file) > 0 ,'invalid dict_file'
    alphabet = get_base('lower')
    infile = open(dict_file, 'r',encoding=" ISO-8859-15") 
    dict_words = infile.readlines()
    dict_list = [[] for i in range(26)]
    for w in dict_words:
        word = w.strip('\n')
        dict_list[alphabet.index(word[0])]+=[word]
    infile.close()
    return dict_list



"""
----------------------------------------------------
Parameters:   None 
Return:       freq (list of floats) 
Description:  Return frequencies of characters in a given language
              Default language is English
---------------------------------------------------
"""
def get_language_freq(language='English'):
    if language == 'English':
        return [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
                0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    else:
        print('Error(get_language_freq): Unsupported language')
        return []

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
Parameters:     plaintext(str)
                key (int)
Return:         ciphertext (str)
Description:    Encryption using Atbash Cipher
                If key = 0, uses lower case base
                If key = 1, uses upper case base
                If key = 2: uses upper+lower case
                If key = 3: uses upper+lower+num
                If key = 4: uses upper+lower+num+special
Asserts:      plaintext is a string and key is an integer
---------------------------------------------------
"""
def e_eatbash(plaintext, key):
    ciphertext = ''
    key = key % 5
    if key == 0:
        base = get_base("lower")
        
    elif key == 1:
        base = get_base("upper")
        
    elif key == 2:
        base = get_base("alpha")
        
    elif key == 3:
        base = get_base("alphanum")
    elif key == 4:
        base = get_base("all")
        
    ciphbase = list(base)  
    
    ciphbase.reverse()
    
    
    for c in plaintext:
        i = 0
        if c in base:
            while c != base[i]:
                i += 1
            ciphertext += ciphbase[i]
        else:
            ciphertext += c
            
            
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (int)
Return:       plaintext (str)
Description:  Decryption using Atbash Cipher
              There is no key (None)
              Decryption can be achieved by encrypting ciphertext!!
Asserts:      ciphertext is a string and key is an integer
----------------------------------------------------
"""
def d_eatbash(ciphertext, key):
    plaintext = e_eatbash(ciphertext, key)
    return plaintext

"""
----------------------------------------------------
Parameters:   text (str)
Return:       word_list (list)
Description:  Reads a given text
              Returns a list of strings, each pertaining to a word in file
              Words are separated by a white space (space, tab or newline)
              Gets rid of all special characters at the start and at the end
Asserts:      text is a string
---------------------------------------------------
"""
def text_to_words(text):
    
    speclist = get_base("special")
    
    word_list = text.split()
    
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lstrip(speclist)
        word_list[i] = word_list[i].rstrip(speclist)
        
        
   
    
    return word_list

"""
----------------------------------------------------
Parameters:   text (str)
              dict_file (str)
Return:       match (int)
              mismatch (int)
Description:  Reads a given text, checks if each word appears in given dictionary
              Returns number of matches and number of mismatches.
              Words are compared in lowercase
              Uses load_dictionary and text_to_words functions
Asserts:      text and dict_file are both strings
---------------------------------------------------
"""
def analyze_text(text, dict_file):
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    match = 0
    mismatch = 0
    dic = load_dictionary(dict_file)
    
    word_list = text_to_words(text)
    
    
    for i in range(len(word_list)):
        j = 0
        m2 = match
        
        if word_list[i].isalpha():
            while word_list[i][0].lower() != alph[j]:
                j+=1
            
            for x in range(len(dic[j])):
                if word_list[i].lower() == dic[j][x]:
                    match += 1
            
            if match == m2:
                mismatch+=1
                
        else:
            mismatch+=1
        
        
                
    
    
    return match, mismatch

"""
----------------------------------------------------
Parameters:   text (str)
              dict_file (str): dictionary file
              threshold (float): number between 0 to 1
Return:       True/False
Description:  Check if a given file is a plaintext
              If #matches/#words >= threshold --> True
                  otherwise --> False
              If invalid threshold or not given, default is 0.9
              An empty string should return False
---------------------------------------------------
"""
def is_plaintext(text, dict_file, threshold=0.9):
    match, mismatch = analyze_text(text, dict_file)
    words = text.split()
    
    if threshold > 1 or threshold < 0:
        threshold = 0.9
    
    x = False
    if text != '':
        frac = (match / len(words))
        
        if frac >= threshold:
            x = True
        
        
        
        
    return x

"""
----------------------------------------------------
Parameters:   ciphertext(str)
Return:       key (str)
              plaintext (str)
Description:  Cryptanalysis of Extended Atbash Cipher
              Key is in the range of 0-4
              Uses default dictionary file and threshold of 0.8
Asserts:      ciphertext is a string
----------------------------------------------------
"""
def cryptanalysis_eatbash(ciphertext):
    text = d_eatbash(ciphertext, 0)
    text1 = d_eatbash(ciphertext, 1)
    text2 = d_eatbash(ciphertext, 2)
    text3 = d_eatbash(ciphertext, 3)
    text4 = d_eatbash(ciphertext, 4)
    dict_file = load_dictionary(DICT_FILE)
    
    if is_plaintext(text, dict_file, 0.8) == True:
        key = 0
        plaintext = text
    elif is_plaintext(text1, dict_file, 0.8) == True:
        key = 1
        plaintext = text1
    elif is_plaintext(text2, dict_file, 0.8) == True:
        key = 2
        plaintext = text2
    elif is_plaintext(text3, dict_file, 0.8) == True:
        key = 3
        plaintext = text3
    elif is_plaintext(text4, dict_file, 0.8) == True:
        key = 4
        plaintext = text4
    else: 
        plaintext = None
        key = None
        
    
    return key, plaintext

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
        base = get_base("lower")
        
        for i in range(len(base)):
            temp = 0
            for j in range(len(text)):
                if base[i] == text[j].lower():
                    temp += 1
            count_list.append(temp)
    elif base == ".:;?-," or base == " ":
        for i in range(len(base)):
            temp = 0
            for j in range(len(text)):
                if base[i] == text[j].lower():
                    temp += 1
            count_list.append(temp)


    else:
        base = get_base(base)
        
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
        E = get_language_freq(language)
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
        temp = shift_string(alpha, i, "l")
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
    base = get_base("nonalpha")
    base += " \n"
    
    pos = get_positions(plaintext, base)
    plaintext = clean_text(plaintext, base)
    

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
        ciphertext = insert_positions(ciphertext, pos)
        ciphertext = list(ciphertext)
        plaintext = "".join(plaintext)
        plaintext = insert_positions(plaintext, pos)
        
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
    

    base = get_base("nonalpha")
    base += " \n"
    pos = get_positions(ciphertext, base)
    ciphertext = clean_text(ciphertext, base)

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
        plaintext = insert_positions(plaintext, pos)
        plaintext = list(plaintext)
        ciphertext = insert_positions(ciphertext, pos)
        
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
            base = get_base("lower")
        else:
            base = key[1]

        
        
        base2 = shift_string(base, key[0], "l")
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
        print("Error(e_shift): invalid key")
        plaintext = ""
    else:
        if key[1] == None:
            base = get_base("lower")
        else:
            base = key[1]

        
        
        base2 = shift_string(base, key[0], "l")
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
        base_type = get_base(base_type)

    for i in range(1,25):
        text = d_shift(ciphertext, (i,base_type))
        temp = chi_squared(text)
        if temp < chi:
            chi = temp
            key = i
            plaintext = text




    
    
    
    return key,plaintext, chi

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
    base = get_base("nonalpha") + " \n\t"
    ciphertext = clean_text(ciphertext, base)

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
    base = get_base("nonalpha") + " \n\t"
    base2 = get_base("lower")
    pos = get_positions(ciphertext, base)
    ciphertext = clean_text(ciphertext, base)
    text = ciphertext.lower()
    dict_list = load_dictionary(DICT_FILE)
    isp = False

    key_ls = _cryptanalysis_vigenere_key_length(ciphertext)

    
    
    for i in range(len(key_ls)):
        blocks = text_to_blocks(ciphertext, key_ls[i])
        baskets = _blocks_to_baskets(blocks)

        for j in range(len(baskets)):
            k, _ = cryptanalysis_shift(baskets[j])
            key += base2[k]

        ciphertext = insert_positions(ciphertext, pos)
        
        plaintext = d_vigenere(ciphertext, key)
            
        ptc = is_plaintext(plaintext, dict_list)
        if ptc == True:
            return key,plaintext







    return _, _

"""
----------------------------------------------------
Parameters:   r: #rows (int)
              c: #columns (int)
              fill (str,int,double)
Return:       empty matrix (2D List)
Description:  Create an empty matrix of size r x c
              All elements initialized to fill
---------------------------------------------------
"""
def new_matrix(r,c,fill):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[fill] * c for i in range(r)]

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
                items separated by a tab
#               Assumes given parameter is a valid matrix
---------------------------------------------------
"""
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
---------------------------------------------------
"""
def matrix_to_string(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=matrix[i][j]
    return text

"""#----------------------------------------------------
# Parameters:   None
# Return:       polybius_square (string)
# Description:  Returns the following polybius square
#               as a sequential string:
#               [1] [2]  [3] [4] [5] [6] [7] [8]
#           [1]      !    "   #   $   %   &   '
#           [2]  (   )    *   +   '   -   .   /
#           [3]  0   1    2   3   4   5   6   7
#           [4]  8   9    :   ;   <   =   >   ?
#           [5]  @   A    B   C   D   E   F   G
#           [6]  H   I    J   K   L   M   N   O
#           [7]  P   Q    R   S   T   U   V   W
#           [8]  X   Y    Z   [   \   ]   ^   _
#---------------------------------------------------"""
def get_polybius_square():
    polybius_square = ""
    for i in range(32,96):
        polybius_square+=chr(i)
    return polybius_square

"""
----------------------------------------------------
Parameters:   start (str): an ASCII character
              size (int) number of rows & columns in square
Return:       square (str): A string representing a Polybius square
Description:  Creates a string that begins with 'start' character and 
              contains consecutive ASCII characters that are good to fill
              the given size of a polybius square
Asserts:      start is a single character string
              size is an integer >= 2
---------------------------------------------------
"""
def get_polybius_square(start,size):
    assert size >= 2
    assert len(start) == 1
    assert type(start) == str
    x = ord(start)
    
    
    polybius_square = ''
    
    if x < 32 or x > 126 or (x + size**2) > 126:
        return polybius_square
        
    else:
        for i in range(size**2):
            polybius_square += chr(x)
            x += 1
            
                
                
            
    
    return polybius_square

"""--------------------------------------------------------------
Parameters:   plaintext (str)
              key (tuple(str,int))
Return:       ciphertext (str)
Description:  Encryption using Polybius Square
Asserts:      plaintext is a string
              key is a tuple containing a single character and an integer
--------------------------------------------------------------
"""
def e_polybius(plaintext, key):
    assert type(plaintext) == str
    assert type(key) == tuple
    x = 0
    ciphertext = ''
    
    square = get_polybius_square(key[0], key[1])
    if square == "":
        print("error, empty string")
        return ciphertext
    
    else:
        mat = new_matrix(key[1], key[1], '')
        
        for i in range(key[1]):
            for j in range(key[1]):
                mat[i][j] = square[x]
                x += 1
        
        
        for i in range(len(plaintext)):
            if plaintext[i] in square:
                for j in range(key[1]):
                    for k in range(key[1]):
                        if plaintext[i] == mat[j][k]:
                            ciphertext += str(j+1)
                            ciphertext += str(k+1)
            else:
                ciphertext += plaintext[i]
                
    

    
    
    return ciphertext

"""
-------------------------------------------------------
Parameters:   ciphertext(str)
              key (tuple(str,int))
Return:       plaintext (str)
Description:  Decryption using Polybius Square
Asserts:      ciphertext is a string
              key is a tuple containing a single character and an integer
-------------------------------------------------------
"""
def d_polybius(ciphertext, key):
    assert type(ciphertext) == str
    assert type(key) == tuple
    x = 0
    c = 0
    plaintext = ''
    square = get_polybius_square(key[0], key[1])
    if square == "":
        print("Error, invalid square")
        return plaintext
    
    
    else:
        mat = new_matrix(key[1], key[1], '')
        
        for i in range(key[1]):
            for j in range(key[1]):
                mat[i][j] = square[x]
                x += 1
    
        while c < len(ciphertext):
            if ciphertext[c].isnumeric():
                
                
                i1 = int(ciphertext[c])
                i2 = int(ciphertext[c+1])
                try:
                        
                    plaintext += mat[i1-1][i2-1]
                    c += 2
                except IndexError:
                    c += 2
                    pass
                
                
                
            else:
                plaintext += ciphertext[c]
                c += 1
                
           
    
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              size (int)
Return:       key (str)
              plaintext (str)
Description:  Apply brute-force to break polybius cipher
              The size of the polybius square is given
              The square is always located between [' ', '~'] ASCII characters
              Use threshold of 0.93
Asserts:      ciphertext is a string
              size is an integer
---------------------------------------------------
"""
def cryptanalysis_polybius(ciphertext,size):
    key = None
    plaintext = ''
    dict_file = DICT_FILE
    for i in range(32,127):
        if i + (size*size) < 126:
            text = d_polybius(ciphertext, (chr(i), size))
            if is_plaintext(text, dict_file, 0.93) == True:
                key = (chr(i), size)
                plaintext = text
            
    return key,plaintext

def build_permutation_list(string, prefix='', permutation_list=[]):
    if len(string) == 0:
        if prefix not in permutation_list:
            permutation_list.append(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i + 1:]
            build_permutation_list(rem, prefix + string[i], permutation_list)



    


#debug_substitution(file_to_text('cipher23.txt')) # change file name