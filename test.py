idade = int(input("qual a sua idade?"))
print(idade)
if idade >= 18:
    print("Adulto")
elif idade <= 17 and idade > 14:
    print("Adolescente")
else:
    print ("criança")