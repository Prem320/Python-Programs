# 3- Write a program in python check palindrome or not
'''s=input("Enter the any values:")
palin=s[::-1]
if (s==palin):
    print(s,"is palindrome")
else:
    print(s,"is not palindrome")'''

def prem():
    s=input("enter the any value: ")
    palin=""
    for char in s:
        palin=char+palin
    if (palin==s):
        print(s,"is palindrome")
    else:
        print(s,"is not palindrome")
prem()