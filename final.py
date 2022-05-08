import utilities
import mod
import math
import matrix
import task5
import string

#---------------------------------------
NAME = 'Samuel_Bergin'    #<------- edit this to be your name, should match your file name
ID = '170670850'            #<------- edit this with your student ID
CERTIFICATION = """I certify that I completed this final exam according to academic honesty guidelines. I attest
that I did not use any external help, neither in person nor virtually. I understand that failing
to abide by the academic integrity guidelines may lead to my failure in the course, in
addition to other penalties according to the University policies."""   #<------- edit this string with your honor pledge

def comments():
    print('If you have anything that you think the instructor should know about, put it in this print statement')
    return

def references():
    print('References Used:')
    print('1- https://en.wikipedia.org/wiki/Modular_exponentiation')
    print('2- https://www.youtube.com/watch?v=23J2doHaJ6U&start=80s')
    print("3- http://pi.math.cornell.edu/~mec/Summer2008/lundell/lecture3.html")
    #...
    return

#----------------------------------
#       Task 1: Math Cipher       #
#----------------------------------

def validate_mathx_key(key):
    if type(key) != tuple:
        return False
    if type(key[0]) != str:
        return False
    if type(key[1]) != list:
        return False
    for i in key[1]:
        if type(i) != int:
            return False
    
    if len(key[1]) != 3:
        return False

    if len(key[0]) < 3:
        return False

    
    a = key[1][0]
    b = key[1][1]
    c = key[1][2]

    if mod.has_mul_inv((a+b-c), len(key[0])) == False:
        return False
    

    

    
    return True
    
def e_mathx(plaintext, key):
    ciphertext = ""
    if validate_mathx_key(key) == False:
        print("Error(e_mathx): invalid key")
        return ""
    
    a = key[1][0]
    b = key[1][1]
    c = key[1][2]
    p1 = a + b - c
    p2 = (b*c) - a
    base = key[0]
    baselist = []
    for i in base:
        baselist.append(i)

    x = 0
    for i in plaintext:
        
        
        if baselist.__contains__(i):
            for j in range(len(baselist)):
                if baselist[j] == i:
                    x = j
            ciphertext += baselist[((p1 * x) + p2) % len(base)]
        
        else:
            ciphertext += i

    

    
    
    return ciphertext

def d_mathx(ciphertext,key):
    plaintext = ""
    if validate_mathx_key(key) == False:
        print("Error(d_mathx): invalid key")
        return ""
    a = key[1][0]
    b = key[1][1]
    c = key[1][2]
    p1 = a + b - c
    p2 = (b*c) - a
    base = key[0]
    baselist = []
    p1inv = mod.mul_inv(p1, len(base))

    for i in base:
        baselist.append(i)
    
    x = 0
    for i in ciphertext:
        if baselist.__contains__(i):
            for j in range(len(baselist)):
                if baselist[j] == i:
                    x = j
            plaintext += baselist[((x-p2) * p1inv) % len(baselist)]
        
        else:
            plaintext += i
    


    return plaintext

def classify_mathx(key):
    if validate_mathx_key(key) == False:
        return "Invalid"
    
    a = key[1][0]
    b = key[1][1]
    c = key[1][2]
    
    if a == c:
        return "No Encipherment"
    
    if ((a+b-c) + ((b*c)-a) == 1):
        return "No Encipherment"
    
    if a+b-c == 1:
        return "No Encipherment"

    if (b*c)-a == 0:
        return "Decimation"
    
    if ((b*c)-a) % len(key[0]) == 0:
        return "Decimation"
    
    else:
        return "Affine"
    
    
    
    
    

    return ''

def get_mathx_keydomain(base):
    percentage = 0.0
    k = len(base)
    vkeys = 0
    tkeys = 0

    for x in range(k):
        print(x)
        for y in range(k):
            for z in range(k):
                
                s = classify_mathx((base, [x,y,z]))
                
                
                if s != "Invalid" and s != "No Encipherment":
                    vkeys += 1
                   
                    
                tkeys += 1
    
    percentage = vkeys/tkeys
   
    

    return percentage
               
def cryptanalysis_mathx(ciphertext):
    plaintext= ""
    key = ()
    base = utilities.get_base("lower") + utilities.get_base("special")
    dict_list = utilities.load_dictionary("engmix.txt")
    for i in range(3, len(base)):
        for j in range(4):
            for k in range(6):
                for l in range(11):
                    val = validate_mathx_key((base[:i], [j,k,l]))
                    if val == True:

                        plaintext = d_mathx(ciphertext, (base[:i], [j,k,l]))
                        isp = utilities.is_plaintext(plaintext, dict_list)
                        if isp == True:
                            
                            return (base[:i], [j,k,l]), plaintext
    return key,plaintext

