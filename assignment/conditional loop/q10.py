#Write a Python program that accepts a string and calculates the number of digits and letters.
digits=0
letters=0
a=input('enter ')
for i in a:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
print(digits)
print(letters)