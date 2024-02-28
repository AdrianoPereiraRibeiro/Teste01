n1=float(input('Qual o tamanho do primeiro lado do triângulo:'))
n2=float(input('Qual valor do segundo lado do triãngulo:' ))
n3=float(input('Qual valor do terceiro lado do triângulo:'))
if n1+n2<n3 or n2+n3<n1 or n1+n3<n2:
   print("Isso não é um triângulo.") 
if n1==n2 and n1==n3 and n3==n2: 
    {print('Esse triângulo é equilátero.')}
if n1==n2 and n3!=n1: 
   { print('Esse triângulo é isósceles') }
if n1==n3 and n3!=n2:
   { print('Esse triângulo é isósceles') }
if n3==n2 and n3!=n1:
   { print('Esse triângulo é isósceles') }
if  n1!=n2!=n3 and n1!=n3:
   { print('Esse triângulo é escaleno.')}

