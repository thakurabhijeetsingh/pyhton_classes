#Write a Python program to print the alphabet pattern 'L'.
for row in range (7):
    for col in range (5):
        if( row!=0 )and (col==0):
            print('*',end='')
        elif row==6:
            print('*',end='')
        else:
            print(' ',end='')
    print() 