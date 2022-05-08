# This file could be changed locally for testing purposes only
# do not submit this file

import midterm_solution
import utilities

def get_info():
    first,last = midterm_solution.NAME.split('_')
    print('This is midterm solution of:')
    print('Name: {} {}'.format(first,last))
    print('ID: {}'.format(midterm_solution.ID))
    print()
    print(midterm_solution.CERTIFICATION)
    print()
    midterm_solution.comments()
    print()
    midterm_solution.references()
    return

def task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Cipher Detector Testing")
    print()
    
    cipher_names = ['Substitution','Vigenere','Myszkowski','Shift','Polybius','E-Atbash']
    print('-------------- Testing over sample files:')
    file_list = ['cipher'+str(i)+'.txt' for i in range(1,19)]
    for i in range(0,18,6):
        print('Analyzing: {}'.format(file_list[i:i+6]))
        cipher_types = midterm_solution.cipher_detector(file_list[i:i+6])
        for j in range(6):
            print('{} is {}'.format(cipher_types[j],cipher_names[j]))
        print()
    
    print('-------------- Testing over midterm files:')
    student_name = midterm_solution.NAME
    file_list2 = ['ciphertext' + str(i) + '_' + student_name + '.txt' for i in range(1,4)]
    file_list3 = [file_list2[0],file_list2[1],file_list2[2],'cipher18.txt','cipher12.txt','cipher11.txt']
    print('Analyzing {} files'.format(student_name))
    cipher_types = midterm_solution.cipher_detector(file_list3)
    for j in range(3):
        print('{:15s} is {}'.format(cipher_names[j],cipher_types[j]))
    print()
    
    print('-------------- Classify Files:')
    files = midterm_solution.classify()
    
    for j in range(len(files)):
        print('{:15s} is {}'.format(cipher_names[j],files[j]))
    print()
     
    print('-------------- Displaying Comments:')
    midterm_solution.comments_q1()
    print()
    
    print('End of Task 1: Cipher Detector Testing')
    print('{}'.format('-'*40))
    print()
    return

def task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: Myszkowski Cipher Testing")
    print()
    
    print('-------------- Testing Decryption:')
     
    ciphertexts = ['SIEIRDDMNHRMUGAAMTMES','Tmi thewqh ea ngf eSrqqqTohq',
                   'muoNnlr\noiqe Mhb ttOeo htVeqqe\ndienpAg\ncctuhnqc ol fqTsAohtMaeq']
    keys = ['swindon', 'deemed', 'shakespeare']
 
    for i in range(len(ciphertexts)):
        ciphertext = ciphertexts[i]
        key = keys[i]
        print('key = {}'.format(key))
        print(ciphertext)
        plaintext = midterm_solution.d_myszkowski(ciphertext,key)
        print(plaintext)
        print()
     
    print('-------------- Testing Cryptanalysis1:')
 
    plaintext = utilities.file_to_text('plain10.txt')
    cases = [[3,'eb'],[4,'tr'],[5,'kfu'],[6,'kou'],[7,'efotr']]
    cipher_indx = 19
    for i in range(len(cases)):
        args = cases[i]
        if i == 2:
            ciphertext = ''
        else:
            cipher_file = 'cipher'+str(cipher_indx)+'.txt'
            ciphertext = utilities.file_to_text(cipher_file)
            cipher_indx += 1
        key,plaintext2,key_list = midterm_solution.cryptanalysis1_myszkwoski(ciphertext,args)
        print('key list = {}'.format(key_list))
        print('found key = {}'.format(key))
        if plaintext2.strip('\n') == plaintext.strip('\n'):
            print('Validated')
        else:
            print('Validation Failed')
        print()
     
    cases = [[16,''],[1,'rtd'],[2,'omre'],[-1,'omre'],[0,'']]
    for args in cases:
        _,_,key_list = midterm_solution.cryptanalysis1_myszkwoski('',args)
        print('There are {} keys that satisfy {}'.format(len(key_list),args))
    print()

    print('-------------- Testing Cryptanalysis2:')
    _,_,myszkowski_file = midterm_solution.classify()
    print('Analyzing file: {}'.format(myszkowski_file))
    ciphertext = utilities.file_to_text(myszkowski_file)
    first,last = get_name()
    k1,k2 = get_myszkowski_args(first,last)
    key,plaintext2 = midterm_solution.cryptanalysis2_myszkowski(ciphertext,[k1,k2])
    print('Found key: {}'.format(key))
    print()
    
    print('-------------- Displaying Comments:')
    midterm_solution.comments_q2()
    print()
    
    print('End of Task 2: Myszkowski Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return
    
def task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Substitution Cipher Testing")
    print()
    
    print('-------------- Testing over sample file:')
    plaintext = utilities.file_to_text('plain23.txt')
    key = 'qkvbxrozmigeltjydcshuwanpf.: ;?-,'
    
    ciphertext = utilities.file_to_text('cipher23.txt')
    ciphertext2 = midterm_solution.e_substitution(plaintext,key)
    if ciphertext2 == ciphertext:
        print('E-Validated')
    else:
        print('E-Failed')
    plaintext2 = midterm_solution.d_substitution(ciphertext,key)
    if plaintext2 == plaintext:
        print('D-Validated')
    else:
        print('D-Failed')
 
    print('-------------- Testing cryptanalysis:')
    sub_file,_,_ = midterm_solution.classify()
    ciphertext = utilities.file_to_text(sub_file)
    key,plaintext = midterm_solution.cryptanalysis_substitution(ciphertext)
    print('key = {}'.format(key))
    print('plaintext:')
    print(plaintext[:300])
    print()
     
    print('-------------- Displaying Comments:')
    midterm_solution.comments_q3()
    print()
    
    print('End of Task 3: Substitution Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def task4():
    print('{}'.format('-'*40))
    print("Start of Task 4: Vigenerex Cipher Testing")
    print()
    
    print('-------------- Testing swapt cipher:')
    plaintexts = ['LOCALGUARDS', 'rulesofengagement','Swapt Cipher is a simple transposition scheme']
    for plaintext in plaintexts:
        print(plaintext)
        ciphertext = midterm_solution.e_swapt(plaintext,None)
        print(ciphertext)
        plaintext2 = midterm_solution.d_swapt(ciphertext,None)
        print(plaintext2)
        print()
    
    print('-------------- Testing cryptanalysis_vigenerex::')
    _,vigenerex_file,_ = midterm_solution.classify()
    print('Analyzing file: {}'.format(vigenerex_file))
    ciphertext = utilities.file_to_text(vigenerex_file)
    key,plaintext2 = midterm_solution.cryptanalysis_vigenerex(ciphertext)
    print('Found key: {}'.format(key))
    print()
    
    print('-------------- Displaying Comments:')
    midterm_solution.comments_q4()
    print()
    
    print('End of Task 4: Vignere Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def get_myszkowski_args(first,last):
    k1 = first[0].lower()
    i = 0
    while True:
        k2 = last[i].lower()
        i += 1
        if k2 != k1:
            break
    return k1,k2

def get_name():
    first,last = midterm_solution.NAME.split('_')
    return first,last

get_info()
task1()
task2()
task3()
task4()
