entrada = int(input())

agregar = []
eliminar = []

for i in range(entrada):
    z = list(input().split())
    if z[0] == '1':
        agregar.append(z[1])
        
    elif z[0] == '2':
        if not eliminar:
            while agregar:
                eliminar.append(agregar.pop())
        eliminar.pop()
        
    else:
        if not eliminar:
            while agregar:
                eliminar.append(agregar.pop())
        print(eliminar[-1])
        
        