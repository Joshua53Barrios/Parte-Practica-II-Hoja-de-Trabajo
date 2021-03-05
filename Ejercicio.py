#Programa 1
print("¡Hola a  '"" todas "' " y '" todos")
print()

#Programa 2
nombre=input('Ingrese su nombre')
print('!Bienvenido ', nombre,'!')
print()

#Programa 3
x=1
y=0
a1=x|y
a2=y|y
a3=y|x
a4=x|x 
print("X Y Q")
print(y, y, a2)
print(x, y ,a1)
print(y, x ,a3)
print(x, x ,a4)
print()

#Programa 4
horas=int(input('Ingrese un promedio de horas que le dedica al estudio en Programación a la semana'))
total=(float(horas)/7)
mes=horas*4
print('El alumno estudia en total de horas al día: ', "{0:.2f}".format(total))
print('El alumno estudia en total de horas al mes: ', mes)
print()

#Programa 5
m=int(input('Ingrese un número para realizar la sumatoria'))
dato=((m+1)*(m))/(2)
print('La sumatoria de números desde 0 hasta el número ingresado es igual a ', dato)
print()

#Programa 6 
altura=float(input('Ingrese su altura en metros'))
peso=float(input('Ingrese su peso en kilogramos "kg"'))
IMC=(peso)/(altura*altura)
print('Su indice de masa corporal es de  ', "{0:.2f}".format(IMC))
print()

#Programa 7
x1=float(input('Ingrese el primer número de la división'))
x2=float(input('Ingrese el segundo número de la división'))
coc=float(x1)/x2
pro=float(x1)%x2
print('El cociente de la división es de : ', "{0:.2f}".format(coc))
print('El residuo de la división es de : ', "{0:.2f}".format(pro))
print()

#Programa 8
monto=int(input('Ingrese el monto a invertir'))
interes=int(input('Ingrese el interes anual'))
año=int(input('Ingrese el número de años que se va a realizar la inversion'))
capital=(monto*100)/(interes*año)
print('El capital obtenido por la inversión sera de:  ',capital)
print()

#Programa 9
print('"Ferretería Marroquin"_________Cálculo de peso del paquete a enviar')
barrenos=int(input('Ingrese el número de barrenos comprados'))
sierras=int(input('Ingrese el número de sierras compradas'))
paquete=(barrenos*112)+(sierras*75)
print('El peso total del paquete es de ', paquete,'kg')
print()
 
#Programa 10
print('Venta Tecnologica')
RAM=int(input('Ingrese el número memorias RAM usadas vendidas'))
Habitual=RAM*20
descuento=(Habitual*60)/(100)
total=Habitual-descuento
print('El precio correspondiento a las', RAM, ' memorias RAM vendidas es: ',Habitual)
print('El descuento del 60 porciento fue de ',descuento , 'por lo que el total es de ', total)
print()
