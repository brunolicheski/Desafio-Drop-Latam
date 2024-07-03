import pandas as pd

df = pd.read_csv(r'C:\Users\Bruno\Desktop\Desafio Drop Latam\impact-report.csv')

print(df.head())
print(df.columns)


df_aprovados = df[df['Status'] == 'Approved']
eventos_relevantes = df_aprovados[df_aprovados['Event Type'].isin(['Free Trial API', 'Paid Trial API', 'Online Sale API', 'POS Pro Sale API'])]


faturamento_atual = eventos_relevantes[eventos_relevantes['Event Type'].isin(['Online Sale API', 'POS Pro Sale API'])].groupby('Sub Id 2')['Action Earnings'].sum()


free_trial_revenue = eventos_relevantes[eventos_relevantes['Event Type'] == 'Free Trial API'].groupby('Sub Id 2')['Action Earnings'].sum()
paid_trial_revenue = eventos_relevantes[eventos_relevantes['Event Type'] == 'Paid Trial API'].groupby('Sub Id 2')['Action Earnings'].sum()


relatorio = pd.DataFrame({
    'Faturamento Atual': faturamento_atual,
    'Previsão Free Trial': free_trial_revenue,
    'Previsão Paid Trial': paid_trial_revenue
}).fillna(0)  # Preencher valores ausentes com 0



relatorio.to_csv(r'C:\Users\Bruno\Desktop\Desafio Drop Latam\relatorio_por_canal.csv', index=True)

print("Relatório gerado e salvo como 'relatorio_por_canal.csv'")

