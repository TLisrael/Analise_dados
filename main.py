import matplotlib.pyplot as plt
import pandas as pd

# Carregar o arquivo CSV
dados = pd.read_csv('microdados_enem_2005/DADOS/MICRODADOS_ENEM_2005.csv', sep=';', encoding='ISO-8859-1')

# Exibir as primeiras linhas dos dados
dados.head()

# Selecionar colunas específicas
colunas_selecionadas = ['TP_FAIXA_ETARIA','NU_ANO', 'TP_SEXO',
       'CO_MUNICIPIO_RESIDENCIA', 'NO_MUNICIPIO_RESIDENCIA',
       'CO_UF_RESIDENCIA', 'SG_UF_RESIDENCIA', 'TP_ST_CONCLUSAO',
       'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC',
       'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC',
       'TP_PRESENCA', 'CO_PROVA', 'VL_PERC_COMP1', 'VL_PERC_COMP2',
       'VL_PERC_COMP3', 'VL_PERC_COMP4', 'VL_PERC_COMP5',
       'NU_NOTA_OBJETIVA', 'TX_RESPOSTAS_OBJETIVA',
       'TX_GABARITO_OBJETIVA', 'TP_STATUS_REDACAO', 'NU_NOTA_COMP1',
       'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5',
       'NU_NOTA_REDACAO', 'IN_QSE']

dados_selecionados = dados.filter(items=colunas_selecionadas)

# Exibir a coluna de municípios de residência e suas contagens
coluna_municipio = dados_selecionados['NO_MUNICIPIO_RESIDENCIA']
coluna_municipio.value_counts().sort_index()

# Exibir a coluna de faixa etária e suas contagens
coluna_faixa_etaria = dados_selecionados['TP_FAIXA_ETARIA']
coluna_faixa_etaria.value_counts().sort_index()

# Gerar um histograma da coluna de faixa etária
coluna_faixa_etaria.hist(bins=30)

# Exibir a coluna de estados de residência e suas contagens
coluna_estado = dados_selecionados['SG_UF_RESIDENCIA']
coluna_estado.value_counts()

# Gerar um histograma da coluna de estados de residência
coluna_estado.hist(bins=27)

# Exibir a coluna de sexo e suas contagens
coluna_sexo = dados_selecionados['TP_SEXO']
coluna_sexo.value_counts()

# Calcular a distribuição percentual do sexo
distribuicaoSexo = coluna_sexo.value_counts()
porcentagemSexo = [100*x/distribuicaoSexo.sum() for x in distribuicaoSexo]

# Exibir a porcentagem de distribuição do sexo
porcentagemSexo
