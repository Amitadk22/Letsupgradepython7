#to find the first armstrong number in the range 1042000 to 702648265

for n in range(1042000,70264827):
    temp=n
    sum=0
    order=len(str(n))
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10

    if n == sum:
        print(n)
        break

