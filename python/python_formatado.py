import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PROJETO: ANÁLISE ESTRATÉGICA DE CLIENTES E VENDAS
# ============================================================


# ============================================================
# 1. CARREGAMENTO DOS DADOS
# ============================================================

tbc = pd.read_csv("tb_clientes_bruto.csv", sep=";")
tbv = pd.read_csv("tb_vendas_bruto.csv", sep=";")


# ============================================================
# 2. EXPLORAÇÃO DOS DADOS
# ============================================================

# Estrutura dos dados
print(f"Shape tbc: {tbc.shape}")
print(f"Total de elementos tbc: {tbc.size}")
print(f"Dimensões tbc: {tbc.ndim}\n")

print(f"Shape tbv: {tbv.shape}")
print(f"Total de elementos tbv: {tbv.size}")
print(f"Dimensões tbv: {tbv.ndim}\n")


# Categorias
print(f"Tbc: {tbc.columns}\n")
print(f"Tbv: {tbv.columns}\n")


# Verificando valores NaN
print(f"NaN tbc:\n{tbc.isnull().sum()}\n")
print(f"NaN tbv:\n{tbv.isnull().sum()}\n")


# ============================================================
# 3. ANÁLISE BÁSICA DOS CLIENTES
# ============================================================

# Idade média dos clientes
idade_media_tbc = tbc["idade"].mean()

print(f"Idade média dos clientes: {idade_media_tbc:.2f}")


# Maior e menor idade
print(f"\nMaior idade: {tbc['idade'].max()}")
print(f"Menor idade: {tbc['idade'].min()}\n")


# Renda mensal dos clientes
renda_media = tbc["renda_mensal"].mean()

print(f"Renda média dos clientes: {renda_media:.2f}\n")


# Maior e menor renda
print(f"Maior renda: {tbc['renda_mensal'].max()}")
print(f"Menor renda: {tbc['renda_mensal'].min()}\n")


# ============================================================
# 4. CLASSIFICAÇÃO DE RENDA
# ============================================================

# Classificando os clientes por faixa de renda
tbc["class_renda"] = tbc["renda_mensal"].apply(
    lambda i: (
        "Alta renda"
        if i > 5000
        else "Baixa renda"
        if i < 2000
        else "Média renda"
    )
)


# Quantidade de clientes por faixa de renda
qtd_clientes_por_renda = (
    tbc.groupby("class_renda")["renda_mensal"].count()
)

print(
    f"Quantidade de clientes em cada classe de renda:\n"
    f"{qtd_clientes_por_renda}\n"
)


# Classe com mais clientes
print(
    f"Classe que possui mais clientes: "
    f"{qtd_clientes_por_renda.idxmax()}\n"
)


# Renda média de cada classe
media_por_classe = (
    tbc.groupby("class_renda")["renda_mensal"].mean()
)

print(f"Média de renda por classe:\n{media_por_classe}\n")


# ============================================================
# 5. ANÁLISE POR ESTADO
# ============================================================

# Renda média por estado
renda_media_estado = (
    tbc.groupby("sg_uf")["renda_mensal"].mean()
)

print(f"Renda média por estado:\n{renda_media_estado}\n")

print(
    f"Estado com maior renda média: "
    f"{renda_media_estado.idxmax()} - "
    f"renda: {renda_media_estado.max():.2f}"
)

print(
    f"Estado com menor renda média: "
    f"{renda_media_estado.idxmin()} - "
    f"renda: {renda_media_estado.min():.2f}\n"
)


# Quantidade de clientes em cada estado
qtd_clientes_estado = (
    tbc.groupby("sg_uf")["nm_cliente"].count()
)

print(
    f"Quantidade de clientes por estado:\n"
    f"{qtd_clientes_estado}\n"
)


# Estado com mais clientes
print(
    f"Estado com mais clientes: "
    f"{qtd_clientes_estado.idxmax()} - "
    f"quantidade: {qtd_clientes_estado.max()}\n"
)


# ============================================================
# 6. ANÁLISE DAS VENDAS
# ============================================================

# Faturamento total
faturamento_total = tbv["vl_total"].sum()

print(f"Faturamento total: {faturamento_total:.2f}\n")


# Média das vendas
media_faturamento = tbv["vl_total"].mean()

print(f"Média das vendas: {media_faturamento:.2f}")


# Maior e menor venda
maior_venda = tbv["vl_total"].max()
menor_venda = tbv["vl_total"].min()

print(f"Maior venda: {maior_venda:.2f}")
print(f"Menor venda: {menor_venda:.2f}\n")


# Quantidade de vendas
qtd_vendas = tbv["vl_total"].count()

print(f"Quantidade de vendas: {qtd_vendas}\n")


# ============================================================
# 7. ANÁLISE POR CATEGORIA
# ============================================================

# Quantidade de vendas por categoria
qtd_vendas_categoria = (
    tbv.groupby("categoria_prod")["qtd"].sum()
)

print(
    f"Quantidade de vendas por categoria:\n"
    f"{qtd_vendas_categoria}\n"
)

