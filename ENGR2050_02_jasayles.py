# ENGR2050_02_jasayles.py
# Ethan Sayles
# Feb 02, 2017

#Function to return a specific row of a given matrix.
def Row_Grab(matrix,row):             #row is the non-programming understanding of row
    return matrix[row-1]

#Funtion to return a specific column of a given matrix.
def Column_Grab(matrix,column):              #column is the non-programming understanding of column
    col = []                                 #List to hold the given column of matrix
    for x in matrix:
        col.append(x[column-1])
    return col

#Funtion to return the forwards diagonal of a given matrix.
def Diagonal(matrix):  
    D_matrix=[]                              #Matrix to hold the diagonal of matrix
    if len(matrix) != len(matrix[0]):        #Check if matrix is square
        return None
    else:
        for x in range(len(matrix)):
            D_matrix.append(matrix[x][x])
        return D_matrix

#Funtion to return the backwards diagonal of a given matrix.
def R_Diagonal(matrix):
    RD_matrix=[]                              #Matrix to hold the reverse diagonal of matrix     
    if len(matrix) != len(matrix[0]):         #Check if matrix is square
        return None
    else:
        for x in range(len(matrix)):
            RD_matrix.append(matrix[x][-x-1])
        return RD_matrix

#Funtion to return the transpose of a given matrix.
def Transpose(matrix): 
    T_matrix = []                             #Matrix to hold the transpose of matrix
    for x in range(1,len(matrix)+1):          #Make the columns of matrix be the rows of T_matrix                   
        T_matrix.append(Column_Grab(matrix,x))
    return T_matrix

#Conditional to check for test cases
if __name__ == '__main__':
   Matrix = [[1,-2,-1,2],[5,11,3,0],[7,2,1,5],[8,7,-2,1]]
   print (Row_Grab(Matrix,2))
   print (Column_Grab(Matrix,2))
   print (Diagonal(Matrix))
   print (R_Diagonal(Matrix))
   print (Transpose(Matrix))
