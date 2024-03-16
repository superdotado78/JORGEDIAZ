def calcular_iva(subtotal, porcentaje_iva = 13):
    valor_iva = (subtotal * porcentaje_iva) / 100
    return valor_iva
subtotal = 520
valor_iva = calcular_iva(subtotal)
print(f'El valor del IVA es: {valor_iva}')
subtotal_mc = 730
valor_iva = calcular_iva(subtotal_mc, 15)
print(f'El valor del IVA es: {valor_iva}')
