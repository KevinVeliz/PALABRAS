palabra = input("Ingrese la palabra a buscar: ")
archivo = open('harry.txt','r')
i=0
acumulador = 0

for line in archivo.readlines(): #leó linea por linea mi archivo
  lista_sin_comas = line.split(".")
  texto_sin_comas= " ".join(lista_sin_comas)
  lista = texto_sin_comas.split()
  i = lista.count(palabra)
  acumulador = acumulador + i

if acumulador !=1:
  print("La palabra: " + palabra + " se repite: " + str(acumulador) )
else:
  print("La palabra: " + palabra + " se repite " + str(acumulador) )
archivo.close()

