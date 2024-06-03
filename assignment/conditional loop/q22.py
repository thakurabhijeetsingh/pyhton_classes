#Write a Python program to print the alphabet pattern 'O7
for row in range (7):
    for colom in range (5):
        if (row in {0,5}) and (colom in{1,2,3}):
            print('*',end=' ')
        elif (row in {1,2,3,4}) and (colom in{0,4}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()