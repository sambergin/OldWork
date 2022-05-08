"""
-----------------------------
CP460 (Fall 2020)
Name: sam bergin<------------------------- edit this
ID:   170670850<------------------------- edit this
Assignment 4 (mod Library)
-----------------------------
"""

import math
import string

#-----------------------------------------------------------
# Parameters:   mod (int)
# Return:       r_list (list)
# Description:  Returns list of numbers in the given mod
#               which are residues of all other numbers
# Example:      residue_list(5) --> [0,1,2,3,4]
# Errors:       If mode is not a positive integer:
#                   return 'Error(residue_list): Invalid mod'
#-----------------------------------------------------------
def residue_list(mod):
    
    if (type(mod) != int) or mod <= 0:
        r_list = "Error(residue_list): Invalid mod"
    else:
        r_list = []
        for i in range(mod):
            r_list.append(i)
    
    return r_list

#-----------------------------------------------------------
# Parameters:   num (int)
#               mod (int)
# Return:       residue (int)
# Description:  Returns the smallest positive integer that is
#               congruent to num mod m
# Example:      residue 16 mod 5 --> 1
# Errors:       mod has to be positive integer
#                   return 'Error(residue): Invalid mod'
#               num should be integer
#                   return 'Error(residue): Invalid num'
#-----------------------------------------------------------
def residue(num,mod):
    
    if type(mod) != int or mod <= 0:
        result = "Error(residue): Invalid mod"
    elif type(num) != int or num <= 0:
        result = 'Error(residue): Invalid num'
    else:
        result = num % mod

    return result

#-----------------------------------------------------------
# Parameters:   a (int)
#               b (int)
#               m (int)
# Return:       True/False
# Description:  Returns True if a is congruent b mod m
#               return False otherwise
# Example:      is_congruent(22,33,11) --> True
#               is_congruent(7,9,3) --> False
# Errors:       if mod is not a positive integer
#                   return 'Error(is_congruent): Invalid mod'
#               a and b should be integer
#                   return 'Error(is_congruent): Invalid input num'
#-----------------------------------------------------------
def is_congruent(a,b,m):
    if type(m) != int or m <= 0:
        result = 'Error(is_congruent): Invalid mod'
    elif type(a) != int  or type(b) != int:
        result = 'Error(is_congruent): Invalid input num'
    else:
        if a % m == b % m:
            result = True
        else:
            result = False
    return result

#-----------------------------------------------------------
# Parameters:   a (int)
#               b (int)
#               m (int)
# Return:       result (integer)
# Description:  Returns (a + b) mod m
#               result is an integer in residue_list mod m
# Example:      11 + 3 mod 5 = 4
# Errors:       If a or b is not an integer
#                   return 'Error(add): Invalid input num'
#               m should be positive integer
#                   return 'Error(add): Invalid mod'
#-----------------------------------------------------------
def add(a,b,m):
    if type(a) != int or type(b) != int:
        result = 'Error(add): Invalid input num'
    elif type(m) != int or m <= 0:
        result = 'Error(add): Invalid mod'
    else:
        result = (a + b) % m
    return result

#-----------------------------------------------------------
# Parameters:   a (int)
#               b (int)
#               m (int)
# Return:       result (int)
# Description:  Returns (a - b) mod m
#               result is an integer in residue_list mod m
# Example:      sub(11,2,5) = 4
# Errors:       a and b should be integers
#                   return 'Error(sub): Invalid input num'
#               m should be positive integer
#                   return 'Error(sub): Invalid mod'
#-----------------------------------------------------------
def sub(a,b,m):
    if type(a) != int or type(b) != int:
        result = 'Error(sub): Invalid input num'
    elif type(m) != int or m <= 0:
        result = 'Error(sub): Invalid mod'
    else:
        result = (a - b) % m
    return result

#-----------------------------------------------------------
# Parameters:   a (int)
#               m (int)
# Return:       result (int)
# Description:  Returns additive inverse of a mod m
#               result is an integer in residue_list mod m
# Example:      additive inverse of 3 mod 5 is 2
# Errors:       if a or b is not an integer
#                   return 'Error(add_inv): Invalid input num'
#               if m is not a positive integer
#                   return 'Error(add_inv): Invalid mod'
#-----------------------------------------------------------
def add_inv(a,m):
    if type(m) != int or m <= 0:
        result = 'Error(add_inv): Invalid mod'
    elif type(a) != int:
        result = 'Error(add_inv): Invalid input num'
    
    else:
        result = 0
        rlist = residue_list(m)
        for i in range(m):
            if (a + rlist[i]) % m == 0:
                result = rlist[i]

        
        

                
                
            
            



    return result

