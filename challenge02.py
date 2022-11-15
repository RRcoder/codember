import re
ult=''
xxx=[]
def partir(c):
    return re.split('\n| ', c)

def data_to_dicc(l, keys):
    dicc={}
    for i in l:
        kv=re.split(':', i)
        if kv[0] in keys:
            dicc[kv[0]]=kv[1]
    return dicc

f = open("users.txt", "r")
a=f.read() # leo todo el archivo porque es cortito

b= re.split('\n\n', a)

print(len(b))
print("===========")

c=list(map( partir, b))

oblig_keys=['usr','eme','psw','age','loc','fll']
ccc=0
last_usr=''
for r in c:
    d= data_to_dicc(r, oblig_keys)
    todos = [1 for x in d.keys() if x in oblig_keys]
    print(d)
    if sum(todos)==6:
        print("YES")
        print(d['usr'])
        ccc+=1
        last_usr=d['usr']
    else:
        print('NO')

print("===========")
print("cantidad de correctos: {}".format(ccc))
print("ultimo user {}".format(last_usr))

f.close()
