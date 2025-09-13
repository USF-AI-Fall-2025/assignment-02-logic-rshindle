import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from DataInvestigator import DataInvestigator

if __name__ == "__main__":
    df = pd.read_csv('gallstone.csv')
    di = DataInvestigator(df)
    print(di.baseline(1))

    #print(df.head())
    #print(df.info())

    testCols = ["Lean Mass (LM) (%)", "Muscle Mass (MM)", "Bone Mass (BM)", "Obesity (%)", "Total Fat Content (TFC)"]

    for col in testCols:
        sns.boxplot(x="Gender", y=col, data=df)
        plt.title(f"Boxplot of {col} by Gender")
        plt.show()

    print(df.groupby("Gender")[testCols].mean())

    print()

    sns.histplot(df["Glucose"], kde=True, bins=100)
    plt.title("Histogram of Glucose")
    plt.show()

    sns.boxplot(x=df["Glucose"])
    plt.title("Boxplot of Glucose")
    plt.show()

    print("Glucose data:\n",df["Glucose"].describe())

    mean = df['Glucose'].mean()
    std = df['Glucose'].std()

    lowerBound = mean - 2 * std
    upperBound = mean + 2 * std

    outliers = df[(df['Glucose'] < lowerBound) | (df['Glucose'] > upperBound)]
    print("Outliers:")
    print(outliers['Glucose'].values)