want=int(input('Яку суму ви бажаєте отримати - '))
have=int(input('Яку суму ви маєте - '))
suma=have
k=0
while suma<=want:
    suma=suma+0.24*suma
    k=k+1
    print(suma)
print('Потрібно',k, 'років')
input()
