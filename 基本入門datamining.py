# -*- coding: utf-8 -*-
"""基本入門datamining.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TUl8uriOkhclVK_aIpR3FOCT2rRikazn
"""

import pandas as pd
import numpy as np
#import matplotlib as ma
import scipy as sc
import matplotlib.pyplot as plt
import seaborn as sns

t1 = 10, 20
# it can hold different types of data
t2 = 10, 'hello world'

print(type(t1))
print(t1)
print(t2)

r1 = range(10)
r2 = range(5, 50, 5)

print(type(r1))
print(r1)
print(r2)

str1 = 'hello python'
str2 = str1
# str2[0] = 'y'
# a = a + b could be written as a += b
str2 += ' journey'
print(str2 is str1)

print(str1)
result = str2.split(' ')
print(result)
result_back = '***'.join(result)
print(result_back)

str1 = 'hello world'
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mind the stop
arr2 = arr1[0:5]
# -1 represent the last element
arr3 = arr1[0:-1:2]
# you can ignore the args...
arr4 = arr1[:]
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr4 is arr1)
print(str1[5:])
print(arr1[:-1])

arr1 = [2, 4, 6, 8, 10]
str1 = 'hello python'

for i in range(10):
    print(i)
print('***\n')

for i in range(len(arr1)):
    print(arr1[i])
print('***\n')

for i in arr1:
    print(i)
print('***\n')

for i in str1:
    print(i)
print('***\n')

for i in arr1:
     i += 1
     print(i)
print('***\n')

arr1 = []

for i in range(10):
    arr1.append(i)

print(arr1)

# in-place construction
arr1 = [i for i in range(10)]

print(arr1)

# in-place construction
arr1 = [i for i in range(10)]

# you can use if to filter the elements
arr2 = [x for x in arr1 if x % 2 == 0]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2]

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)

import time

arr1 = []
s = time.time()
for i in range(int(1e+6)):
    arr1.append(i)
print('took {} secs'.format(round(time.time() - s, 3)))

s = time.time()
arr2 = [i for i in range(int(1e+6))]
print('took {} secs'.format(round(time.time() - s, 3)))

comp = (i for i in range(10))
print(comp)
print(type(comp))

arr1 = list(comp)
arr2 = list(comp)
arr3 = [comp]
print(arr1)
print(arr2)
print(arr3)

arr1 = [i for i in range(1,21) if i % 2 == 1]
arr2 = [i for i in range(1,21) if i % 2 == 0]
print(arr1)
print(arr2)

arr3 = [i for i in range(1,21,2)]
arr4 = [i for i in range(2,21,2)]
print(arr3)
print(arr4)

for i in range(len(arr1)):
    print(arr1[i], '<--->', arr2[i])

arr1 = [i for i in range(10)]
arr2 = [i for i in range(5, 15)]

for t in zip(arr1, arr2):
    print(t[0], t[1])
print('*' * 10)

for i, j in zip(arr1, arr2):
    print(i, j, sep = ' <---> ')
print('*' * 10)

my_obj = pd.Series([4, 7, -5, 3])

print(my_obj.values)
print(my_obj.index)

my_obj2 = pd.Series([8,9,10,11], index=['a','b','c','d'])
print(my_obj2.values)
print(my_obj2.index)
#my_obj2['a'] 找8
'a' in my_obj2 #確認8是否在裏頭

dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 }
my_obj3 = pd.Series(dic_data)
my_obj3

registration = [True,False,True,True]
registration = pd.Series(registration)
print(registration.index)
registration

dictionary = {'A':'an animal',
              'B':'a color',
              'C':'a fruit'}
dictionary = pd.Series(dictionary)
dictionary

data = {'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day':[11,23,8,3,11],
       'name': ['Bob', 'Nancy','Amy','Elsa','Jack']}
myframe = pd.DataFrame(data)
myframe

myframe2 = pd.DataFrame(data,columns=['name','year', 'month', 'day'])
myframe2

myframe3 = pd.DataFrame(data,columns=['name','year', 'month', 'day','luckynumber'])
luckynumber = ['3','2','1','7','8']
luckynumber = pd.Series(luckynumber)
myframe3['luckynumber'] = luckynumber
myframe3

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
# 建立數據
data = np.round(np.random.randn(4, 6), 1)
print(data)
data[:, ::2] *= 10
print(data)
data += 37
print(data)
 #建立 DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data

health_data['Guido', 'HR']

health_data.iloc[:2, :2]

x = [[1, 2],
     [3, 4]]
print(x)
#np.concatenate([x, x], axis=0)

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print(ser1)
pd.concat([ser1, ser2])

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print(df1, df2)
df3 = pd.merge(df1, df2)
df3


df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
print(pd.merge(df3,df4))

df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})
print(pd.merge(df1, df5))

df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
print(pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1))

