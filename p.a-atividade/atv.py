#ordem inversa
num = int(int(input("digite um numero: ")))
while num > 0:
    print(num % 10, end="")
    num = num // 10


#contador de digitos 
numero = int(input("Digite um número: "))
contador = 0
while numero > 0:
    contador += 1
    numero //= 10
print(f"O número tem {contador} dígitos.")


#cofrinho
guardar = 10000
total = 0
meses = 0
dep = float(input("Digite o valor do depósito mensal: "))
while total < guardar:
    total += dep
    meses += 1
print(f"meses necessários: {meses}")
print(f"total guardado: R${total}")
print(f"meta atingida no mês: {meses}")


#caixa registradora
total = 0
while True:
    preco = float(input("Digite o preço do produto (ou 0 para encerrar): "))
    if preco == 0:
        break
    quant = int(input("Digite a quantidade do produto: "))
    total += preco * quant
if total < 100:
    desconto = 0
elif total < 500:
    desconto = total * 0.05
elif total < 1000:
    desconto = total * 0.10
else:
    desconto = total * 0.15
vfinal = total - (total * desconto / 100)
print(f"Total da compra: R${total:.2f}")
print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Valor final: R${vfinal:.2f}")



