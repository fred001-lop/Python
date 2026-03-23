#Fundamentos del bucle while



blocks = int(input("Ingrese el numero de bloques: "))

#Variables

height = 0
blocks_usados = 0
blocks_en_fila = 1

#Calculamos la altura
while blocks_usados + blocks_en_fila <= blocks:
    blocks_usados += blocks_en_fila
    height += 1
    blocks_en_fila +=1 
    

print("La altura de la piramide es", height)