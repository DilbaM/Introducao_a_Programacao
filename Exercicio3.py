#Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma
#mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior a 6 o aluno é
#aprovado). Escrever também o resultado da média calculada.


n1=float (input("Digite sua primeira nota: "))
n2=float (input("Digite sua segunda nota: "))
total=((n1+n2)/2)
if total >= 7:
    print(f'você tirou {total} e foi aprovado')
else:
    print(f"você tirou {total} e reprovou")