import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
df = sns.load_dataset("iris")
# Display first few rows
df.head()
# Checking for missing values
print(df.isnull().sum())
# Summary statistics
print(df.describe())
# Check unique species
print(df["species"].unique())
# Pairplot to visualize relationships
sns.pairplot(df,hue="species")
plt.show()
# Boxplot for feature comparison
sns.boxplot(x="species",y="sepal_length",data=df)
plt.show()
