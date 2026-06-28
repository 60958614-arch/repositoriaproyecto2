from datetime import datetime 

print("\n=================== INGRESO DE DATOS ======================")
print("************** Cliente : ************")
dni = int(input("ingrese DNI del cliente :\t\t\t"))
apellido = input("Ingrese apellido del cliente :\t\t")
nombre = input("ingrese nombre del cliente:\t\t\t")
DatosCompletos = nombre + " " + apellido  
print("*************** Tipo de cambio  ****************")
Tipodecambio = float(input("Ingrese tipo de cambio a SOLES:\t\t"))

#calculando
MontoimpuestoDolares = preciodeventaendolares * 0.19
MontopagoDolares = preciodeventaendolares + MontoimpuestoDolares

MontoInpuestoSoles = MontoimpuestoDolares * Tipodecambio
MontoPagoSoles = MontopagoDolares * Tipodecambio