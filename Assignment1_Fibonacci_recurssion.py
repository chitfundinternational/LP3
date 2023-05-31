import time
initial=time.time()
def Fib(n):
   if n <= 1:
       return n
   else:
       return (Fib(n - 1) + Fib(n - 2))  # function calling itself(recursion)

# n=4
# print(Fib(6))

n = int(input("Enter the Value of n: "))  # take input from the user
print("Fibonacci series :")
for i in range(n):
   print(Fib(i),end = " ")
final=time.time()
print("\nTime for execution is ", final-initial)