n=int(input("Enter the number"))

temp=n

rev=0

while n>0:
    rev=rev*10+n%10
    n=n//10

if temp==rev:
    print("palindrome")
else:
    print("Not Palindrome")