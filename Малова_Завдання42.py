import random
a=random.randint(1,50)
k=0
n=0
s=0
while (a!=50):
    s=s+a
    print(a,end=' ')
    if(a%2==0):
        k=k+1
    else:
        n=n+1
    a=random.randint(1,50)
s=s/(k+n)
print('Парних - ',k)
print('Непарних - ',n)
print('Середнє арифметичне - ',s)
input()