df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                   columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
print(pd.merge(df6, df7, how=inner)

from google.colab import files
uploaded = files.upload()
import io
df = pd.read_csv(io.BytesIO(uploaded['NBA_season1718_salary.csv']))

df = pd.read_csv('NBA_season1718_salary.csv')

#df.insert(3,column="sport",value="Basketball")
df.dropna()
df = df.dropna()
df.columns = ['cod', 'player', 'team', 'salary']
del df['cod']
df.head()

#df.drop(labels=['team','salary'], axis="columns")
#axis=1跟axis="columns"是一樣的！axis=0則是和asxis = "row"一樣。

df.sort_values('salary',ascending= False)

df1 = pd.DataFrame(np.random.randn(4,2),index=['a', 'a', 'b', 'b']) #隨機產生2維矩陣(numpy為產生矩陣的套件)
df1

df1.ix['b']

filter = df['salary']> 33000000
df[filter]
mask = df["team"].notnull()
df[mask]

df.set_index("team" , inplace=True) #選取row資料
df.loc[["GSW","CLE","LAL"]]

df.reset_index(inplace=True)

sector = df.groupby("team")
sector.get_group("GSW").head
#sector.size()

df.groupby('team').sum()

df["player"].str.split(":").head()

"""# 資料視覺化

## 靜態視覺化
"""

from sklearn.datasets import make_blobs
X, y = make_blobs(150, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X, y);

rng = np.random.RandomState(0)
Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
ynew = model.predict(Xnew)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
lim = plt.axis()
plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=20, cmap='RdBu', alpha=0.1)
plt.axis(lim);

yprob = model.predict_proba(Xnew)
yprob[-8:].round(2)

arr = np.arange(10)
arr[5]
arr[5:8]

arr[5:9] = 7

arr

myarr = np.arange(10)
slice = myarr[5:8]
myarr[5:8] = 7
slice[1] = 87
myarr

x = np.arange(4)
x2 = x.reshape(4,1)
print(x2)

y = np.ones(5)
print(y)

x2 + y

years = [1000,1500,1600,1700,1750,1800,1850,
        1900,1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]

pops = [200,400,458,580,662,791,1000,
        1262,1650,2525,2758,3018,3322,3682,
        4061,4440,4853,5310,6520,
        6930,7349]

plt.plot(years,pops)
plt.show()

years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
pops = [2.5,2.7,3,3.3,3.6,4.0,
        4.4,4.8,5.3,6.1,6.5,6.9,7.3]
deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]
#plt.plot(years,pops,color=(255/255,100/255,100/255))
#plt.plot(years,deaths,'--', color=(100/255,100/255,255/255))
plt.title("Population Growth") # title
plt.ylabel("Population in billions") # y label
plt.xlabel("Population growth by year") # x label
lines = plt.plot(years,pops,years,deaths) #顯示multilines 全部寫在一起放進lines變數
plt.grid(True)
plt.setp(lines,marker = "o") 

plt.show()

x = np.arange(0, 1.0, 0.01)
y1 = np.sin(4*np.pi*x)
y2 = np.sin(2*np.pi*x)
lines = plt.plot(x, y1, x, y2)
l1, l2 = lines
plt.setp(lines, linestyle='--')      
plt.show()

labels = 'A','B','C','D','E','F'
size = [33,52,12,17,62,48]
plt.pie(size , labels = labels,autopct='%1.1f%%') #autopct顯示百分比
plt.axis('equal')
plt.show()

separated = (.1,0,0,0,0,0)
plt.pie(size , labels = labels,autopct='%1.1f%%',explode=separated)

data = {'names':['a','b','c','d','e'],
        'jan':[133,122,101,104,320],
        'feb':[122,132,144,98,62],
        'march':[64,99,32,12,65] }
df1 = pd.DataFrame(data,columns=['names','jan','feb','march'])
print(df1)

df1['total'] = df1['jan']+ df1['feb']+df1['march']
colors = [(1,.4,.4),(1,.6,1),(.5,.3,1),(.7,.7,.2),(.6,.2,.6)]

plt.pie( df1['total'] ,
    labels = df1['names'],
    colors = colors,
    autopct='%1.1f%%',
    ) 
plt.axis('equal') 
plt.show()

col_count = 3
bar_width = 0.2
A_scores = (553,536,548)
B_scores = (518,523,523)
C_scores = (613,570,588)
D_scores = (475,505,499)
index = np.arange(col_count)

A = plt.bar(index,
           A_scores, 
           bar_width,
           alpha=.4,
           label="K") 
B = plt.bar(index+0.2,
            B_scores,
            bar_width,
            alpha=.4,
            label="C") 
C = plt.bar(index+0.4,
            C_scores,
            bar_width,
            alpha=.4,
            label="N") # x,y ,width
