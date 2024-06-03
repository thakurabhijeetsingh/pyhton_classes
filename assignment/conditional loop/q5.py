#Write a Python program to count the number of even and odd numbers in a series of numbers
even=0
odd=0
a=int(input('enter value'))
for i in range(a,31):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)