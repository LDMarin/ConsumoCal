from queue import Empty
from socket import if_indextoname


print("\nCalculadora de facturacion de consumo electrico CNFL\n")
consumo_kwh = int(input("Ingrese consumo del mes en KWH: "))

# Bloques
b31_200 = 30
b201_300 = 200
b301plus = 300

# Costos kwh por bloque
tarifa_base = 2209.50
cb31_200 = 73.65
cb201_300 = 113.02
cb301plus = 116.85

# Otros
tribBom = 0.0175
alumPub = 3.24
iva_pc = 0.13

# Total por bloque
tb31_200 = 0
tb201_300 = 0
tb301plus = 0

alumbrado_pub = consumo_kwh * alumPub

if consumo_kwh > b301plus:
    tb301plus = (consumo_kwh - b301plus) * cb301plus
    consumo_kwh = b301plus

if consumo_kwh > b201_300:
    tb201_300 = (consumo_kwh - b201_300) * cb201_300
    consumo_kwh = b201_300

if consumo_kwh > b31_200:
    tb31_200 = (consumo_kwh - b31_200) * cb31_200

consumo_total_energia = tarifa_base + tb31_200 + tb201_300 + tb301plus
tributo_bomberos = consumo_total_energia * tribBom
consumo_total = consumo_total_energia + alumbrado_pub + tributo_bomberos
iva = consumo_total * iva_pc
consumo_total_iva = consumo_total + iva

print(f"\nEl total a pagar por el consumo del mes es: {consumo_total_iva:.2f} colones")
print("\n-------------------------Desglose---------------------------\n")
print(f"Costo por energia:                     {consumo_total_energia:.2f} colones")
print(f"Alumbrado publico:                     {alumbrado_pub:.2f} colones")
print(f"Tributo Bomberos:                      {tributo_bomberos:.2f} colones")
print(f"IVA:                                   {iva:.2f} colones\n")
