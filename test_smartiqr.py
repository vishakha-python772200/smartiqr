from smartiqr import analyze_iqr
import pandas as pd

df=pd.read_csv(r"C:\Users\badgu\Downloads\customer_profile_noisy.csv")
result=analyze_iqr(df['income'])
print(result)


