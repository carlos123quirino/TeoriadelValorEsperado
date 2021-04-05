print("INSERTA DATOS DE LA PRIMERA OPCION\n")
x1 = float(input("Ingresa cantidad a Ganar:\t"))
p1 = float(input("Ingresa probabilidad de Ganar:\t"))
x2 = float(input("Ingresa cantidad a Perder:\t"))
p2 = float(input("Ingresa probabilidad de Perder:\t"))
print("\n\nINSERTAR DATOS DE LA SEGUNDA OPCION\n")
x11 = float(input("Ingresa cantidad a Ganar:\t"))
p11 = float(input("Ingresa probabilidad de Ganar:\t"))
x21 = float(input("Ingresa cantidad a Perder:\t"))
p21 = float(input("Ingresa probabilidad de Perder:\t"))

print("La opcion 1 queda de la siguiente manera: Ganar ", x1," con ", p1, " de probabilidad o perder ", x2, " con ", p2, " de probabilidad ")
print("La opcion 2 queda de la siguiente manera: Ganar ", x11," con ", p11, " de probabilidad o perder ", x21, " con ", p21, " de probabilidad ")

s1 = ((x1*(p1/100)) - (x2*(p2/100)))
s2 = ((x11*(p11/100)) - (x21*(p21/100))) 

if(s1>s2):
	print("\n<<<<<<<<La mejor opcion ingresas es la Numero 1>>>>>>>>")
else:
	print("\n<<<<<<<<La mejor opcion ingresada es la Numero 2>>>>>>>>")
