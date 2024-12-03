# 1. Solicitar al usuario las medidas de la pieza del mueble en cms

medida_cms = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cms): "))

# 2. Convertir las medidas de centímetros a pulgadas

medida_pulgadas = medida_cms / 2.54

# 3. Mostrar las medidas convertidas en pulgadas al usuario

print("La medidas en pulgadas de la pieza ingresada son:", medida_pulgadas)