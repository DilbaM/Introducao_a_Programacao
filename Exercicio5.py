#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
#quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade
#média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual
#a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.


e_a=int (input("Qual o estoque atual?"))
e_m=10
e_max=100
e_media=int ((e_max+e_m)/2)
if e_a>=e_media:
    print(f"Seu estoque de {e_a} está na media, não precisa comprar mais")
else:
    print(f"Comprar mais {e_media-e_a} produtos, você esta com pouco estoque")