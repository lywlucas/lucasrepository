def isprime(a):
    if a%2==0:
        return False
    i=3
    while(i*i<=a):
        if a%i==0:
            return False
        else:
            i+=2
    return True
x=int(input())
if x<6 or x%2==1:
    print("Error!")
else:
    maxi=x//2+1
    for i in range(3,maxi,2):
        y=i
        z=x-i
        if isprime(y) and isprime(z):
            print("%d=%d+%d" % (x,y,z))
