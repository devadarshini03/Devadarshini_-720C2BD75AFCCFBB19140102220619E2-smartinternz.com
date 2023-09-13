
def fact(n):
 if n==0:
   return 1
 else:
   return n*fact(n-1)
print("\nfactorial of a number")
num=int(input("enter a non negative integer:"))
factorial=fact(num)
print("the factorial of",num,"is",factorial)