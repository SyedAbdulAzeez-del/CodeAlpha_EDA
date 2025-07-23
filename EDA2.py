# EDA on Top 50 Highest-Grossing Films

# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset
df = pd.read_csv("C:/Task-1/Task-1/top_50_highest_grossing_movies.csv")
print("\n✅ First 5 rows of the dataset:")
print(df.head())

# Step 3: Data structure and types
print("\n✅ Dataset Info:")
print(df.info())

# Step 4: Check for missing values
print("\n✅ Missing values:")
print(df.isnull().sum())

# Step 5: Clean the 'Worldwide Gross' column
# Remove '$' and commas, then convert to float
df['Worldwide Gross'] = df['Worldwide Gross'].replace('[\$,]', '', regex=True).astype(float)

# Step 6: Summary statistics
print("\n✅ Summary Statistics:")
print(df.describe())

# Step 7: Top 10 highest-grossing movies
top10 = df.sort_values('Worldwide Gross', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x='Worldwide Gross', y='Title', palette='viridis')
plt.title("Top 10 Highest Grossing Movies")
plt.xlabel("Gross (in USD)")
plt.tight_layout()
plt.show()

# Step 8: Gross by year
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Year', y='Worldwide Gross', palette='coolwarm')
plt.title("Top Grossing Movies by Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 9: Frequency of top movies by year
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Year', order=df['Year'].value_counts().index, palette='mako')
plt.title("Number of Top-Grossing Movies per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 10: Save cleaned data
cleaned_path = "C:\Task-1\cleaned_top_50_movies.csv"
df.to_csv(cleaned_path, index=False)
print(f"\n✅ Cleaned data saved to {cleaned_path}")