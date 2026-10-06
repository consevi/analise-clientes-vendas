import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PROJETO: ANÁLISE ESTRATÉGICA DE CLIENTES E VENDAS
# ============================================================


# ============================================================
# 1. CARREGAMENTO DOS DADOS
# ============================================================

tbc = pd.read_csv(("tb_clientes_bruto.csv"), sep=';')
tbv = pd.read_csv(("tb_vendas_bruto.csv"), sep=';')

dadoc = np.loadtxt(("tb_clientes_bruto.csv"), delimiter=';')
dadov = np.loadtxt(("tb_vendas_bruto.csv"), delimiter=';')
# ============================================================
# 2. EXPLORAÇÃO DOS DADOS
# ============================================================

# Estrutura:
print(f"Shape tbc: {tbc.shape}")
print(f"Total de elementos tbc: {tbc.size}")
print(f"Dimensoes tbc: {tbc.ndim}\n\n")

print(f"Shape tbv:{tbv.shape}")
print(f"Total de elementos tbv:{tbv.size}")
print(f"Dimensoes tbv: {tbv.ndim}\n\n")


# Categorias:

print(f"Tbc: {tbc.columns}\n")
print(f"Tbv: {tbv.columns}")

# Verificando se existem valores do tipo NaN:

print(f"NaN tbc: {tbc.isnull().sum()}\n\n")

print(f"NaN tbv: {tbv.isnull().sum()}\n")


# ============================================================
# 3. ANÁLISE BÁSICA DOS CLIENTES
# ============================================================

# Idade média dos clientes:

idade_media_tbc = tbc["idade"].mean()
print(f"Idade Média dos clientes: {idade_media_tbc:.2f}")

# Maior e Menor idade:

print(f"\nMaior idade: {tbc["idade"].max()}")

print(f"Menor idade: {tbc["idade"].min()}\n")


# Renda mensal dos clientes:

renda_media = tbc["renda_mensal"].mean()
print(f"Renda média dos clientrs: {renda_media:.2f}\n")


# Menor e Maior renda:

print(f"Maior renda: {tbc["renda_mensal"].max()}")
print(f"Menor renda: {tbc["renda_mensal"].min()}\n")

# ============================================================
# 4. CLASSIFICAÇÃO DE RENDA
# ============================================================

# Classificando os clientes:

tbc["class_renda"] = tbc["renda_mensal"].apply(
    lambda i: "Alta renda" if i > 5000 else("Baixa renda" if i < 2000 else "Média renda")
)


# Quantidade de clientes por renda:

qtd_clientes_por_renda = tbc.groupby("class_renda")["renda_mensal"].count()
print(f"Quantidade de clientes em cada classe de renda: {qtd_clientes_por_renda}")

# Classe que possui mais clientes:

print(f"\nClasse que possui mais clientes: {qtd_clientes_por_renda.idxmax()}\n")

# Renda média de cada classe:

media_por_classe = tbc.groupby("class_renda")["renda_mensal"].mean()
print(f"Média de renda por classe: {media_por_classe}\n")


# ============================================================
# 5. ANÁLISE POR ESTADO
# ============================================================

# Renda média por estado:
renda_media_estado = tbc.groupby("sg_uf")["renda_mensal"].mean()
print(f"Renda média por estado: {renda_media_estado}\n")

print(f"Estado com maior renda média: {renda_media_estado.idxmax()} - renda: {renda_media_estado.max():.2f}") 

print(f"Estado com menor renda média: {renda_media_estado.idxmin()} - renda: {renda_media_estado.min():.2f}") 

# Quantidade de clientes em cada estado:

print(f"\nQuantidade de clientes por estado: {tbc.groupby("sg_uf")["nm_cliente"].count()}\n")

qtd_clientes_estado = tbc.groupby("sg_uf")["nm_cliente"].count()

print(f"Estado com mais clientes: {qtd_clientes_estado.idxmax()} - quantidade {qtd_clientes_estado.max()}")


# ============================================================
# 6. ANÁLISE DAS VENDAS
# ============================================================

# Faturamento total:

faturamento_total = tbv["vl_total"].sum()
print(f"Faturamento total: {faturamento_total}\n")

