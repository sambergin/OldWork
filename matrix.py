"""
-----------------------------
CP460 (Fall 2020)
Name: sam bergin<------------------------- edit this
ID:   170670850<------------------------- edit this
Assignment 4 (matrix Library)
-----------------------------
"""
import math
import string
import mod

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid vector
#               A valid vector is a list in which all elements are integers
#               An empty list is a valid vector
# Errors:       None
#-----------------------------------------------------------
def is_vector(A):
    
    if type(A) == list and len(A) == 0:
        
        return True
    
    elif type(A) != list:
        
        return False
    
    else:
        
        
        for i in A:
            if type(i) != int:
                
                return False
            
        return True    
        
        
        
    return 

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid matrix
#               A matrix is a list in which all elements are valid vectors of equal size
#               Any valid vector is also a valid matrix
# Errors:       None
#-----------------------------------------------------------
def is_matrix(A):
    
    if type(A) == list and len(A) == 0:
        return True
    elif type(A) != list:
       
        return False
    elif len(A) == 1 and is_vector(A) == False:
        return False
    

    else:
        
        if is_vector(A) == True:
            return True
        
        if type(A[0]) == list:

            l = len(A[0])
            
            for i in A:
                
                if (is_vector(i) == False):
                    return False
                
                if len(i) != l:
                   
                    return False
                    
            return True
        if type(A[0]) == int:
            for i in A:
                if type(i) != int:
                    return False
            return True  
   

        
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       None
# Description:  Prints a given matrix, each row on a separate line
# Errors:       If A not a matrix --> print 'Error (print_matrix): Invalid input'
#-----------------------------------------------------------
def print_matrix(A):
    if is_matrix(A) == False:
        print("Error (print_matrix): Invalid input")
        return ""
    else:
        if len(A) != 0 and type(A[0]) != list:
            print(A)
        elif len(A) == 0:
            print(A)
        else:

            for i in A:
                print(i)
            
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of rows (int)
# Description:  Returns number of rows in a given matrix
# Examples:     [5,3,2] --> 1
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 3
# Errors:       If A not a matrix -->
#                   return 'Error(get_r): invalid input'
#-----------------------------------------------------------
def get_r(A):
    if is_matrix(A) == False:
        return "Error (get_r): Invalid input"
    
    else:
        if len(A) == 0:
            return 0
        elif type(A[0]) != list:
            return 1
        else:
            c = 0
            for i in A:
                c += 1
            return c
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of columns (int)
# Description:  Returns number of columns in a given matrix
# Examples:     [5,3,2] --> 3
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 2
# Errors:       If A not a matrix -->
#                   return 'Error(get_c): invalid input'
#-----------------------------------------------------------
def get_c(A):
    if is_matrix(A) == False:
        return "Error (get_c): Invalid input"
    else:
        
        if len(A) == 0:
            return 0
        elif type(A[0]) != list:
            return len(A)
        else:
            return len(A[0])
    
    return 

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       [number of rows (int), number of columns(int)]
# Description:  Returns number size of matrix [rxc]
# Examples:     [5,3,2] --> [1,3]
#               [] --> [0,0]
#               [[1,2],[3,4],[5,6]] --> [3,2]
# Errors:       If A not a matrix -->
#                   return 'Error(get_size): invalid input'
#-----------------------------------------------------------
def get_size(A):
    if is_matrix(A) == False:
        return "Error (get_size): Invalid input"

    else:
        return [get_r(A), get_c(A)]
    return

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid square matrix
# Examples:     [] --> True
#               [10] --> True
#               [[1,2],[3,4]] --> True
#               [[1,2],[3,4],[5,6]] --> False
# Errors:       None
#-----------------------------------------------------------
def is_square(A):
    x = get_size(A)
    if x[0] == x[1]:
        return True
    else:
        return False
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
# Return:       row (list)
# Description:  Returns the ith row of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1,2],[3,4]],0) --> [1,2]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error(get_row): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error(get_row): invalid row number'
#-----------------------------------------------------------
def get_row(A,i):
    if len(A) == 0 or is_matrix(A) == False:
        return 'Error(get_row): invalid input matrix'
    elif i >= len(A):
        return 'Error(get_row): invalid row number'
    else:
        return A[i]
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               j (column number)
# Return:       column (list)
# Description:  Returns the jth column of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1], [2]],0) --> [[1], [2]]
#               ([[1,2],[3,4]],1) --> [2,4]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_column): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error(get_column): invalid column number'
#-----------------------------------------------------------
def get_column(A,j):
    if len(A) == 0 or is_matrix(A) == False:
        return 'Error (get_column): invalid input matrix'
    elif j >= len(A[0]):
        return 'Error(get_column): invalid column number'
    else:
        c = []
        for i in A:
            c.append([i[j]])
        return c
            
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
#               j (column number)
# Return:       element
# Description:  Returns element (i,j) of the given matrix
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error(get_element): invalid input matrix'
#               If i or j is outside matrix range -->
#                   return 'Error(get_element): invalid element position'
#-----------------------------------------------------------
def get_element(A,i,j):
    if len(A) == 0 or is_matrix(A) == False:
        return 'Error (get_element): invalid input matrix'
    elif i >= len(A) or j >= len(A[0]):
        return 'Error(get_element): invalid element position'

    else:
        return A[i][j]
    return

