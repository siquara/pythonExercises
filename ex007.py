productPrice = float(input('Digite o preço do produto: R$ '))

productDiscount = float(input('Quantos % de desconto esse produto vai ter? '))


def calcNewPrice(price, discount):
    discount_value = price * discount / 100
    new_price = price - discount_value  
    return new_price


print(f'o produto custava R${productPrice} foi aplicado um desconto de {productDiscount}%.\n o novo valor do produto é R$ {calcNewPrice(productPrice, productDiscount)}')