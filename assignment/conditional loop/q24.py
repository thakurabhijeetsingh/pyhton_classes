# Write a Python program to print the alphabet pattern 'R'.
for row in range(7):
    for col in range(5):
        if (row in {0,3}) and (col in {0,1,2,3}):
            print('*',end=' ')
        elif (row in {1,2,6}) and( col in {0,4}):
            print('*',end=' ')
        elif row in {4} and col in {0,1}:
            print('*',end=' ')
        elif row in {5} and col in {0,2}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()