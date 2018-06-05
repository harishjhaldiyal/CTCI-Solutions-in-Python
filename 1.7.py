"""
this is a very classical problem that will enhance your mathematical skills while solving any problem. I would suggest you to solve this problem 
whenever you see this rather than just reading the solution. the main idea of solving this problem is to just swap the layers first outside and then 
swapping the inside layers. for example first I reserve the top layer and then in the place of top layer I put the left layer and in the place of left 
layer I put the bottom layer in the place of bottom layer I put right layer and in the place of right layer I put back the top layer that I reserved in the 
beginning; however in doing so we have to create an extra array for reserving the whole top layer and this is not very efficient in terms of space complexity; 
therefore rather than swapping the whole layers we would swap the individual cells in each layer - layer by layer moving inside so we are performing the 
same operation but now we are swapping the cells and therefore the space complexity will just be constant. please note Gayle's solution and read it very 
carefully, it is very very efficient and you have to modularize your code and make variables' names having sense

"""

def rotate(matrix):
    n = len(matrix)
    if ((n != len(matrix[0])) or (n == 0)):
        print("Invalid Input")
        return
    if (n == 1):
        return
 
    """    top = I[layer][layer+i]
            bottom = I[n-1-layer][n-1-layer-i]
            left = I[n-1-layer-i][layer]
            right = I[layer+i][n-1-layer]"""     
    for layer in range(int(n / 2)):
        for i in range(n - 2 * (layer) - 1):
            temp = matrix[layer][layer + i] #temp
            matrix[layer][layer + i] = matrix[n - 1 - layer - i][layer] #top->left
            matrix[n - 1 - layer - i][layer] = matrix[n - 1 - layer][n - 1 - layer - i] #left->bottom
            matrix[n - 1 - layer][n - 1 - layer - i] = matrix[layer + i][n - 1 - layer] #bottom->right
            matrix[layer + i][n - 1 - layer] = temp #right->temp
 
def initialize_matrix(size):
    counter = 0
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(counter)
            counter += 1
    return matrix
 
def print_matrix(matrix):
    for a in matrix:
        print (a)
    print ('')
    
    
    
    
"""
matrix = initialize_matrix(5)
print_matrix(matrix)
rotate(matrix)
print_matrix(matrix)
"""