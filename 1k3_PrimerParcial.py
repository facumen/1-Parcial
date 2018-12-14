def es_vocal(a):
    vocales = 'aeiou'
    return a in vocales

def es_consonante(a):
    consonantes = 'qwrtypsdfghjklñzxcvbnm'
    return  a in consonantes

cl = ctl = cp = may1 = may2 = cant_v = cant_c = item3 = item4 = 0
flagItem1 = flagL = False

texto = input("Ingrese un texto finalizado en '.': ")

for i in range(len(texto)):
    if texto[i] != ' ' and texto[i] != '.':
        cl += 1
        ctl += 1
        ult_letra = texto[i]
        if es_vocal(texto[i]):
            cant_v += 1
        else:
            if es_consonante(texto[i]):
                cant_c += 1
        if texto[i] == 'c' and texto[i + 1] == 'h':
            item3 += 1
        if cl == 1 and texto[i] == 'l':
            flagL = True
    else:
        cp +=1
        if not flagItem1:
            may1 = cl
            may2 = cp
            flagItem1 = True
        else:
            if cl > may1:
                may1 = cl
                may2 = cp
        if flagL and es_vocal(ult_letra):
            item4 += 1
        cl = 0
        flagL = False

porc1 = cant_v * 100 // ctl
porc2 = cant_c * 100 // ctl

cant_totalCH = ctl - item3

print('\nCantidad total de caracteres:', ctl)
print('Cantidad total de palabras:', cp)
print('La cantidad de caracteres de la palabra mas larga es:', may1, 'y su posicion es:' ,may2)
print('La cantidad total de consonantes en el texto es de:', cant_c, 'y de vocales:' ,cant_v)
print('El porcentaje de consonantes sobre el total de los caracteres es de:', porc2, '%')
print('El porcentaje de vocales sobre el total de los caracteres es de:', porc1, '%')
print('Cantidad de veces que aparece "ch" en el texto:', item3)
print('En el caso de que "ch" se contara como una letra, el total de letras seria:', cant_totalCH)
print('La cant. de palabras que comienzan con "l" y terminan en vocal son:', item4, '\n')

input("ENTER para salir")