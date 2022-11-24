def cumple_req(nro):
    strnro=str(nro)

    cant=0
    cant_5=0
    for c in range(0,5):
        if c >0:
            if int(strnro[c:c+1]) >= int(strnro[c-1:c]):
                cant+=1
        if strnro[c:c+1]=='5':
            cant_5+=1

    rta=False

    if cant_5>=2 and cant==4:
        rta=True

    return rta


print(cumple_req(55555))


lista_ok=[]
for i in range(11098, 98124):
    if cumple_req(i):
        lista_ok.append(i)


print( lista_ok)
print("{}-{}".format( len(lista_ok), lista_ok[55]))