#-----------------------------------------------------------
# Parameters:   m (int)
# Return:       table (2D List)
# Description:  Returns addition table mod m
#               element [r][c] represent r+c mod m
# Example:      add_table(2) --> [[0,1],[1,0]]
# Errors:       if m is not a positive integer
#                   return 'Error(add_table): Invalid mod'
#-----------------------------------------------------------
def add_table(m):
    if type(m) != int or m <= 0:
        table = 'Error(add_table): Invalid mod'
    else:
        table = [["" for i in range(m)] for j in range(m)]
        
        for i in range(m):
            for j in range(m):
                table[i][j] = (i + j) % m
        
        
    return table

#-----------------------------------------------------------
# Parameters:   m (int)
# Return:       table (2D List)
# Description:  Returns subtraction table mod m
#               element [r][c] represent r-c mod m
# Example:      sub_table(3) --> [[[0,2,1],[1,0,2],[2,1,0]]
# Errors:       if m is not a positive integer
#                   return 'Error(sub_table): Invalid mod'
#-----------------------------------------------------------
def sub_table(m):
    if type(m) != int or m <= 0:
        table = 'Error(sub_table): Invalid mod'
    else:
        table = [["" for i in range(m)] for j in range(m)]
        
        for i in range(m):
            
            for j in range(m):
                table[i][j] = (i - j) % m
        
        
    return table

#-----------------------------------------------------------
# Parameters:   m (int)
# Return:       table (2D List)
# Description:  Returns additive Inverse table mode m
#               Top row is num, bottom row is additive inverse
# Example:      add_inv_table(5) --> [[0,1,2,3,4],[0,4,3,2,1]]
# Errors:       if m is not a positive integer
#                   return 'Error(add_inv_table): Invalid mod'
#-----------------------------------------------------------
def add_inv_table(m):
    if type(m) != int or m <= 0:
        table = "Error(add_inv_table): Invalid mod"
    else:
        table = []
        r1 = []
        r2 = []
        for i in range(m):
            r1.append(i)
        table.append(r1)

        for i in range(m):
            r2.append(add_inv(r1[i],m))
        
        table.append(r2)

    return table

#-----------------------------------------------------------
# Parameters:   a (int)
#               b (int)
#               m (int)
# Return:       result (int)
# Description:  Returns (a * b) mod m
#               result is an integer in residue_list mod m
# Example:      mul(11,2,5) = 2
# Errors:       a and b should be integers
#                   return 'Error(mul): Invalid input num'
#               m should be positive integer
#                   return 'Error(mul): Invalid mod'
#-----------------------------------------------------------
def mul(a,b,m):
    if type(a) != int or type(b) != int:
        result = 'Error(mul): Invalid input num'
    elif type(m) != int or m <= 0:
        result = 'Error(mul): Invalid mod'
    else:
        result = (a * b) % m
    return result

    

#-----------------------------------------------------------
# Parameters:   m (int)
# Return:       table (2D List)
# Description:  Returns multiplication table mod m
#               element [r][c] represent r*c mod m
# Example:      mul table for mod 4 -->
#                       [0, 0, 0, 0]
#                       [0, 1, 2, 3]
#                       [0, 2, 0, 2]
#                       [0, 3, 2, 1]
# Errors:       if m is not a positive integer
#                   return 'Error(mul_table): Invalid mod'
#-----------------------------------------------------------
def mul_table(m):
    if type(m) != int or m <= 0:
        table = 'Error(mul_table): Invalid mod'
    else:
        table = [["" for i in range(m)] for j in range(m)]
        
        for i in range(m):
            
            for j in range(m):
                table[i][j] = (i * j) % m
        
        
    
    return table

#-----------------------------------------------------------
# Parameters:   n (an integer)
# Return:       True/False
# Description:  Returns True if n is a prime
#               False otherwise
#               (Note: Search online for an efficient implementation)
#     taken from https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
# Errors        None
#-----------------------------------------------------------
def is_prime(n):
    
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    
    if (n % 2 == 0 or n % 3 == 0): 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        
        i = i + 6
  
    return True         
    

