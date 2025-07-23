
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Task-1/Task-1/top_50_highest_grossing_movies.csv")
print("\n✅ First 5 rows of the dataset:")
print(df.head())

print("\n✅ Dataset Info:")
print(df.info())

print("\n✅ Missing values:")
print(df.isnull().sum())

df['Worldwide Gross'] = df['Worldwide Gross'].replace('[\$,]', '', regex=True).astype(float)

print("\n✅ Summary Statistics:")
print(df.describe())


top10 = df.sort_values('Worldwide Gross', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x='Worldwide Gross', y='Title', palette='viridis')
plt.title("Top 10 Highest Grossing Movies")
plt.xlabel("Gross (in USD)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Year', y='Worldwide Gross', palette='coolwarm')
plt.title("Top Grossing Movies by Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Year', order=df['Year'].value_counts().index, palette='mako')
plt.title("Number of Top-Grossing Movies per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

cleaned_path = "C:\Task-1\cleaned_top_50_movies.csv"
df.to_csv(cleaned_path, index=False)
print(f"\n✅ Cleaned data saved to {cleaned_path}")
