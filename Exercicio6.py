#Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se
#forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
#calcule e escreva o custo total da compra.




macas=int (input("Quantas maçãs você quer comprar?"))
if macas < 12:
    print(f"{macas} maçãs custam R${macas * 1.30} ")

else:
    print(f"{macas} maçãs custam R${macas * 1}")