def get_mathx_key():
    
    return ('abcdefghijklmnopqrstuvwxyz!"#$%&\'', [1, 0, 2]) # <---- edit this

#----------------------------------
#            Task 2: SDES         #
#----------------------------------

# see SDES.py

#----------------------------------
# Task 3: Public Key Cryptography #
#----------------------------------

def get_RSA_key():
    p = 20008801
    q = 22263049
    m = 445456917094249 
    n = 445456874822400
    e = 32452999 
    d = 156504640479799 
    return [p,q,m,n,e,d]



def LRM(b,e,m):
    x = 1
    
    if e & 1:
        x = b
    
    while e != 0:
        
        e = e // 2**1
        b = (b * b) % m
        
        if e & 1: 
            x = (x * b) % m

    
    return x
 
def encode_BA(text):
    num = 1
    
    base = utilities.get_base("BA")
    basel = []
    for i in base:
        basel.append(i)
    if len(text) == 1:
        if basel.__contains__(text):
            for i in range(len(basel)):
                if text == basel[i]:
                    num = i
    elif text == "BA":
        num = 96
    
    else:
        l = []
        for c in text:
            if basel.__contains__(c):
                for i in range(len(basel)):
                    if c == basel[i]:
                        l.append(i)
        
        num = 0
        l.reverse()
        for i in range(len(l)):
            num += l[i] * 96**i
        

    
        
        


    return num
 
def decode_BA(num,block_size):
    text = ""
    base = utilities.get_base("BA")

    if num == 96:
        if block_size > 2:
            while len(text) < block_size -2:
                text += "A"
        text += "BA"
    
    elif num >= 0 and num <=95:
        if block_size > 1:
            while len(text) < block_size - 1:
                text += "A"
        text += base[num]

    else:
        nt = ""
        q = num
        l = []
        
        while q != 0:
            l.append(q % 96)
            q = q // 96
        
        l.reverse()

        for i in l:
            nt += base[i]
        if len(nt) < block_size:
            while len(text) < block_size -len(nt):
                text += "A"
            
            text += nt
        else:
            text = nt




    return text
 
def e_RSA(plaintext,key):
    ciphertext = ""
    blocks = utilities.text_to_blocks(plaintext, 6, 1, "q")
    blocks2 = []
    blocks3 = []
    blocks4 = []
    
    for i in blocks:
        blocks2.append(encode_BA(i))
    for i in blocks2:
        blocks3.append(LRM(i, key[1], key[0]))
    for i in blocks3:
        blocks4.append(decode_BA(i, 8))
    
    for i in blocks4:
        ciphertext += i



        
    return ciphertext
 
def d_RSA(ciphertext,key):
    plaintext = ""
    blocks = utilities.text_to_blocks(ciphertext, 8)
    blocks2 = []
    blocks3 = []
    blocks4 = []

    for i in blocks:
        blocks2.append(encode_BA(i))
    for i in blocks2:
        blocks3.append(LRM(i, key[1], key[0]))
    for i in blocks3:
        blocks4.append(decode_BA(i,6))
    for i in blocks4:
        plaintext += i

    plaintext = plaintext.rstrip("Q")
    
    return plaintext
     
def verify_RSA(message,public_key_file):
    ptext = ""
    message2 = ""
    name = ""
    people = []
    f = open(public_key_file, "r")
    dic_list = utilities.load_dictionary("engmix.txt")

    for line in f:
        line = line.split(" ")
        
        people.append(line)

    for p in people:
        
        ptext = d_RSA(message, (int(p[1]), int(p[2])))
        isp = utilities.is_plaintext(ptext,dic_list, 0.7)
        if isp == True:
            name = p[0]
            message2 = ptext
            break
    
    if name == "":
        name = "Unknown"

    return name,message2

#----------------------------------
# Task 4: TransposeX #
#----------------------------------
def _en_pad_transposex(input_list,pad=utilities.PAD):
   
    if len(input_list) == 0 or type(input_list) != list or type(input_list[0]) != list:
        print("Error(enpad): invalid input")
        return []
    for i in input_list:
        if type(i) != list:
            print("Error(enpad): invalid input")
            return []

    output_list = input_list

    leng = len(output_list[0])

    for i in output_list:
        if len(i) < leng:
            while len(i) != leng:
                i.append(pad)
    
    return output_list

def e_transposex(plaintext,key):
    ciphertext = ""
    main = []

    if type(key) != int or key < 0:
        print("Error(e_transposex): invalid key")
        return ""
    i = 0
    
    while i < len(plaintext):
        temp = []
        for j in range(key):
            if i < len(plaintext):
                temp.append(plaintext[i])
                i += 1
        
        main.append(temp)
    
    main = _en_pad_transposex(main)
    
    main = utilities.transpose(main)
    

    for i in main:
        for j in i:
            ciphertext += j


    
    
    
    return ciphertext

