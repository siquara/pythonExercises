lanche = ('hanbúguer', 'suco', 'pizza','pudim')

print(lanche)

for c in range(0, len(lanche)):
    print(lanche[c])

print("----------")

for c in lanche:
    print(c)

#Trup,as são imutáveis
print("----------")
print(lanche[1])

# lanche[1] = "teste" - TypeError: 'tuple' object does not support item assignment


print('-------')
print(sorted(lanche))


print("----------")
print(lanche.count('suco'))