# O exercicio que criei em tupla foi para uma revisão o objetivo é saber quais os vendedores que baterão a meta
# 1. Tupla com os nomes dos 10 vendedores
vendedores = (
    "Carlos", "Ana", "Paulo", "Mariana", "Lucas",
    "Beatriz", "Fernando", "Juliana", "Rodrigo", "Camila")

 # 2. Tupla com os 10 valores em reais (floats)
vendas_reais = (
    1250.50, 3400.00, 2100.75, 4500.20, 1800.00,
    2900.30, 5100.00, 3150.80, 950.00, 4200.00)
meta = 3000
# juntando as tuplas:
## COM O CAST EXPLÍCITO (Conversão para tupla):

juncaotupla = tuple(zip(vendedores, vendas_reais))
print(f'{"Lista dos Vendedores que bateram a meta":.^60}\n')
# Calcula quem superou ou foi igual a meta
for vendedor, valor in (juncaotupla):
    if valor >= meta:
        # Convertendo a moeda para o padrão brasileiro utiizando o replace
        valor_br = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f'{vendedor:.<50} R$ {valor_br}')