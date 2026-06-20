import random
a=random.randint(1,50)
k=0
n=0
while (a!=50):
    print(a, end=' ')
    if(a%2==0):
        k=k+1
    else:
        n=n+1
    a=random.randint(1,50)
print('Паних чисел - ',k)
print('Непарних чисел - ',n)
input()
