import pandas as pd

df = pd.read_csv('iris_with_errors.csv')


numeric_columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']

print("\nTypy danych przed poprawkami:")
print(df.dtypes)

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

print("\nTypy danych po poprawkach:")
print(df.dtypes)

missing_data = df.isnull().sum()
print("Brakujące dane w każdej kolumnie:")
print(missing_data)

print("\nDane przed poprawkami numerycznymi:")
print(df[numeric_columns].describe())


for column in numeric_columns:
    mean_value = df[column].mean()
    df.fillna({column: mean_value}, inplace=True)

for column in numeric_columns:
    mean_value = df[column].mean()
    df[column] = df[column].apply(lambda x: mean_value if x <= 0 or x >= 15 else x)

print("\nDane po poprawkach numerycznych:")
print(df[numeric_columns].describe())

print("Gatunki przed poprawkami:")
print(df['variety'].unique())

df['variety'] = df['variety'].replace({
    'setosa': 'Setosa',
    'versicolor': 'Versicolor',
    'virginica': 'Virginica',
    'Versicolour':'Versicolor'
})

df = df[df['variety'].isin(['Setosa', 'Versicolor', 'Virginica'])]

print("\nGatunki po poprawkach:")
print(df['variety'].unique())


print("\nPoprawiona baza danych:")
print(df)
