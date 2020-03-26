#Developed by Shebin Jose Jacob
#Python program to plot BINDING ENERGY CURVE using Semi Empirical Formula

from numpy import *
from matplotlib import pyplot as mp

a1 = 15.75
a2 = 17.8
a3 = 0.711
a4 = 23.7
a5 = 11.8

z = arange(1,83,1,'float')
a = []

f=open('data.txt','r')

while True:
    s =f.read(3)
    if s == "":
        break
    else:
        a.append(s)
a.pop()

for i in range (len(a)):
    a[i]=float(a[i])
    print (a[i])

#Volume Energy    
def ev(x):
    return a1*x
ev = vectorize(ev)
ve = ev(a)
ve[0] = 0

#Surface Energy
def es(x):
    return -a2*(x**(2./3))
es = vectorize(es)
se = es(a)
se[0] = 0

#Coulomb Energy
def ec(a,z):
    return -a3*z*(z-1)*(a**(-1./3))
ec = vectorize(ec)
ce = ec(a,z)
ce[0]= 0

#Asymmetry Energy
def ea(a,z):
    return -a4*((a-2*z)**2)/a
ea = vectorize(ea)
ae = ea(a,z)
ae[0] = 0

#Pairing Energy
def ep(a,z):
    n = a-z
    pe = a5*(a**(-1./2))
    if (n+z)%2 == 1:
        return 0
    else:
        if z%2==0:
            return pe
        else:
            return -1*pe
ep = vectorize(ep)
pe = ep(a,z)
pe[0]=0

def div(x,y):
    return x/y

div  = vectorize(div)
vepa = div(ve,a)
sepa = div(se,a)
cepa = div(ce,a)
aepa = div(ae,a)
pepa = div(pe,a)

#Plot
lbl  = "Atomic No"
mp.plot(a,vepa)
mp.plot(a,-sepa,'r')
mp.plot(a,-cepa,'g')
mp.plot(a,-aepa,'y')
mp.plot(a,pepa,'b')
te = pepa+aepa+sepa+cepa+vepa
mp.plot(a,te)
mp.xlabel(lbl)
mp.ylabel("Energy Per Nucleus")
mp.show()
