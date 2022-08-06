P=float(input("Principal = "))
R=float(input("Rate of intrest = "))
Y=float(input("Number Of Years / ONLY ANNUALY OR YEARLY = "))
a=float(((100+R)/100))
b=(a**Y)
c=(P*b)
f=int((c-P))
print("COMPOUND INTREST = ",f)












