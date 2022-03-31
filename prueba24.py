def squares(numbers):
  for number in numbers:
    yield number*number
 
# esta vez, si hacemos la siguiente llamada, no obtenemos resultados
# sino que vamos a crear un generador
squares([1,2,3,4,5])
 
# podemos iterar sobre el generador
# si ejecutamos
for square in squares([1,2,3]):
    print(square)