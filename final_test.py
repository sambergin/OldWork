import final
import utilities
import SDES
import copy
import task5

#----------------------------------------------------
# Test Q1: mathCipher
#---------------------------------------------------
def task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Mathx  Cipher Testing")
    print()

    base = utilities.get_base('lower')

    print('----- Part 1: validate mathx key:')
    keys = [['abc',[1,1,1]],('ab',[1,1,1]),('abc',[1,1,1.0]),(123,[1,1,1]),
            ('abc',(1,1,1)),('abc',[1,1]),('abc',[1,'1',1]), ('abc',[0,0,0]), 
            (base[:14],[6,4,2]), (base[:14],[9,2,3]),
            (base[:14],[11,7,1]),('abc',[1,1,1])]
    for key in keys:
        print('{:30s} = {}'.format(str(key),final.validate_mathx_key(key)))
    print()
    
    print('----- Part 2: encryption:')    
    plaintext = 'The quick brown fox jumps over the lazy dog'
    keys = [ (base,[5,9,11]), (base+ ' ',[43,5,17]), ('T'+base,[7,5,13]), (base,[12,1,12]), (base,[0,0,0])]
    for key in keys:
        print('key =       {}'.format(key))
        print('plaintext = {}'.format(plaintext))
        ciphertext = final.e_mathx(plaintext,key)
        print('ciphertext= {}'.format(ciphertext))
        print()
    
    print('----- Part 3: decryption:')    

    ciphertexts = ['Tlc myowu tpged fgh ryajs gbcp vlc xqnk zgi',
                   'Tqelzouxbltcrwnlir lyojvglrseclkqelfphdlarm',
                   'dwz njvat bmphq ypg ujrol pizm kwz scef Tpx',
                   'The quick brown fox jumps over the lazy dog',
                   'The quick brown fox jumps over the lazy dog']
    for i in range(len(keys)):
        print('key =       {}'.format(keys[i]))
        print('ciphertext= {}'.format(ciphertexts[i]))
        plaintext2 = final.d_mathx(ciphertexts[i],keys[i])
        print('plaintexts= {}'.format(plaintext2))
        print()
        
    print('----- Part 4: Classify mathx:')    
    keys = [(base,[2,1,2]), (base,[10,6,3]), (base,[6,3,2]), (base,[7,4,9]),
            (base,[17,1,43]), (base,[19,2,10]), (base,[1,1,1]), (base,[25,24,4]), 
            (base,[25,24,5]), (base[:14],[14,28,14]), (base[:15],[49,7,9]), (base[:15],[4,7,7]),
            (base[:17],[3,18,20]), (base[:23],[2,25,1]), (base+' ',[8,8,11]), (base+'?!#',[103,8,2])]
    for key in keys:
        print('{:46s} is {}'.format(str(key),final.classify_mathx(key)))
    print()
    
    print('----- Part 5: mathx Key Domain:')
    bases = [base[:3],base[:4],base[:5],base[:10], base[:13],base[:26]]
    for b in bases:
        result = final.get_mathx_keydomain(b)
        print('Percentage of valid keys in base ({}) = {:.2f}%'.format(b,result*100))
    print()
    
    print('----- Part 6: cryptanalysis mathx:')
    cipher_file = 'ciphertext1_'+final.NAME+'.txt'
    ciphertext = utilities.file_to_text(cipher_file)
    #key,plaintext = final.cryptanalysis_mathx(ciphertext)
    
    key = final.get_mathx_key()
    plaintext2 = final.d_mathx(ciphertext,key)
    print('key = {}'.format(key))
    print('plaintetx2:')
    print(plaintext2[:200])
    print()
    
    print('End of Task 1: Mathx Testing')
    print('{}'.format('-'*40))
    print()
    return

