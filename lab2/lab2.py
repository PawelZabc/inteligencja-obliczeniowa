import pandas as pd
import math


df = pd.read_csv("iris_with_errors.csv")

# print(df.values)
regex = r'^(\d{4})'
# extr = df['sepal.length'].str.extract(r'^(\d{4})', expand=False)
# extr.head()
# def check_value(x):
#     if x is not float:
#         return 1000
#     return 1000

# df.apply(check_value, axis=1)


#   print(type(value ))
#   print(type(value)!=type(0.0))
#   print(value)
names = ['Versicolor','Setosa','Virginica']
change2mean=[]

means = {
    'sepal.width':0,
    'sepal.length':0,
    'petal.length':0,
    'petal.width':0
}

print(df.isnull().sum())
for column in df.columns:
    print(f'Unique values in {column}:')
    print(df[column].unique())
    print()

for name in df.columns:
    if name != 'variety':
        means[name] = 0
        for x in df.index:
            value = df.loc[x, name]
            try:
                if math.isnan(float(value)):
                    change2mean.append((x,name))
                else:
                    if float(value) <=0 or float(value)>=15:
                        change2mean.append((x,name))
                    else: 
                        df.loc[x, name] = float(value)   
                        means[name]+=float(value)
            except:
                change2mean.append((x,name))
    else:
        for x in df.index:
            value = df.loc[x, name]
            if value not in names:
                df.loc[x, name] = "error"

for i in change2mean:
    
    x,name = i
    df.loc[x, name] = means[name]
    print(x,name)

print(means)




print(df.values)
# (df.line_race != 10)
#jvfwnpn