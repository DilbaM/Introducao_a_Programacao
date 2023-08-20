#Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O
#programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário


n1=float (input("Digite um numero: "))
if n1>10:
    print(f"O numero {n1} é maior que 10")
else:
    print(f"O numero {n1} é menor que 10")