media_faturamento = tbv["vl_total"].mean()
print(f"Média do faturamento total: {media_faturamento:.2f}")

# Valor da maior e manor venda:
maior_venda = tbv["vl_total"].max()
menor_venda = tbv["vl_total"].min()
print(f"Maior venda: {maior_venda} - Menor venda {menor_venda}")

# Quantidade de vendas:
qtd_vendas = tbv["vl_total"].count()
print(f"Quantidade de vendas: {qtd_vendas}")


# ============================================================
# 7. ANÁLISE POR CATEGORIA
# ============================================================

# Quantidade de vendas por categoria:

qtd_vendas_categoria = tbv.groupby("categoria_prod")["qtd"].sum()
print(f"\nQuantidade de vendas por categoria: {qtd_vendas_categoria}\n")

print(f"Categoria com maior quantidade de vendas: {qtd_vendas_categoria.idxmax()} - Vendas: {qtd_vendas_categoria.max()}\n")

# Faturamento de cada categoria:

faturamento_categoria = tbv.groupby("categoria_prod")["vl_total"].sum()
print(f"Faturamento de cada categoria: {faturamento_categoria}\n")
print(f"Categoria com maior faturamento: {faturamento_categoria.idxmax()} - Faturamento: {faturamento_categoria.max()}\n")

# Média de cada categoria:
media_faturamento_categoria = tbv.groupby("categoria_prod")["vl_total"].mean()
cateogira_maior_media = media_faturamento_categoria.max()
print(f"Média de faturamento de cada categoria: {media_faturamento_categoria}\n")
print(f"Categoria com maior média: {media_faturamento_categoria.idxmax()} - Média: {cateogira_maior_media:.2f}")


# ============================================================
# 8. RELAÇÃO ENTRE CLIENTES E VENDAS
# ============================================================


# Quanto cada cliente gastou:

clientes_vendas = pd.merge(
    tbc,
    tbv,
    left_on="id_cli",
    right_on="cliente_id"
)

total_por_cliente = clientes_vendas.groupby(["id_cli", "nm_cliente"])["vl_total"].sum()
print(f"\nTotal de gasto de cada cliente: {total_por_cliente}\n")

# Clientes que mais gastou e os que compraram mais:

total_por_cliente = clientes_vendas.groupby("id_cli")["vl_total"].sum().reset_index(name="total_gasto_cliente")
top10_clientes = total_por_cliente.nlargest(10, "total_gasto_cliente")


qtd_por_cliente = clientes_vendas.groupby("id_cli")["qtd"].sum().reset_index(name="total_compras")
top10_clientes_compras = qtd_por_cliente.nlargest(10, "total_compras")

print(f"Top 10 clientes: {top10_clientes}\n")

print(f"Clientes que realizaram mais compras: {top10_clientes_compras}\n")

# Quais clientes realizaram apenas uma compra:

clientes_com_uma_compra = total_por_cliente[total_por_cliente == 1]
print(f"Clientes que só fizeram 1 compra: {clientes_com_uma_compra}\n")

# ============================================================
# 9. RENDA x CONSUMO
# ============================================================

# Biografia dos clientes: 

#r = tbc["id_cli"].count()
#for i in range(1, r + 1):
    #print(f'Nome: {tbc.loc[tbc["id_cli"] == i, "nm_cliente"]}')
    #print(f'Renda mensal: {tbc.loc[tbc["id_cli"] == i, "renda_mensal"]}')
    #print(f'Valor total gasto: {qtd_por_cliente.loc[qtd_por_cliente["id_cli"] == i, "total_compras"]}')
    #print('====================================\n')


# Qual cliente gastou mais:

cliente_mais_gastou = qtd_por_cliente.nlargest(1, "total_compras")
nome_cliente_mais_gastou = tbc.loc[tbc["id_cli"] == cliente_mais_gastou["id_cli"].iloc[0], "nm_cliente"]
renda_cliente_mais_gastou = tbc.loc[tbc["id_cli"] == cliente_mais_gastou["id_cli"].iloc[0], "renda_mensal"]
valor_gasto_cliente_mais_gastou = total_por_cliente.nlargest(1, "total_gasto_cliente")

