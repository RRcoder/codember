import re

f = open("encrypted.txt", "r")
a=f.read() # leo todo el archivo porque es cortito

b= re.split(' ', a)

print(len(b))
print( b)
print("===========")

palabras=['']

for l in b:
    pos=0
    letra_ascii=''
    bflag=False
    for i in range(len(l)):
        car = l[i]
        if pos==0:
            letra_ascii+=car
            if car=='9':
                bflag=True
            pos+=1
        elif pos==1:
            letra_ascii+=car
    
            if bflag:
                palabras[len(palabras)-1]+=chr(int(letra_ascii))
                bflag=False
                pos=0
                letra_ascii=''
            else:
                pos+=1
        elif pos==2:
            letra_ascii+=car
            palabras[len(palabras)-1]+=chr(int(letra_ascii))
            bflag=False
            pos=0
            letra_ascii=''
    


    palabras.append('')

print(palabras)

    



print("===========")
#print("cantidad de correctos: {}".format(ccc))
#print("ultimo user {}".format(last_usr))



f.close()
