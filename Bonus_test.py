import utilities
import Bonus_solution

def task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Permutation Cipher Testing")
    print()
    
    print('-------------- Testing validate permutation key:')
    keys = ['5',['312','stream'],('53142','stream','53142'),('53142a','stream'),(53142,'stream'),
            ('53142','stream'),('53142','block'),('53142','cipher'),('5312','block'),('6471325','stream'),
            ('30142','block'),('2345','stream')]
    for key in keys:
        print('key = {} --> {}'.format(key, Bonus_solution._is_valid_key_permutation(key)))
    print()
    
    print('-------------- Testing Stream Mode:')
    plaintext = 'It takes 20 years to build a reputation and a few minutes of cyber-incident to ruin it.'
    keys = ['21','312','3124','35124','351642','7415263']
    for key in keys:
        k = (key,'stream')
        print('key = {}'.format(k))
        print('plaintext = {}'.format(plaintext))
        ciphertext = Bonus_solution.e_permutation(plaintext,k)
        print('ciphertext= {}'.format(ciphertext))
        plaintext2 = Bonus_solution.d_permutation(ciphertext,k)
        print('plaintext2= {}'.format(plaintext2))
        if plaintext == plaintext2:
            print('Validated')
        else:
            print('Validation Failed')
        print()

    print('-------------- Testing Block Mode:')
    for key in keys:
        k = (key,'block')
        print('key = {}'.format(k))
        print('plaintext = {}'.format(plaintext))
        ciphertext = Bonus_solution.e_permutation(plaintext,k)
        print('ciphertext= {}'.format(ciphertext))
        plaintext2 = Bonus_solution.d_permutation(ciphertext,k)
        print('plaintext2= {}'.format(plaintext2))
        if plaintext == plaintext2:
            print('Validated')
        else:
            print('Validation Failed')
        print()
        
    print('End of Task 1: Permutation Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: ADFGVX Cipher")
    print()
    
    print('-------------- Testing ADFGVX Square:')
    print('ADFGVX Square = ')
    square = Bonus_solution._adfgvx_square()
    for row in square:
        print(row)
    print()
    
    print('-------------- Testing Encryption/Decryption:')
    keys = ['Rose','flower','Sunflower','Marigold']
    i = 1
    for key in keys:
        file = 'plaintext'+str(i)+'.txt'
        plaintext = utilities.file_to_text(file)
        print('key =       {}'.format(key))
        print('plaintext = {}'.format(plaintext[:39]))
        ciphertext = Bonus_solution.e_adfgvx(plaintext,key)
        print('ciphertext= {}'.format(ciphertext[:39]))
        plaintext2 = Bonus_solution.d_adfgvx(ciphertext,key)
        print('plaintext2= {}'.format(plaintext2[:39]))
        if plaintext2 == plaintext:
            print('Validated')
        else:
            print('Validation failed')
        print()
        i += 1
    
    print('End of Task 2: ADFGVX Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Myszkowski Cipher")
    print()
    
    print('-------------- Testing Key order:')

    invalid_keys = [34, '', 'a', 'ab', 'aa', list('door'),'Dad', 'DOOR','Dad']
    valid_keys = ['dad','apple','good day','Vigenere Cipher']
    for key in invalid_keys+valid_keys:
        print('Key order for {} ='.format(key),end=' ')
        key_order = Bonus_solution._get_order_myszkowski(key)
        print(key_order)
    print()
    
    print('-------------- Testing Encryption/Decryption:')
    
    plaintexts = ['AMIDSUMMERNIGHTSDREAM', 'The Taming of the Shrew',
                  utilities.file_to_text('plaintext4.txt')]
    keys = ['swindon', 'deemed', 'One Time Pad']
    print('Testing encryption/decryption:')

    for i in range(len(plaintexts)):
        plaintext = plaintexts[i]
        key = keys[i]
        print('key = {}, key order = {}'.format(key,Bonus_solution._get_order_myszkowski(key)))
        print('plaintext = {}'.format(plaintext[:78]))
        ciphertext = Bonus_solution.e_myszkowski(plaintext,key)
        print('ciphertext= {}'.format(ciphertext[:78]))
        plaintext2 = Bonus_solution.d_myszkowski(ciphertext,key)
        print('plaintext2= {}'.format(plaintext2[:78]))
        if plaintext2 == plaintext:
            print('Validated')
        else:
            print('Validation failed')
        print()
        
    print('End of Task 3: Myszkowski Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

task1()
task2()
task3()