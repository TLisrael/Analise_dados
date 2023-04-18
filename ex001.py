# Importar as bibliotecas necessárias
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
monthly_overtime = [10, 12, 12, 14, 15, 16, 16, 30, 19, 20, 20, 21, 24, 24, 25, 28, 18]

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(monthly_overtime, columns=['valores'])

# Calcular a amplitude total dos valores
at = df['valores'].max() - df['valores'].min()

# Calcular o número de classes usando a raiz quadrada do tamanho do DataFrame
num_classes = int(sqrt(len(df)))

# Calcular o intervalo de classe
intervalo = int(at / num_classes)

# Adicionar uma nova coluna ao DataFrame com os intervalos de classe
df['Intervalo de classe'] = pd.cut(df['valores'], bins=range(df['valores'].min(), df['valores'].max() + intervalo, intervalo), right=False)

# Calcular a frequência absoluta de cada classe
class_frequencies = df['Intervalo de classe'].value_counts(sort=False).reset_index()
class_frequencies.columns = ['Intervalo de classe', 'Frequência absoluta']

# Calcular a frequência relativa de cada classe
class_frequencies['Frequência Relativa'] = class_frequencies['Frequência absoluta'] / len(df)

# Calcular a frequência acumulada de cada classe
class_frequencies['Frequência Acumulada'] = class_frequencies['Frequência absoluta'].cumsum()

# Preparar os dados para o gráfico de barras
grafico_df = pd.DataFrame({'Frequência Absoluta': class_frequencies['Frequência absoluta']})

# Plotar o gráfico de barras
grafico_df.plot(kind='bar', legend=False)

# Adicionar título e rótulos aos eixos do gráfico
plt.title('Distribuição de Frequência - Frequência Absoluta')
plt.xlabel('Intervalos de Classe')
plt.ylabel('Frequência Absoluta')
plt.xticks(ticks=range(len(class_frequencies)), labels=class_frequencies['Intervalo de classe'])

# Exibir o gráfico
plt.show()
