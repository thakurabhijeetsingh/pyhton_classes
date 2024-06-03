#Write a Python program that takes two digits m (row) and n (column) as input and generates
# a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
row=int(input('enter row number'))
coloumn=int(input('enter coloumn number'))
list1=[]
for i in range(row):
    list2=[] #this list signifies the rows in the array  
    for j in range(coloumn):
        list2.append(i*j)
    list1.append(list2)
print(list1)
    
    