D = plt.bar(index+0.6,
            D_scores,
            bar_width,
            alpha=.4,
            label="F") # x,y ,width

def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2., 
            height*1.05, 
            '%d' % int(height),
            ha = "center",
            va = "bottom",
        )
createLabels(A)
createLabels(B)
createLabels(C)
createLabels(D)
plt.ylabel("Mean score")
plt.xlabel("Subject")
plt.title("Test Scores by Contry")
plt.xticks(index+.3 / 2 ,("Math","Reading","Science")) #Bar底標文字為了至中所以+.3 / 2
plt.legend() #右上方文字

plt.grid(True)
plt.show()

pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)

data = web.DataReader("F", 'yahoo', start, end) # F指的是Finance的資料
data

data.plot()

data.plot(y="Close")

data["Close"].plot()

data[["High","Low"]].plot()

df = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range('12/31/2017', periods=100), columns=list('ABCD')) #建立一筆隨機的資料np.random.randn(100, 4)，x為日期(從12/31開始為期100天的period)，columns設定為A,B,C,D 
df

df = df.cumsum()
df

df.plot()

iris = sns.load_dataset('iris')
iris.head()

sns.set()
sns.pairplot(iris, hue='species', size=3);

rng = np.random.RandomState(42)
x = 50 * rng.rand(50)
print(x) 
y = 2 * x - 1 + rng.randn(50)
print(y)
plt.scatter(x, y)

"""## 動態視覺化"""

from bokeh.plotting import figure, show

p = figure(plot_width=500, plot_height=500)

x = [1,2,3,4,5,6,7,8,9,10,11]
y = [6,3,7,2,4,6,1,2,3,5,6]
p.circle(x, y, size=20, color="gray", alpha=0.6)
p.line(x, y, line_width=3)

show(p)

x1 = [1, 2, 3]
x2 = [2, 3, 4, 5, 6]
y1 = [3, 2, 5]
y2 = [3, 2, 4, 1, 3]
p.multi_line([x1,x2] , [y1, y2],
             color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=5)
show(p)

p = figure(plot_width=500, plot_height=500)
p.vbar(x=[1, 2, 3, 4], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7, 2.9], color="black",alpha=0.4)
show(p)

p = figure(plot_width=500, plot_height=500)
x1 = [1, 4, 5, 2]
x2 = [3, 4, 5, 6]
x3 = [1,3,2]
y1 = [2, 3, 5, 6]
y2 = [4, 7, 7, 5]
y3 = [7,8,5.5]
p.patches([x1,x2,x3 ], [y1,y2,y3],
          color=["black", "navy","firebrick"], alpha=[0.2, 0.2,0.3], line_width=2)

show(p)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html_doc, 'html.parser')  #使用html.parser這個python的解析程序

print(soup.prettify())

soup.find_all('p')

for link in soup.find_all('a'):
    print(link.get('href'))

for className in soup.find_all('p'):
    print(className.get('class'))

soup.find(id="link3")

print(soup.get_text())

"""# Decision tree"""

from sklearn import tree 
features = [[150,1],[170,1],[130,0],[140,0]]
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

wantPredict = clf.predict([[120,0]]) 
if wantPredict == [1]:
    print('This is an apple')
elif wantPredict == [0]:
    print('This is an orange')

"""# KNN"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
print(iris)

iris_data = iris.data
iris_label = iris.target

iris_data[0:3]
iris_label

train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)

knn = KNeighborsClassifier()

knn.fit(train_data,train_label)

print(knn.predict(test_data))

print(test_label)

"""# Linear regession"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets

X,y = datasets.make_regression(n_samples=200,n_features=1,n_targets=1,noise=30) 
#make_regression()方法，建立200個樣本(samples)，只有一種特徵(features)和一種標籤類別（label），我們將noise設為10，這樣資料會比較分散一點。

plt.scatter(X,y,linewidths=0.1)
plt.show()

model = LinearRegression()
model.fit(X,y)

predict = model.predict(X[:200,:])

plt.plot(X,predict,c="red")
plt.scatter(X,y)
plt.show()

model = LinearRegression(fit_intercept=True)
model

X = x[:, np.newaxis]
X.shape
model.fit(X, y)

xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit);

"""# Stanardlization"""

from sklearn import preprocessing
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC  #SVM算法

X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,
                          random_state=3,scale=100,n_clusters_per_class=1)
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf = SVC()
clf.fit(X_train,y_train)

clf.score(X_test,y_test)

X = preprocessing.scale(X) #標準化
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf = SVC()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)

"""# Crossvalidation"""

from sklearn.cross_validation import cross_val_score

"""# 存模組"""

from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

clf = svm.SVC()
iris = datasets.load_iris()
X,y = iris.data , iris.target
clf.fit(X,y)

joblib.dump(clf,'clf.pkl')

print(clf.predict(X[0:1]))