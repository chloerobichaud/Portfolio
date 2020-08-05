```python
#Signal min, max, median on DataCamp
print(df_clean['dry_bulb_faren'].median())
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].median())
daily_mean_2011 = df_clean.resample('D').mean()
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values
daily_climate = df_climate.resample('D').mean()
daily_temp_climate = daily_climate.reset_index()['Temperature']
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())
```
