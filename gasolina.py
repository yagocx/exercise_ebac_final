import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

gas_df = pd.read_csv('gasolina.csv', sep=',')
gas_df.head()

graph = sns.barplot(data=gas_df, x='dia', y='venda')

# Adicionar rótulos ao gráfico
plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.show()
plt.gcf().savefig(fname='gasolina.png', bbox_inches='tight')