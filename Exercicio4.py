#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
#escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
#ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'



conta=80-9
saldo=2500
debito=1980
credito=200

saldo_atual=saldo-debito+credito
if saldo_atual>=0:
    print(f"Você está com {saldo_atual} saldo positivo")
else:
    print(f"Você está com {saldo_atual}saldo está negativo")