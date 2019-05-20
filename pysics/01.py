import numpy as np
x=[33.8,33.15,33.21,34.85,34.09] #data
n=5   #measuring times
deta=0.05
C=3
D=70

tp_list=[1.84,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.05,1.03]
tp=tp_list[n-2]
avr=np.mean(x)
print('avr ',avr)

print((D*D-avr*avr)/(4*D))

ua=tp*np.sqrt(1/(n*(n-1))*np.var(x))
print('ua ',ua)  #A class uncertainty

ub=deta/C
print('ub ',ub) #B class uncertainty

uc=np.sqrt(ua*ua+ub*ub)
print('uc ',uc)  #C class uncertainty

a=70*70+33.82*33.82
b=70*70-33.82*33.82
c=((a/(70*b))*0.017)
d=((2*33.82)/b)*0.160
print(np.sqrt((c*c)+(d*d)))

print(0.00291*13.41503)