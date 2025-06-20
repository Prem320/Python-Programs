# 2- Write a program in python print the fabonaccie series
num=int(input("Enter the any values:"))
n1=0
n2=1
sum=0
for i in range(1,num):
    n1=n2
    n2=sum
    sum=n1+n2
    print(sum,end=" ")