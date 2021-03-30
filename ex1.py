import math
#Cours 1
''' 
#1.

temps = 6.892
distance = 19.7
vitesse = temps/distance

print(round(vitesse,1))

#-------------------------------
#2.

name = input('nom')
age = int(input('age'))

print('Vous vous appelez :',name, '\n vous avez ',age,'ans')
#-------------------------------



#Cours 2



#1.
entree = input('nombre')
test = entree.isdigit()
if test == True:
    entree = float(entree)
    if int(entree) >= 0:
        print(math.sqrt(entree))
else:
    print("c'est non")

#------------------------



#2.

mot1 = input("premier Mot")
mot2 = input("deuxième Mot")

if(len(mot1)!=len(mot2)):
    if len(mot1) > len(mot2):
        print(mot2,'est le plus petit mot')
    else:
        print(mot1,'est le plus petit mot')
else:
    print('les deux mots sont de la même taille')

res = mot1 if(len(mot1)>len(mot2)) else mot2
print(res)

#------------------------
#3.

Pression= int(float(input('Pression')))
volume= int(float(input('Volume')))
pSeuil = 2.3
vSeuil = 7.41

if Pression> pSeuil and volume>vSeuil:
    print('Stop')
elif Pression >=pSeuil and volume<vSeuil:
    print("Augmenter le volume de l'enceinte")
elif volume > vSeuil and Pression <=pSeuil:
    print("Augmenter la pression de l'enceinte")
else:
    print('Tout va bien')


#------------------------
4.

a,b = 0,10

while (b!=0):
    if (a<b):
        a+=1
    if ((b % 2) != 0):
        b-=1
        print(b)
    


#------------------------
#5.

entree = int(input('nombre'))

while (entree <1) or (entree > 10):
    entree = int(input('nombre'))


#------------------------
#6.
spell = input('Votre mot')
liste = ['mot', 'mot2', 'mot3']
index=0
for i in range(len(spell)):
    print(spell[index])
    index += 1
for i in spell:
    print(i)

for y in liste:
    print(y)


#------------------------
#7.

for i in range(1,15,3):
    print(i)


#------------------------
#8.

for i in range(1,11):
    if(i == 5):
        break
    print(i)


#------------------------
#9.

for i in range(1,11):
    if(i == 5):
        continue
    print(i)


#------------------------



#Cours 3

#1.

def table(base,debut,fin,inc):
    print(base)
    for i in range(debut,fin):
        print(i)
    print(inc*inc)    


table(10,1,8,5)
'''
#------------------------

#2.

def cube(x):
    return x**3


def volumesphere(r):
    return (4*math.pi*cube(r))/3

print(volumesphere(int(input('rayon'))))