#-----------------------------------------------------------
# Parameters:   a (int)
#               b (int)
# Return:       gcd of a and b (int)
# Description:  Returns greatest common divider using standard
#               Euclidean Algorithm
#               Implementation can be recursive or iterative
# Errors:       If a or b is not a non-zero integer: 
#                   return 'Error(gcd): Invalid input num'
#-----------------------------------------------------------
def gcd(a,b):
    flag = 0
    if b <0:
        flag = 1
    if type(a) != int or type(b) != int or a == 0 or b == 0:
        return 'Error(gcd): Invalid input num'
    
    else:

        while b != 0:
            (a, b) = (b, a % b)
        
        if flag == 1:
            return -a
        
    return a

#-----------------------------------------------------------
# Parameters:   a (int)
#               b (int)
# Return:       True/False
# Description:  Checks if two numbers are relatively prime
#               which is when gcd(a,b) equals 1
# Errors:       if a or b is not an integer
#                   return 'Error(is_relatively_prime): Invalid input num'
#-----------------------------------------------------------
def is_relatively_prime(a,b):
    if type(a) != int or type(b) != int:
        res = 'Error(is_relatively_prime): Invalid input num'
    else:
        res = False
        if gcd(a,b) == 1:
            res = True
    return res

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               m (a positive integer)
# Return:       True/False
# Description:  Checks if number 'a' has a multiplicative inverse
#               in mod m. Returns True if such number exist
#               Returns False otherwise
# Errors:       if a is not an integer
#                   return 'Error(has_mul_inv)" Invalid input num'
#               if m is not a positive integer
#                   return 'Error(has_mul_inv): Invalid mod'
#-----------------------------------------------------------
def has_mul_inv(a,m):
    if type(a) != int:
        res = 'Error(has_mul_inv)" Invalid input num'
    elif type(m) != int or m < 1:
        res = 'Error(has_mul_inv): Invalid mod'
    else:
        res = False
        for i in range(m):
            if ((i * a) % m == 1):
                res = True

    
    return res

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               b (an integer)
# Return:       result (list): [gcd(a,b) , s , t]
# Description:  Uses Extended Euclidean Algorithm to find
#               gcd of (a,b) and 's' and 't' such that
#               as + bt = gcd(a,b) , i.e. Bezout's Identity
# Errors:       if a or b equals to 0:
#                   return 'Error(eea): Invalid input num'
#-----------------------------------------------------------
def eea(a,b):
    flag = 0
    if b < 0:
        flag = 1
    if a == 0 or b == 0:
        return  'Error(eea): Invalid input num'
    
    
    
    else:
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q = b // a
            r = b%a
            b = a
            a = r
            u,v = v, u-q*v
            x,y = y, x-q*y
        
        if b < 0:
            return [-b, x, -u]
        if flag == 1:

            return [b, x, -u]
        
        return [b,x,u]
        
    return 

#-----------------------------------------------------------
# Parameters:   a (an integer)
#               m (positive integer)
# Return:       mul_v (int or 'NA')
# Description:  Computes multiplicative inverse of 'a' mod m
#               If such number does not exist, the function
#               return 'NA'
# Errors:       if 'a' is not an integer:
#                   return 'Error(mul_inv)" Invalid input num'
#               if m is not a positive integer
#                   return 'Error(mul_inv): Invalid mod
#-----------------------------------------------------------
def mul_inv(a,m):
    if type(a) != int:
        return 'Error(mul_inv)" Invalid input num'
    elif type(m) != int or m < 1:
        return 'Error(mul_inv): Invalid mod'
    else:
        
        for i in range(m):
            if ((i * a) % m == 1):
                return i
        return "NA"

    
    return

#-----------------------------------------------------------
# Parameters:   m (int)
# Return:       table (2D list)
# Description:  Returns multiplicative Inverse table mode m
#               Top row is num, bottom row is multiplicative inverse
# Example:      Multiplicative Inverse table mod 5 -->
#                   [[0,1,2,3,4],['NA',1,3,2,4]]
# Errors:       if m is not a positive integer
#                   return 'Error(mul_inv_table): Invalid mod'
#-----------------------------------------------------------
def mul_inv_table(m):
    if type(m) != int or m <= 0:
        table = "Error(mul_inv_table): Invalid mod"
    else:
        table = []
        r1 = []
        r2 = []
        for i in range(m):
            r1.append(i)
        table.append(r1)

        for i in range(m):
            r2.append(mul_inv(r1[i],m))
        
        table.append(r2)

    return table