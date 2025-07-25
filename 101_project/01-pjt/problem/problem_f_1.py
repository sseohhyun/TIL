import pandas as pd 

df = pd.read_csv("movie_details.csv")

df['profit_rate'] = df['revenue']/df['budget']
max_rate = max(df['profit_rate'])

max_index = df['profit_rate'].idxmax()

print(f"수익률이 가장 높은 영화의 id는 {df.loc[max_index, 'id']}입니다.")