print(
    f"Categoria com maior quantidade de vendas: "
    f"{qtd_vendas_categoria.idxmax()} - "
    f"Vendas: {qtd_vendas_categoria.max()}\n"
)


# Faturamento de cada categoria
faturamento_categoria = (
    tbv.groupby("categoria_prod")["vl_total"].sum()
)

print(
    f"Faturamento de cada categoria:\n"
    f"{faturamento_categoria}\n"
)

print(
    f"Categoria com maior faturamento: "
    f"{faturamento_categoria.idxmax()} - "
    f"Faturamento: {faturamento_categoria.max():.2f}\n"
)


# Média de faturamento por categoria
media_faturamento_categoria = (
    tbv.groupby("categoria_prod")["vl_total"].mean()
)

categoria_maior_media = media_faturamento_categoria.max()

print(
    f"Média de faturamento de cada categoria:\n"
    f"{media_faturamento_categoria}\n"
)

print(
    f"Categoria com maior média: "
    f"{media_faturamento_categoria.idxmax()} - "
    f"Média: {categoria_maior_media:.2f}\n"
)


# ============================================================
# 8. RELAÇÃO ENTRE CLIENTES E VENDAS
# ============================================================

# Relacionando clientes e vendas
clientes_vendas = pd.merge(
    tbc,
    tbv,
    left_on="id_cli",
    right_on="cliente_id"
)


# Quanto cada cliente gastou
total_por_cliente = (
    clientes_vendas
    .groupby(["id_cli", "nm_cliente"])["vl_total"]
    .sum()
)

print(
    f"\nTotal gasto por cada cliente:\n"
    f"{total_por_cliente}\n"
)


# Total gasto por cliente
total_por_cliente = (
    clientes_vendas
    .groupby("id_cli")["vl_total"]
    .sum()
    .reset_index(name="total_gasto_cliente")
)


# Top 10 clientes que mais gastaram
top10_clientes = (
    total_por_cliente
    .nlargest(10, "total_gasto_cliente")
)


# Quantidade de compras por cliente
qtd_por_cliente = (
    clientes_vendas
    .groupby("id_cli")["qtd"]
    .sum()
    .reset_index(name="total_compras")
)


# Top 10 clientes que mais compraram
top10_clientes_compras = (
    qtd_por_cliente
    .nlargest(10, "total_compras")
)


print(f"Top 10 clientes:\n{top10_clientes}\n")

print(
    f"Clientes que realizaram mais compras:\n"
    f"{top10_clientes_compras}\n"
)


# Clientes que realizaram apenas uma compra
clientes_com_uma_compra = (
    total_por_cliente[total_por_cliente == 1]
)

print(
    f"Clientes que só fizeram 1 compra:\n"
    f"{clientes_com_uma_compra}\n"
)


# ============================================================
# 9. RENDA x CONSUMO
# ============================================================

# Cliente que mais gastou
cliente_mais_gastou = (
    qtd_por_cliente.nlargest(1, "total_compras")
)

nome_cliente_mais_gastou = tbc.loc[
    tbc["id_cli"] == cliente_mais_gastou["id_cli"].iloc[0],
    "nm_cliente"
]

renda_cliente_mais_gastou = tbc.loc[
    tbc["id_cli"] == cliente_mais_gastou["id_cli"].iloc[0],
    "renda_mensal"
]

valor_gasto_cliente_mais_gastou = (
    total_por_cliente.nlargest(1, "total_gasto_cliente")
)


# Cliente que menos gastou
cliente_menos_gastou = (
    qtd_por_cliente.nsmallest(1, "total_compras")
)

nome_cliente_menos_gastou = tbc.loc[
    tbc["id_cli"] == cliente_menos_gastou["id_cli"].iloc[0],
    "nm_cliente"
]

renda_cliente_menos_gastou = tbc.loc[
    tbc["id_cli"] == cliente_menos_gastou["id_cli"].iloc[0],
    "renda_mensal"
]

valor_gasto_cliente_menos_gastou = (
    total_por_cliente.nsmallest(1, "total_gasto_cliente")
)


print(f"Cliente que mais gastou: {nome_cliente_mais_gastou.iloc[0]}")
print(f"Renda: {renda_cliente_mais_gastou.iloc[0]:.2f}")
print(
    f"Valor gasto: "
    f"{valor_gasto_cliente_mais_gastou['total_gasto_cliente'].iloc[0]:.2f}\n"
)

print(f"Cliente que menos gastou: {nome_cliente_menos_gastou.iloc[0]}")
print(f"Renda: {renda_cliente_menos_gastou.iloc[0]:.2f}")
print(
    f"Valor gasto: "
    f"{valor_gasto_cliente_menos_gastou['total_gasto_cliente'].iloc[0]:.2f}\n"
)


# Clientes com maior renda tendem a gastar mais?
# Sim, conforme a análise, o cliente com maior renda
# gastou mais em relação ao cliente com menor renda.


# ============================================================
# 10. ESTATÍSTICA COM NUMPY
# ============================================================

# Valores das vendas
qtd = tbv["qtd"].to_numpy()
preço = tbv["vl_total"].to_numpy()


# Média dos valores de venda
media_vendas = np.nansum(qtd * preço) / len(qtd)

