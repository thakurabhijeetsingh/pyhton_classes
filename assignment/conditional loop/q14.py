# Write a Python program that accepts a sequence of comma separated 4 digit binary numbers
# as its input.
# The program will print the numbers that are divisible by 5 in a comma separated sequence.
a=input('binary number')
abhi=a.split(',')
print(abhi)
for i in abhi:
    x=int(i,2)#this is use to convert binary number into integer
    if x%5==0:
        print(x,i)# num and their binary value