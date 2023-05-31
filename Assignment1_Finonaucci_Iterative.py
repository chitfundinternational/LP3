def Fib(n):
    if n<=1:
        return n
    to=0 
    t1=1
    var = None
    for i in range(2,n+1):
        f=to+t1
        to=t1
        t1=f
    return f
n=int(input("Enter your number for fibonaucci series :"))
#print("Fibonaucci Series:", Fib(n))
for j in range(n+1):
    print(Fib(j),end = " ") 

        