print(f"Média das vendas: {media_vendas:.2f}")


# Mediana dos valores de venda
mediana_vendas = np.nanmedian(preço)

print(f"Mediana: {mediana_vendas:.2f}\n")


# Maior e menor valor de venda
maior_preço = np.nanmax(preço)
menor_preço = np.nanmin(preço)

print(f"Maior preço: {maior_preço:.2f}")
print(f"Menor preço: {menor_preço:.2f}\n")


# Amplitude dos valores
amplitude_preços = maior_preço - menor_preço

print(f"Amplitude dos valores: {amplitude_preços:.2f}\n")


# Diferença entre média e mediana
comparando_media_mediana = media_vendas - mediana_vendas

print(
    f"Diferença entre média e mediana: "
    f"{comparando_media_mediana:.2f}\n"
)


# As médias são parecidas?
# Não, existe uma diferença de 89.


# Existem valores muito distantes?
# Sim. Existem valores muito distantes da maior parte dos dados,
# indicando uma grande dispersão e a possível presença de outliers.


# A média representa bem os dados?
# Não, porque existem valores muito altos enquanto outros são
# muito baixos. Dessa forma, os valores extremos podem influenciar
# a média.


# ============================================================
# 11. GRÁFICOS — MATPLOTLIB
# ============================================================

# Quantidade de clientes por estado
estados_count_clientes = (
    tbc.groupby("sg_uf")["nm_cliente"].count()
)

estados = estados_count_clientes.index
clientes = estados_count_clientes.values

plt.plot(estados, clientes)

plt.title("Quantidade de Clientes por Estado")
plt.xlabel("Estados")
plt.ylabel("Clientes")

plt.show()


# Renda média por estado
renda_por_cliente = renda_media_estado.values

plt.plot(estados, renda_por_cliente)

plt.title("Renda Média por Estado")
plt.xlabel("Estados")
plt.ylabel("Renda Média")

plt.show()


# Faturamento por categoria
valor_por_categoria = faturamento_categoria.values
categorias = faturamento_categoria.index

plt.plot(categorias, valor_por_categoria)

plt.title("Faturamento de Cada Categoria")
plt.xlabel("Categorias")
plt.ylabel("Faturamento")

plt.show()


# Top 10 clientes que mais gastaram
top10_id = top10_clientes["id_cli"].values
top10_valor = top10_clientes["total_gasto_cliente"].values

nomes_top10 = []

for i in top10_id:
    nomes_top10.append(
        tbc.loc[
            tbc["id_cli"] == i,
            "nm_cliente"
        ].iloc[0]
    )


plt.figure(figsize=(10, 6))

plt.bar(nomes_top10, top10_valor)

plt.title("Top 10 Clientes que Mais Gastaram")
plt.xlabel("Clientes")
plt.ylabel("Valor Gasto")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()


# ============================================================
# 12. ANÁLISE FINAL
# ============================================================

# Estado que possui o melhor perfil de renda
estado_perfil_renda = renda_media_estado.idxmax()

print(
    f"Estado que possui o melhor perfil de renda: "
    f"{estado_perfil_renda}\n"
)


# Estado que possui mais clientes
estado_mais_clientes = qtd_clientes_estado.idxmax()

print(
    f"Estado com mais clientes: "
    f"{estado_mais_clientes}\n"
)


# Categoria que gera mais dinheiro
categoria_mais_lucro = faturamento_categoria.idxmax()

print(
    f"Categoria de produto que gera mais faturamento: "
    f"{categoria_mais_lucro}"
)


# Categoria que possui mais vendas
categoria_mais_vendas = qtd_vendas_categoria.idxmax()

print(
    f"Categoria de produto com mais vendas: "
    f"{categoria_mais_vendas}\n"
)


# Principais clientes
print(f"Principais clientes: {nomes_top10}\n")


# Clientes de maior renda realmente gastam mais?
# Sim.


# Faixa de renda mais importante para a empresa
faixa_mais_importante = tbc["class_renda"].idxmax()

print(
    f"Faixa de renda mais importante: "
    f"{faixa_mais_importante}\n"
)


# Estado com muitos clientes, mas baixo faturamento
# Sim. Por exemplo, a Bahia, que possui uma renda média de
# 4952 e 104 clientes, quantidade acima da média.


# Estado com poucos clientes, mas alto faturamento
# Sim. Por exemplo, São Paulo, que possui 23 clientes
# e gera 6468 de faturamento.


# Categoria que vende muito, mas gera pouco dinheiro
# Sim. Bebidas possui a terceira maior quantidade de vendas
# e é a categoria que gera menos dinheiro.


# Principal recomendação
# A empresa deve priorizar os estados e categorias que apresentam
# maior potencial de faturamento, principalmente São Paulo, que
# possui poucos clientes, mas gera um faturamento elevado.
#
# Também seria interessante analisar a categoria de bebidas,
# pois possui uma quantidade significativa de vendas, mas
# apresenta baixo faturamento.
#
# Isso pode indicar uma oportunidade de aumentar o valor médio
# das vendas dessa categoria.


# ============================================================
# FIM DO PROJETO :)
# ============================================================





