class zebra:
    def __init__(self, lstr):
        self.l=lstr
        self.largo_maximo=0
        self.ultimo_color=""

    def descubrir(self):
        dic= {'c1':'', 'c2':''}
        pos=0
        cont=0
        largo=0
        idx=1
        largomax=0
        ultcol=''
        r_ant=''
        liguales=True
        for r in self.l:
            cont+=1

            if cont==1:
                dic['c1']=r
                pos=1
            if cont==2:
                dic['c2']=r
                pos=2
                idx=1
                largo=2

            if cont>2:
                if idx==1:
                    if r==dic['c1']:
                        largo+=1
                        idx=2
                        if largo>largomax:
                            largomax=largo
                            ultcol=r
                    else:
                        largo=2
                        idx=1
                        dic['c1']=r_ant
                        dic['c2']=r
                        if r==r_ant:
                            liguales=True
                else:
                    if r==dic['c2']:
                        largo+=1
                        idx=1
                        if largo>largomax:
                            largomax=largo
                            ultcol=r
                    else:
                        dic['c1']=r_ant
                        dic['c2']=r
                        largo=2
                        idx=1
                        
            r_ant=r

        self.largo_maximo = largomax
        self.ultimo_color = ultcol


f = open("colors.txt", "r")
a=f.read()

import re
b= re.split(',|\n', a)
c= b[1:-1]
d= [x.strip() for x in c]
e= [x[1:-1] for x in d]
f.close()
print(e)
print("====================================")

z=zebra(e)
z.descubrir()
print(z.largo_maximo)
print(z.ultimo_color)
print("====================================")