#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               num (int)
# Return:       matrix
# Description:  Create an empty matrix of size r x c
#               All elements are initialized to integer num
# Error:        r and c should be positive integers
#               (except the following which is valid 0x0 --> [])
#                   return 'Error(new_matrix): invalid size'
#               pad should be an integer
#                   return 'Error(new_matrix): invalid num'
#-----------------------------------------------------------
def new_matrix(r,c,num):
    if type(num) != int:
        return 'Error(new_matrix): invalid num'
    elif type(r) != int or type(c) != int:
        return 'Error(new_matrix): invalid size'
    elif (r == 0 and c == 0):
        return []
    elif r <=0 or c <= 0:
        return 'Error(new_matrix): invalid size'

    else:
        if r == 1:
            l = []
            for i in range(c):
                l.append(num)
            return l
        else:

            return [[num] * c for i in range(r)]
    return

#-----------------------------------------------------------
# Parameters:   size (int)
# Return:       square matrix (identity matrix)
# Description:  returns the identity matrix of size: [size x size]
# Examples:     0 --> Error
#               1 --> [1]
#               2 --> [[1,0],[0,1]]
# Errors        size should be a positive integer
#                   return 'Error(get_I): invalid size'
#-----------------------------------------------------------
def get_I(size):
    if size <= 0:
        return 'Error(get_I): invalid size'

    else:
        mat = new_matrix(size,size,0)
        k = 0
        
        if len(mat) == 1:
            mat[0] += 1
        
        else:
            for i in mat:
                i[k] += 1
                k += 1
        
        return mat
    
    return

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid identity matrix
#-----------------------------------------------------------
def is_identity(A):
    if is_matrix(A) == False:
        return False
    if is_square(A) == False:
        return False
    else:
        if len(A) == 1:
            if A[0] != 1:
                return False
            return True
        else:
            k = 0
            for i in A:
                for j in range(len(A)):
                    if i[j] == 1 and j != k:
                        return False
                if i[k] != 1:
                    return False
                k += 1
            return True

    return

