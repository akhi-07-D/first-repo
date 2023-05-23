num=int(input())
if num >1:
    for i in range (2,int(num/2)+1):
        if (num%1)==0:
            print(num, "not prime")
            break
    else:
        print(num,"is prime")
else:
    print(num, "is not prime")