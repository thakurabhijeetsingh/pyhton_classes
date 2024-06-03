#Write a Python program to check the validity of passwords input by users.
#Validation :
#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.
a=input('password')
lower=0
upper=0
digit=0
spr=0
for i in a:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1 
    elif i.isdigit():
        digit+=1
    elif i in '$#@':
        spr+=1
if lower > 0 and upper>0 and digit>0 and spr>0 :
    if len(a)>6 and len(a)<16:
        print('password valid')
    else:
        print('invalid password')
else:
    print('missing')
          
        
        
                