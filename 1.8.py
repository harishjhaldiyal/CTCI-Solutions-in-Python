######## METHOD 1 - O(n.o of rows + n.o of cols) space#########


"""
the main idea of solving this problem is that we do not need to know the exact location of an element in the Matrix whose value is 0; in fact we just need 
to know that an element whose value is 0 in the matrix occurs in which row and which column so that we can just nullify that row and that column. we 
accomplish this by first having two boolean lists for row and column and whenever we see an element in the Matrix whose value is 0, we record it's row 
number and we flip the value of that row number in our boolean list from false to true; similarly we also record its column number and we flip the value 
of that column number in the column list from false to true and then at the end we traverse through those row boolean list and column boolean list and 
identify that which row number and column number contains an element which has zero value and we just nullify that row number and column number
"""


def input_matrix(M):
    rows = len(M)
    cols = len(M[0])
    if (rows == 0 and cols == 0):
        print ("Empty matrix")
    else:
        #process(M, rows, cols)
        process2(M, rows, cols)
        
def process(M, rows, cols):
    row_bool = [False]*rows
    col_bool = [False]*cols
    for list_index in range(len(M)):
        for e in range(len(M[list_index])):
            if (M[list_index][e]==0):
                row_bool[list_index] = True
                col_bool[e] = True
                
    for j in range(len(row_bool)):
        if row_bool[j]:
            nullifyRow(M, j)
    for k in range(len(col_bool)):
        if col_bool[k]:
            nullifyCol(M, k)
        
    print_matrix(M)
    
def nullifyRow(M, row_index):
    for i in range(len(M[row_index])):
        M[row_index][i] = 0
    
    
def nullifyCol(M, col_index):
    for i in range(len(M)):
        M[i][col_index] = 0


def print_matrix(M):
    for a in M:
        print(a)
        
        
        
######## METHOD 2 - O(1) space#########

"""
We can reduce the space to 0(1) by using the first row as a replacement for the row array and the first
column as a replacement for the column array. This works as follows:
1. Check if the first row and first column have any zeros, and set variables rowHasZero and
columnHasZero. (We'll nullify the first row and first column later, if necessary.)
2. Iterate through the rest of the matrix, setting matrix[ i] [ 0) and matrix [ 0) [ j] to zero whenever
there's a zero in matrix[i] [j ].
3. Iterate through rest of matrix, nullifying row i if there's a zero in matrix [ i] [ 0].
4. Iterate through rest of matrix, nullifying column j if there's a zero in matrix [ 0] [ j].
5. Nullify the first row and first column, if necessary (based on values from Step 1 ). 
"""

def process2(M,rows,cols):
    rowHasZero = False
    colHasZero = False
    for i in range(len(M[0])):
        if(M[0][i]==0):
            rowHasZero = True
            break
            
    for i in range(len(M)):
        if(M[i][0]==0):
            colHasZero = True
            break
            
    i = 1
    while (i<len(M)):
        j = 1
        while (j<len(M[0])):
            if (M[i][j] == 0):
                M[i][0] = 0
                M[0][j] = 0
            j+=1
        i+=1
                
    for i in range(len(M)):
        if(M[i][0]==0):
            nullifyRow(M,i)
            
    for i in range(len(M[0])):
        if(M[0][i]==0):
            nullifyCol(M,i)
            
    if (rowHasZero):
        nullifyRow(M,0)
        
    if (colHasZero):
        nullifyCol(M,0)
        
    print_matrix(M)