def es_prime(n): 
  if n ==1 :
    return print('NO es primo')  
  for i in range(2, n):
         if n % i == 0:
          return print('NO es primo')
  return print('Es primo')

n = int(input("Ingrese número: "))
es_prime(n)