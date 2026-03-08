"""a="harsha"
b=a[-3]
print(b)"""
"""

a=input()
b=a[::-1]

if a == b:
    print("palin")
else:
    print ("not")"""

"""a, b, c = map(int, input("Enter three numbers (comma separated): ").split(","))

if a > b and a > c:
    print("Largest:", a)

elif b > a and b > c:
    print("Largest:", b)

else:
    print("Largest:", c)"""


"""#while loops
vardhan = 5

while vardhan > 0:
    print("hello vardhan")
    vardhan -= 2

print("over")"""

#LOOP for

"""
 
for i in range(2,3):
    for j in range(1,11):
        
        print(f"{i} * {j} = {i*j}")"""

"""
n=int(input('enter a natural '))

i=1


while i<=10 :

   print(f"{n} x {i}={n*i}")

   i += 1

print("over")"""

"""
n=int(input())

f=1

while n>0 :

     f *= n
     n -=1

print(f)"""


""" 
 
a=input("enter some value :")
b=str(a)


def varible_name(f) :
    if  "apple" == f :
        print("10")
    else:
        print("20")

varible_name(b)"""

def var(v):
    if v == 0:      # Base case
        return
    print(v)
          # Recursive call

var(4)