cliente_menos_gastou = qtd_por_cliente.nsmallest(1, "total_compras")
nome_cliente_menos_gastou = tbc.loc[tbc["id_cli"] == cliente_menos_gastou["id_cli"].iloc[0], "nm_cliente"]
renda_cliente_menos_gastou = tbc.loc[tbc["id_cli"] == cliente_mais_gastou["id_cli"].iloc[0], "renda_mensal"]
valor_gasto_cliente_menos_gastou = total_por_cliente.nsmallest(1, "total_gasto_cliente")

print(f"Cliente que mais gastou: {nome_cliente_mais_gastou}")
print(f"Renda do cliente que mais gastou: {renda_cliente_mais_gastou}")
print(f'Valor gasto: {valor_gasto_cliente_mais_gastou["total_gasto_cliente"]}')

print(f"\nCliente que gastou menos: {nome_cliente_menos_gastou}")
print(f"Renda do cliente que menos gastou: {renda_cliente_menos_gastou}")
print(f'Valor gasto: {valor_gasto_cliente_menos_gastou["total_gasto_cliente"]}\n')


# Clientes com maior renda tendem a gastar mais?
# Sim, conforme a analise, o cliente com maior renda gastou mais em relaçao ao com menor renda.

# ============================================================
# 10. ESTATÍSTICA COM NUMPY
# ============================================================

# Média dos valores de venda:
qtd = np.dadoc["qtd"].to_numpy()
preço = np.dadoc["vl_total"].to_numpy()

media_vendas = (qtd * preço) / len(qtd)
print(f"Média das vendas: {media_vendas}")

# Mediana dos valores de venda:

mediana_vendas = np.median(preço)
print(f"Mediana: {mediana_vendas}")

# Menor valor de venda e o Maior valor de venda

maior_preço = preço.nlargest(1, "qtd")
menor_preço = preço.nsmallest(1, "qtd")
print(f"Maior preço: {maior_preço}")
print(f"Menor preço: {menor_preço}")

# A amplitude dos valores:
amplitude_preços = maior_preço - menor_preço
print(f"Amplitude dos valores: {amplitude_preços}")


# Calcule o desvio padrão dos valores de venda.



# Compare a média e a mediana.
#
# Elas são parecidas?
# Ou existe uma diferença grande entre elas?



# Analise se existem valores muito distantes



# Na sua opinião, a média representa bem os dados?
# Nao, porque tem valores muito altos enquanto outros muito baixos, ou seja, o valor alto de certa forma "compensa" o valor baixo.


# ============================================================
# 11. GRÁFICOS — MATPLOTLIB
# ============================================================

# Questão 114:
# Crie um gráfico mostrando a quantidade de clientes
# por estado.


# Questão 115:
# Crie um gráfico mostrando a renda média
# de cada estado.


# Questão 116:
# Crie um gráfico mostrando o faturamento
# de cada categoria.


# Questão 117:
# Crie um gráfico mostrando os 10 clientes
# que mais gastaram.


# Questão 118:
# Crie um gráfico comparando:
#
# Renda mensal x Valor gasto
#
# O objetivo é tentar visualizar se existe
# relação entre renda e consumo.


# ============================================================
# 12. ANÁLISE FINAL
# ============================================================

# Questão 119:
# Qual estado possui o melhor perfil de renda?


# Questão 120:
# Qual estado possui mais clientes?


# Questão 121:
# Qual categoria gera mais dinheiro?


# Questão 122:
# Qual categoria possui mais vendas?


# Questão 123:
# Quem são os principais clientes da empresa?


# Questão 124:
# Clientes de maior renda realmente gastam mais?


# Questão 125:
# Qual faixa de renda é mais importante para a empresa?


# Questão 126:
# Existe algum estado que possui muitos clientes,
# mas baixo faturamento?


# Questão 127:
# Existe algum estado com poucos clientes,
# mas alto faturamento?


# Questão 128:
# Existe alguma categoria que vende muito,
# mas gera pouco dinheiro?


# Questão 129:
# Se você fosse o analista da empresa,
# qual seria sua principal recomendação?


# ============================================================
# FIM DO PROJETO :)
# ============================================================





