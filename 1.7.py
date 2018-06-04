def func1(I):
    row = len(I)
    col = len(I[0])
    if((row!=col) or (row==0)):
        print("Invalid Input")
        return False
    if(row==1 and col==1):
        return I
    else:
        return func2(I,row)
        
def func2(I,n):
    for layer in range(int(n/2)):
        for i in range(n-2*(layer)):
            
            """top = I[layer][layer+i]
            bottom = I[n-1-layer][n-1-layer-i]
            left = I[n-1-layer-i][layer]
            right = I[layer+i][n-1-layer]"""          
            temp = I[layer][layer+i] #temp
            I[layer][layer+i] = I[n-1-layer-i][layer] #top->left
            I[n-1-layer-i][layer] = I[n-1-layer][n-1-layer-i] #left->bottom
            I[n-1-layer][n-1-layer-i] = I[layer+i][n-1-layer] #bottom->right
            I[layer+i][n-1-layer] = temp #right->temp
    return I