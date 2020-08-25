df_simon = df.groupby('simon')
df_flankers = df.groupby('flankers')
df_flankers[['rt']].plot(kind='box')
df_simon[['rt']].plot(kind = 'box')