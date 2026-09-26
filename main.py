a=int(input('enter the number:'))
b=a
rev=0
while a>0:
    c=a%10
    rev=(rev*10)+c
    a=a//10
if b==rev:
    print('palindrome')
else:
    print('not palindrome')