#----------------------------------------------------
# Test Q2: SDES
#---------------------------------------------------
def task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: SDES Testing")
    print()
    
    print('----- Part 1: Generic SDES:')
    SDES.set_SDES_value('encoding_type','B6')
    SDES.set_SDES_value('rounds','2')
    SDES.set_SDES_value('key_size','9')
    SDES.set_SDES_value('block_size','12')
     
    print('Testing e_SDES:')
    print('Empty plaintext: ',end='')
    SDES.e_SDES('','111000111','CFB')
    print()
    print('Invalid key: ',end='')
    SDES.e_SDES('sweet','11100','CFB')
    print()
    print('CFB mode: ',end='')
    SDES.e_SDES('sweet','111000111','CFB')
    print('\n')
 
    print('Testing d_SDES:')
    print('Empty plaintext: ',end='')
    SDES.d_SDES('','111000111','CFB')
    print()
    print('Invalid key: ',end='')
    SDES.d_SDES('sweet','11100','CFB')
    print()
    print('CFB mode: ',end='')
    SDES.d_SDES('sweet','111000111','CFB')
    print()
     
    print('Testing valid modes:')
    modes = ['ECB','CBC','OFB']
    plaintext = 'CP460'
    key = '111000111'
    for i in range(len(modes)):
        ciphertext = SDES.e_SDES(plaintext,key,modes[i])
        plaintext2 = SDES.d_SDES(ciphertext,key,modes[i])
        print('mode = {}: ciphertext = {:6s}  plaintext = {}'.format(modes[i],ciphertext,plaintext2))
    print()
     
    print('----- Part 2: LFSR:')
    print('Testing LFSR:')
    c = [[0,1,0,1],[0,0,1,1],[0,1,1,1,0]]
    IG = ['1011','1000','10001']
    bits = [7,16,16]
    for i in range(len(IG)):
        print('LFSR({},{},{}) = {}'.format(c[i],IG[i],bits[i],SDES.LFSR(c[i],IG[i],bits[i])))
     
    c = [[1],(1,0),[1,0,1],[1,0,1],[1,0,1],[1,0,1]]
    IG = ['101','101','10','123','101','101']
    bits = [9,8,8,9,0,'9']
    for i in range(len(IG)):
        SDES.LFSR(c[i],IG[i],bits[i])
    print()
     
    print('Testing get_IV:')
    SDES.set_SDES_value('key_size','9')
    SDES.set_SDES_value('block_size','12')
    print('key_size = 9,  block_size = 12, get_IV = {}'.format(SDES.get_IV()))
    SDES.set_SDES_value('block_size','16')
    print('key_size = 9,  block_size = 16, get_IV = {}'.format(SDES.get_IV()))
    SDES.set_SDES_value('key_size','10')
    print('key_size = 10, block_size = 16, get_IV = {}'.format(SDES.get_IV()))
    print()
     
    print('----- Part 3: CBC Mode')
    SDES.set_SDES_value('key_size','9')
    SDES.set_SDES_value('block_size','12')
    plaintext = 'CBC is an abbreviation of Cipher Block Chaining'
    key = '111000111'
    print('key        = {}'.format(key))
    print('plaintext  = {}'.format(plaintext))
    ciphertext = SDES.e_SDES(plaintext,key,'CBC')
    print('ciphertext = {}'.format(ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key,'CBC')
    print('ciphertext2= {}'.format(plaintext2,key,'CBC'))
    print()
     
    key = '011001011'
    SDES.set_SDES_value('rounds','3')
    print('key        = {}'.format(key))
    print('plaintext  = {}'.format(plaintext))
    ciphertext = SDES.e_SDES(plaintext,key,'CBC')
    print('ciphertext = {}'.format(ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key,'CBC')
    print('ciphertext2= {}'.format(plaintext2))
    print()
     
    print('----- Part 4: OFB Mode')
    SDES.set_SDES_value('rounds','2')
    plaintext = 'OFB stands for Output Feedback'
    key = '111000111'
    print('key        = {}'.format(key))
    print('plaintext  = {}'.format(plaintext))
    ciphertext = SDES.e_SDES(plaintext,key,'OFB')
    print('ciphertext = {}'.format(ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key,'OFB')
    print('ciphertext2= {}'.format(plaintext2))
    print()
     
    key = '011001010'
    plaintext = 'What is the difference between encryption and decryption in OFB?'
    SDES.set_SDES_value('rounds','3')
    print('key        = {}'.format(key))
    print('plaintext  = {}'.format(plaintext))
    ciphertext = SDES.e_SDES(plaintext,key,'OFB')
    print('ciphertext = {}'.format(ciphertext))
    plaintext2 = SDES.d_SDES(ciphertext,key,'OFB')
    print('ciphertext2= {}'.format(plaintext2))
    print()

    print('----- Part 5: SDES3 Cryptanalysis:')
    file = 'ciphertext2_'+final.NAME+'.txt'
    ciphertext = utilities.file_to_text(file)
    #key,plaintext = SDES.cryptanalysis_SDES3(ciphertext)
    key = SDES.get_SDES3_key()
    plaintext = utilities.file_to_text('plaintext2_'+final.NAME+'.txt')
    print('key = {}'.format(key))
    print('plaintext = {}'.format(plaintext[:200]))
    print()
    
    print('End of Task 2: SDES Testing')
    print('{}'.format('-'*40))
    print()
    return
    
#---------------------------------------
# Task 3: Public X
#---------------------------------------------------
def task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Public X Testing")
    print()
    
    print('----- Part 1: RSA Key:')
    attributes = ['p','q','m','n','e','d']
    key = final.get_RSA_key()
    for i in range(len(key)):
        print('{} = {}'.format(attributes[i],key[i])) 
    print()
        
    print('----- Part 2: LRM exponentiation:')
    b = [66, 5, 4, 1234567890]
    e = [13, 117, 60, 151515151515151515]
    m = [20, 19, 69, 190]
    for i in range(len(b)):
        result = final.LRM(b[i],e[i],m[i])
        print('({}**{}) mod {} = {}'.format(b[i],e[i],m[i],result))
    print()
         
    print('----- Part 3: BA Encoding:')
    texts = ['A','a',' ','AA','BA','??','zZ', 'ABC de']
    for i in range(len(texts)):
        result = final.encode_BA(texts[i])
        print('encode_BA({}) = {}'.format(texts[i],result))
    print()
    
    cases = [[0,1],[0,3],[26,1],[27,4],[96,8],[7954,2],[4921,3],[87573246,6]]
    for case in cases:
        result = final.decode_BA(case[0],case[1])
        print('decode_BA({},{}) = {}'.format(case[0],case[1],result))
    print()     
        
    print('----- Part 4: Encryption:')
    print("""Case 1: Use instructor's public key:""")
    print()
    plaintext = "Your theory is crazy, but it's not crazy enough to be true"
    m = 351346324368343
    e = 32452869
    key = (m,e) # this is the instructor's public key
    ciphertext = final.e_RSA(plaintext,key)
    print('Encryption using instructor public key:')
    print('plaintext: ',plaintext)
    print('key: ',key)
    print('ciphertext: ',ciphertext)
    print()
    
    _,_,m,_,e,d = final.get_RSA_key()
    key = (m,e) # this is your public key
    ciphertext = final.e_RSA(plaintext,key)
    print("""Case 2: Use your public key:""")
    print('plaintext: ',plaintext)
    print('key: ',key)
    print('ciphertext: ',ciphertext)
    print()
    
    print('----- Part 5: Decryption:')
    print("Decrypt using instructor's public key:")
    ciphertext = 'AUCBbBj^CP"c~PmHA JA#IjDA#~1,u`EEYK"-9pvCG6_\\r|#E2(c\\u#eC&Pm^ve^'
    plaintext2 = final.d_RSA(ciphertext,(351346324368343,32452869))
    print(plaintext2)
    print()
    
    print('The instructor sent me the following question:')
    file = 'ciphertext3_'+final.NAME+'.txt'
    ciphertext = utilities.file_to_text(file)[:-1]
    question = final.d_RSA(ciphertext,(int(m),int(d)))
    print(question)
    print()
    
    print('----- Part 6: Digital Signatures:')
    file = 'message_'+final.NAME+'.txt'
    message = utilities.file_to_text(file)[:-1]
    name,message = final.verify_RSA(message,'public_keys.txt')
    print('Retrieved message:')
    print(message)
    print('Signed by:')
    print(name)
    print()

    print('End of Task 3: Public X Testing')
    print('{}'.format('-'*40))
    print()
    return

#----------------------------------------------------
# Test Task 4: transposex
#---------------------------------------------------
def task4():
    print('{}'.format('-'*40))
    print("Start of Task 4: Transposex Cipher Testing")
    print()

    print('----- Part 1: En-padding')
    list1 = [['a','b'],['c']]
    list2 = [['a','b','c'],['d','e'],['f','g']]
    list3 = [['a','b'],['c'],['d'],['e']]
    list4 = [['a','b'],['c','d'],['e','f'],['g','h']]

    inputs = [list1,list2,list3,list4,copy.deepcopy(list3),[],'a', ['a','b','c'], [['a','b'],3,['c','d']]]
    padding = ['q','x','#']
    for i in range(len(inputs)):
        print('List before padding: {}'.format(inputs[i]))
        if i < 3:
            output_list = final._en_pad_transposex(inputs[i],padding[i])
            print('list after padding: {}'.format(output_list))
        elif i >= 3 and i < 6:
            output_list = final._en_pad_transposex(inputs[i])
            print('list after padding: {}'.format(output_list))
        else:
            output_list = final._en_pad_transposex(inputs[i])
        print()
        
    print('----- Part 2: Encryption')
    plaintext1 = 'THISFINALEXAMISEASY'
    plaintext2 = 'Passwords are like underwear: don’t let people see it, change it very often, and you shouldn’t share it with strangers.'
    plaintexts = [plaintext1,plaintext2,plaintext1]
    keys = [4,14,-1]
    for i in range(len(keys)):
        print('key = {}'.format(keys[i]))
        print('plaintext = {}'.format(plaintexts[i]))
        ciphertext = final.e_transposex(plaintexts[i],keys[i])
        print('ciphertext= {}'.format(ciphertext))
        print()
    
    print('----- Part 3: Decryption')
    ciphertext1 = 'TFLMAHIEISINXSYSAAEQ'
    ciphertext2 = 'Pl:oho raai pafsenskdlnth gseoegeoiew n enutrou’s ,l srntei dw.dd etaniQsel  n’tQ reivdthQawtte   Qre ,ryssQeap yohtQ rec uarQ'
    ciphertexts = [ciphertext1,ciphertext2,ciphertext1]
    for i in range(len(keys)):
        print('key = {}'.format(keys[i]))
        print('ciphertext = {}'.format(ciphertexts[i]))
        plaintext2 = final.d_transposex(ciphertexts[i],keys[i])
        print('plaintext= {}'.format(plaintext2))
        print()
        
    print('----- Part 4: analyze plaintext:')
    plaintexts = [12,['abc'],'','X', 'Pi','len','Crypto','Cryptography','CP460: Cryptography',
                  'AAA','BBBB','CCCCC','DDDDDD','EEEEEEE', 'FFFFFFFF',
                  'A to Q', 'Generate base from A to Q', 
                  'The 17th character of the alphabet is Q',
                  'In CP460, the default padding character is Q',
                  'QQQQ','QQQAQ', 'QQBQQQQ','QQQCQQQQ', 'QDQQQQQQQ','QQQQQEQQQQQQ',
                  'FAQ','FAQQ','FAQQQ','FAQQQQ','FAQQQQQQQQQQ']
    for i in range(len(plaintexts)):
        plaintext = plaintexts[i]
        keydomain = final.analyze_transposex(plaintext)
        print('#keys = {:2d} for plaintext = {}'.format(keydomain,plaintext))
    print()
    
    print('----- Part 5: analyze ciphertext:')
    ciphertexts = [12, ['abc'], '', 'p', 'pi', 'QQQ',
                   'Cytlg sCytgah n rpaayirpooyi rporpyadCytnlss','CppPlt4io6eg0dr: a CpArhpyy', 'Ticr hse 2i m10sDb32 ee,0',  
                   'fxaQ', 'TFLMAHIEISINXSYSAAEQ','Cytaar onnyigdapsr lt aCyoCprslrhyioyypsgp tQ','CA gPpCr4pra6lyp0iph:ety doQ',
                   'Qs cu b eaaAursDeeiT','Qnssud ie acuSr eteAsa D cbTakas',
                   'SQbtuaaescuikec   aaAnrDdeT  s', 'Ti shzvie em wrpQaylus e',
                   'Aiu l tes Py pQr ieuiQsceou iureaae', 'Tu sshiQ iizuwms eap ouslQne e',
                   'Qsu iwza so ns iSmtpalcekQ', 'Qnudeeude  tAoD TP riiso reixttyeQ','Qiuniez  Coinp hAefrfQ',
                   'Tehxea mP rwiaosr idtiyf fQiuceuulet Q','Sau  tnefladsuec  nakQa rsurtn eeoQ',
                   'Cu esotSnQmeccQprieQ','Ptsroeitonnoifaennelt gsQrT sQaePiQ','D i noiFcItngosn sir cReteaieQanndsQlsdepQ',
                   'Qiiautcniasdzl    QSoFutnoea rucDeekinssgs Q','Qs rQsdu Piu iearteSeuniyutsedo euQ',
                   'CUQiooREuefnI adeaTol slIfipssQ friQ','Tstvlvlh ieieyiQt t ssuaQaAi atutnsiniaiaQ',
                   'Atv t  ieQaQQt utuuaaaieatnlvunidiee','Tdh eQ uQaulainttaittiavtei vQeu eaune',
                   'Dniissgi icStsca hlAe nmFaeolQryQesQ','K uSaLxQli QinOQ']
    
    for i in range(len(ciphertexts)):
        ciphertext = ciphertexts[i]
        keys = final.analyze2_transposex(ciphertext)
        print('ciphertext = {}'.format(ciphertext))
        print('keys = {}'.format(keys))
        print()

    print('End of Task 4: Transposex Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

#----------------------------------------------------
# Test Task 5: doublex
#---------------------------------------------------
def task5():
    print('{}'.format('-'*40))
    print("Start of Task 5: Doublex Cipher Testing")
    print()

    for i in range(1,4):
        print('----- Part {}: ciphertext5{}:'.format(i,i))
        file = 'ciphertext5' + str(i) + '_' + final.NAME + '.txt'
        ciphertext = utilities.file_to_text(file)
        print('file = {}'.format(file))
        print('ciphertext = ')
        print(ciphertext[:200])
        if i == 1:
            cipher1,key1,cipher2,key2,plaintext = final.cryptanalysis_51(ciphertext)
        if i == 2:
            cipher1,key1,cipher2,key2,plaintext = final.cryptanalysis_52(ciphertext)
        if i == 3:
            cipher1,key1,cipher2,key2,plaintext = final.cryptanalysis_53(ciphertext)

        print('Cipher1 = {}, key = {}'.format(cipher1,key1))
        print('Cipher2 = {}, key = {}'.format(cipher2,key2))
        print('plaintext = ')
        print(plaintext[:200])
        print()
    
    print('End of Task 5: Doublex Testing')
    print('{}'.format('-'*40))
    print()
    return

task1()
#task2()
#task3()
#task4()
#task5()