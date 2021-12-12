import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from scipy.stats import normaltest

dataset = pd.read_csv("datasets/clean_df.csv")
dataset.drop("Unnamed: 0", axis=1, inplace=True)

plt.scatter(dataset["review_score"],dataset["days_late"],marker=".")
plt.title("Gráfico de Dispersão entre nota do usuário e quantidade de dias de atraso")
plt.ylabel("Dias de Atraso")
plt.xlabel("Nota do Usuário")
plt.show()