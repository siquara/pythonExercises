#Remoção de duplicatas:

#Dada uma lista com elementos repetidos, crie uma nova lista sem duplicatas.

lista_com_duplicatas = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 1, 9, 10, 5]
novaLista =  []
print(lista_com_duplicatas)

[novaLista.append(num) for num in lista_com_duplicatas if num not in novaLista]

print(novaLista) 