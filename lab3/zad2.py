import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris1 1.csv")
# from sklearn.model_selection import train_test_split
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['variety'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)





from sklearn import tree
# X = [[0, 0], [1, 1]]
# Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(test_inputs, test_classes)
print(df.sort_values('variety').to_string())
print(df.sort_values('petal.length').to_string())

print(f"{clf.score(test_inputs,test_classes)*100}%")
plt.figure(figsize=(10,10))
tree.plot_tree(clf,feature_names=["sl","sw","pl","pw"],class_names=clf.classes_)

plt.show()

# def classify_iris(sl, sw, pl, pw):
#  if pw <1.0:#0.6
#     return("Setosa")
#  elif pl >= 4.8:
#     return("Virginica")
#  else:
#     return("Versicolor")
 
# # print(test_set[0,0])

# good_predictions = 0
# len = .shape[0]
# for i in range(len):
#     if classify_iris(test_set[i,0],test_set[i,1],test_set[i,2],test_set[i,3]) == test_set[i,4]:
#         good_predictions = good_predictions + 1
# print(good_predictions)
# print(good_predictions/len*100, "%")
