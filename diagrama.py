print("-------------------------------")
print("-----verificar triangulo-------")
print("-------------------------------")

a=input("dijite el primer numero")

b=input("dijite el segundo numero")

c=input("dijite el tercer numero")

if a+b>=c:
    r = " se puede formar el triangulo"
elif b+c>=a:
    r= "se puede formar un triangulo "
elif  a+c>=b:
    r="se puede formar un triangulo"
else:
    r="el triangulo no se puede hacer "

print(r)


