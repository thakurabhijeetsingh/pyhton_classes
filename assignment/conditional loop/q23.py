#Write a Python program to print the alphabet pattern 'P'
for row in range(7):
    for col in range(5):
        if (row in {0,3}) and (col in{0,1,2,3}):
            print('*',end=' ')
        elif (row in{4,5,6}) and (col==0):
            print('*',end=' ')
        elif (row in {1,2}) and (col in {0,4}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
            
            