def d_transposex(ciphertext,key):
    plaintext = ""
   
    rows = key
    cols = math.ceil(len(ciphertext)/key)
    main = matrix.new_matrix(rows,cols,0)

    if type(key) != int or key < 0:
        print("Error(d_transposex): invalid key")
        return ""
    i = 0
    
    
    for x in range(rows):
        for y in range(cols):
            if i < len(ciphertext):
                main[x][y] = ciphertext[i]

                i += 1
        
        
    
    
    
    main = utilities.transpose(main)
   
    
    
    for i in main:
        for j in i:
            plaintext += j


    plaintext = plaintext.rstrip("Q")
    
    return plaintext


 
def analyze_transposex(plaintext):
    if type(plaintext) != str:
        return -1
    if len(plaintext) == 0:
        return 0

    keydomain = 0
    i = 0
    flag = 0
    
    same = plaintext[0]
    for i in range(len(plaintext)):
        if plaintext[i] != same:
            flag = 1
    
    if plaintext[len(plaintext)-1] == "Q" and flag == 1:
        for i in range(2,len(plaintext)):
            if len(plaintext) % i == 0:
                keydomain += 1


    elif flag == 0 and plaintext[len(plaintext)-1] == "Q":
        return 0
    
    elif flag == 0:
        for i in range(2,len(plaintext)):
            if len(plaintext) % i != 0:
                keydomain += 1


    else:
        for i in range(2,len(plaintext)):
            keydomain += 1
    return keydomain

def analyze2_transposex(ciphertext):
    keys = []
    if type(ciphertext) != str:
        print("Error(analyze2):invalid ciphertext")
        return []
    if len(ciphertext) <= 2:
        return []
    qc = 0
    for i in range(2,len(ciphertext)):
        if ciphertext[i] == "Q":
            qc += 1
    if qc == 1:
        if ciphertext[len(ciphertext)-1] == "Q":
            for i in range(2,len(ciphertext)-1):
                if len(ciphertext)-1 % i != 0:
                    keys.append(i)
        else:
            for i in range(2,len(ciphertext)):
                if len(ciphertext) % i == 0:
                    keys.append(i)
    elif qc == 2:
        if ciphertext[len(ciphertext)-1] == "Q" and ciphertext[len(ciphertext)-2] == "Q":
            for i in range(2,len(ciphertext)-2):
                if len(ciphertext)-2 % i !=0:
                    keys.append(i)
        elif ciphertext[len(ciphertext)-1] == "Q":
            for i in range(2,len(ciphertext)-1):
                if len(ciphertext)-1 % i != 0:
                    keys.append(i)

        else:
            for i in range(2,len(ciphertext)):
                if len(ciphertext) % i == 0:
                    keys.append(i)
    elif qc == 3:
        if ciphertext[len(ciphertext)-1] == "Q" and ciphertext[len(ciphertext)-2] == "Q" and ciphertext[len(ciphertext)-3] == "Q":
            for i in range(2,len(ciphertext)-3):
                if len(ciphertext)-3 % i !=0:
                    keys.append(i)
        elif ciphertext[len(ciphertext)-2] == "Q" and ciphertext[len(ciphertext)-2] == "Q":
            for i in range(2,len(ciphertext)-2):
                if len(ciphertext)-2 % i != 0:
                    keys.append(i)
        elif ciphertext[len(ciphertext)-1] == "Q":
            for i in range(2,len(ciphertext)-1):
                if len(ciphertext)-1 % i != 0:
                    keys.append(i)
        else:
            for i in range(2,len(ciphertext)):
                if len(ciphertext) % i == 0:
                    keys.append(i)
    else:
        for i in range(2,len(ciphertext)):
                
                keys.append(i)



        
    return keys

#----------------------------------
#        Task 5: Doublex          #
#----------------------------------
# cipher names are: Atbash, Decimation, Rotation, Polybius, Columnar, Hill

def cryptanalysis_51(ciphertext):
    cipher1 = ""
    cipher2 = ""
    key1 = ""
    key2 = ""
    plaintext = ""
    text = ""

    
    return cipher1,key1,cipher2,key2,plaintext

def cryptanalysis_52(ciphertext):
    cipher1 = ""
    cipher2 = ""
    key1 = ""
    key2 = ""
    plaintext = ""
    return cipher1,key1,cipher2,key2,plaintext

def cryptanalysis_53(ciphertext):
    cipher1 = ""
    cipher2 = ""
    key1 = ""
    key2 = ""
    plaintext = ""
    return cipher1,key1,cipher2,key2,plaintext
