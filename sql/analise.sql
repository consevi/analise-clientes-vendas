-- ============================================================
-- PROJETO: ANÁLISE ESTRATÉGICA DE CLIENTES E VENDAS
-- ============================================================


-- ============================================================
-- 1. EXPLORAÇÃO DOS CLIENTES
-- ============================================================

Quantidade de clientes:
SELECT 
COUNT(id_cli) as qtd_cli
FROM tb_clientes_bruto 
  
Média de idade e renda:
SELECT 
ROUND(AVG(idade), 2) as media_idades,
ROUND(AVG(renda_mensal ), 2) as media_renda
FROM tb_clientes_bruto 

Quantidade de clientes por estado:
SELECT 
COUNT(id_cli) as qtd_cli,
UPPER(sg_uf)
FROM tb_clientes_bruto 
GROUP BY sg_uf

-- ============================================================
-- 2. ANÁLISE POR ESTADO
-- ============================================================
  
Renda média por estado:
SELECT 
ROUND(AVG(renda_mensal ), 2) as qtd_cli,
UPPER(sg_uf)
FROM tb_clientes_bruto 
GROUP BY sg_uf

Estado com maior e menor renda:
SELECT
    MAX(media_renda) AS est_maior_renda,
    MIN(media_renda) AS est_menor_renda
FROM (
    SELECT
        sg_uf,
        ROUND(AVG(renda_mensal), 2) AS media_renda
    FROM tb_clientes_bruto
    GROUP BY sg_uf
) AS estados;

Estados com quantidade de clientes a cima da média:
SELECT 
UPPER(sg_uf),
COUNT(id_cli) as qtd_clientes
FROM tb_clientes_bruto tcb 
GROUP BY sg_uf
HAVING COUNT(id_cli) > (
	SELECT ROUND(AVG(qtd_clientes), 2)
	FROM	 (
	  SELECT COUNT(id_cli) AS qtd_clientes
       FROM tb_clientes_bruto
        GROUP BY sg_uf
    ) AS estados
);

-- ============================================================
-- 3. ANÁLISE DAS VENDAS
-- ============================================================
Quantidade de vendas e faturamento:
SELECT 	
SUM(qtd) as qtd_vendas,
SUM(vl_total) as faturamento
FROM tb_vendas_bruto 

Média das vendas, maior e menor venda:
SELECT 
ROUND(AVG(vl_total), 2) as vl_media_vendas,
MAX(vl_total) as maior_vendas,
MIN(vl_total) as menor_vendas
FROM tb_vendas_bruto 

Faturamento de cada categoria:
SELECT 
SUM(vl_total) as faturamento,
categoria_prod
FROM tb_vendas_bruto 
GROUP BY categoria_prod
ORDER BY categoria_prod ASC

Categoria com mais produtos vendidos:
SELECT 
SUM(qtd) as qtd_prod,
categoria_prod 
FROM tb_vendas_bruto 
GROUP BY categoria_prod
ORDER BY categoria_prod DESC
LIMIT 1;

Maior valor médio por venda:
SELECT 
ROUND(AVG(vl_total), 2) as media_preço,
categoria_prod 
FROM tb_vendas_bruto 
GROUP BY categoria_prod
ORDER BY categoria_prod DESC
LIMIT 1;

-- ============================================================
-- 4. JOIN — CLIENTES + VENDAS
-- ============================================================

Perfil dos clientes:
SELECT 
    tbc.nm_cliente AS nome,
    tbc.sg_uf AS estado,
    SUM(tbv.vl_total) AS total_gasto
FROM tb_clientes_bruto AS tbc
JOIN tb_vendas_bruto AS tbv
    ON tbc.id_cli = tbv.cliente_id
GROUP BY 
    tbc.nm_cliente,
    tbc.sg_uf;

Clientes que mais gastaram:
SELECT 
    tbc.nm_cliente AS nome,
    tbc.sg_uf AS estado,
    SUM(tbv.vl_total) AS total_gasto
FROM tb_clientes_bruto AS tbc
JOIN tb_vendas_bruto AS tbv
    ON tbc.id_cli = tbv.cliente_id
GROUP BY 
    tbc.nm_cliente,
    tbc.sg_uf
ORDER BY total_gasto DESC
LIMIT 10;

Clientes que realizaram mais compras:
SELECT 
    tbc.nm_cliente AS nome,
    tbc.sg_uf AS estado,
    SUM(tbv.qtd) AS qtd_compras
FROM tb_clientes_bruto AS tbc
JOIN tb_vendas_bruto AS tbv
    ON tbc.id_cli = tbv.cliente_id
GROUP BY 
    tbc.nm_cliente,
    tbc.sg_uf
ORDER BY qtd_compras DESC
LIMIT 10;

-- ============================================================
-- 5. RENDA × CONSUMO
-- ============================================================




-- ============================================================
-- 6. ANÁLISE AVANÇADA
-- ============================================================


