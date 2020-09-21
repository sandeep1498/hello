l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(l1)):
    for j in range(len(l1)):
        l2[i][j]=l1[j][i]  
print(l2)