#-----------------------------------------------------------
# Parameters:   c (int)
#               A (matrix)
# Return:       a new matrix which is the result of cA
# Description:  Performs scalar multiplication of constant c with matrix A
# Errors:       if A is empty or not a valid matrix or c is not an integer:
#                   return 'Error(scalar_mul): invalid input'
#-----------------------------------------------------------
def scalar_mul(c,A):
    if len(A) == 0 or is_matrix(A) == False or type(c) != int:
        return 'Error(scalar_mul): invalid input'
    
    

    if len(A) == 1 and type(A[0]) != list:
        mat[0] += A[0] * c
    
    elif type(A[0]) != list:
        mat = new_matrix(1, len(A), 0)
        for i in range(len(A)):
            mat[i] = A[i] * c
            
    else:
        mat = new_matrix(len(A), len(A[0]), 0)
        for i in range(len(mat)):
            for j in range(len(mat)):
                mat[i][j] += A[i][j] * c
            
    
    return mat
    return 

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               B (matrix)
# Return:       a new matrix which is the result of AxB
# Description:  Performs cross multiplication of matrix A and matrix B
# Errors:       if either A or B or both is empty matrix nor not a valid matrix
#                   return 'Error(mul): invalid input'
#               if size mismatch:
#                   return 'Error(mul): size mismatch'
#-----------------------------------------------------------
def mul(A,B):
    if len(A) == 0 or len(B) == 0 or is_matrix(B) == False or is_matrix(A) == False:
        return 'Error(mul): invalid input'
    if is_vector(A) or is_vector(B):

        if len(A) != len(B):
            return 'Error(mul): size mismatch'
    else:

        if len(A) != len(B[0]) and len(A[0]) != len(B):

            return 'Error(mul): size mismatch'
    
    if type(A[0]) == int and type(B[0]) == list and len(B[0]) > 1:
        mat = []
        for x in range(len(A)):
            for i in range(len(B[0])):
                for j in range(len(B)):
                    mat.append(A[x]*B[j][i])
        return mat
    
    if type(A[0]) == int and type(B[0]) == list and len(B[0]) == 1:
        mat = []
        n = 0
        for x in range(len(A)):
            n += A[x] * B[x][0]
        mat.append(n)
        return mat
    
    if type(A[0]) == list and type(B[0]) == list and len(A[0]) < len(B[0]):
        mat = new_matrix(len(A), len(A[0]), 0)
        for i in range(len(A)):
            for j in range(len(A[0])):
                for k in range(len(B)):
                    mat[i][j] += (A[i][j] * B[k][j])
        return mat
    
                
    
    if type(A[0]) == list and type(B[0]) == list:
        mat = new_matrix(len(A), len(B[0]), 0)
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    mat[i][j] += (A[i][k] * B[k][j])
        
        return mat
    
    if type(A[0]) == int and type(B[0]) == int and len(A) == 1 and len(B) == 1:
        mat = []
        mat.append(A[0] * B[0])
        return mat
    
    
    




    
    return

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       A` (matrix)
# Description:  Returns matrix A such that each element is the 
#               residue value in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(matrix_mod): invalid input'
#               if m is not a positive integer:
#                   return 'Error(matrix_mod): invalid mod'
#-----------------------------------------------------------
def matrix_mod(A,m):
    if len(A) == 0 or is_matrix(A) == False:
        return 'Error(matrix_mod): invalid input'
    if type(m) != int or m <= 0:
        return 'Error(matrix_mod): invalid mod'
    if type(A[0]) == int:
        mat = []
        for i in range(len(A)):
            mat.append(A[i] % m)
        return mat
    if type(A[0]) == list:
        mat = new_matrix(len(A), len(A[0]), 0)
        for i in range(len(A)):
            for j in range(len(A[0])):
                mat[i][j] += (A[i][j] % m)
        return mat

    return

#-----------------------------------------------------------
# Parameters:   A (matrix)
# Return:       determinant of matrix A (int)
# Description:  Returns the determinant of a 2x2 matrix
# Errors:       if A is empty matrix nor not a valid square matrix
#                   return 'Error(det): invalid input'
#               if A is square matrix of size other than 2x2
#                   return 'Error(det): Unsupported matrix size'
#-----------------------------------------------------------
def det(A):
    if len(A) == 0 or is_square(A) == False:
        return 'Error(det): invalid input'
    if len(A) != 2 or len(A[0]) != 2:
        return 'Error(det): Unsupported matrix size'
    else:
        d = 0
        d += (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
        return d
    return

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       a new matrix which is the inverse of A mode m
# Description:  Returns the inverse of a 2x2 matrix in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(inverse): invalid input'
#               if A is not a square matrix or a matrix of 2x2 with no inverse:
#                   return 'Error(inverse): matrix is not invertible'
#               if A is a square matrix of size other than 2x2
#                   return 'Error(inverse): Unsupported matrix size'
#               if m is not a positive integer:
#                   return 'Error(inverse): invalid mod'
#-----------------------------------------------------------
def inverse(A,m):
    if len(A) == 0 or is_matrix(A) == False:
        return 'Error(inverse): invalid input'
    if len(A) != 2:
        return 'Error(inverse): Unsupported matrix size'
    if type(m) != int or m <= 0:
        return 'Error(inverse): invalid mod'
    else:
        A2 = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
        d = det(A2)
        if mod.has_mul_inv(d,m) == False:
            return 'Error(inverse): matrix is not invertible'
        
        d2 = mod.mul_inv(d, m)

        M = scalar_mul(d2, A2)

        M2 = matrix_mod(M, m)

        return M2
        
        

        

    return