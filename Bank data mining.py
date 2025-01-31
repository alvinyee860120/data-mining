# -*- coding: utf-8 -*-
"""[A2]104403039 Bank.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jJDBz3EczhEa_h3zx2bc4UqYDVcpZpEb
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded['bank01.csv']))  #導入數據集（叫做df）
# Dataset is now stored in a Pandas Dataframe

"""# **導入Decision Tree**"""

from sklearn.tree import DecisionTreeClassifier, export_graphviz #導入決策樹
from sklearn.externals.six import StringIO
from IPython.display import Image, display
import pydotplus

def jupyter_graphviz(m, **kwargs):
    dot_data = StringIO()
    export_graphviz(m, dot_data, **kwargs) #導出決策樹的設定
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())#圖形設定
    display(Image(graph.create_png())) #顯示圖形

"""# transform 跟調整"""

df['job'] = df['job'].str.lower() #lower string
df['job'] = df['job'].str.strip() 
# removing leading and trailing whitespaces
#df=df.drop(columns=['duration', 'pdays', 'campaign', 'previous'])
coded_job = {'admin.':1, 'blue-collar':2, 'entrepreneur':3, 'housemaid':4, 'management':5, 'retired':6, 'self-employed':7, 'services':8, 'student':9, 'technician':10, 'unemployed':11, 'unknown':12}
coded_month = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
coded_marital = {'married':1, 'single':2, 'divorced':3,'unknown':4}
coded_default = {'yes':1, 'no':-1,'unknown':0} 
coded_education = {'primary':1, 'secondary':2, 'tertiary':3,'unknown':4}
coded_housing = {'yes':1, 'no':-1,'unknown':0} 
coded_loan = {'yes':1, 'no':-1,'unknown':0}
coded_contact = {'cellular':1, 'unknown':0, 'telephone':2} 
coded_poutcome = {'failure':-1, 'unknown':0,'success':1,'other':2} 
coded_y = {'no':1, 'yes':-1} 

coded_df = df.replace({"month": coded_month})
coded_df = coded_df.replace({"job": coded_job})
coded_df = coded_df.replace({"marital": coded_marital})
#coded_df = coded_df.replace({"education": coded_education})
coded_df = coded_df.replace({"default": coded_default})
coded_df = coded_df.replace({"education": coded_education})
coded_df = coded_df.replace({"housing": coded_housing})
coded_df = coded_df.replace({"loan": coded_loan})
coded_df = coded_df.replace({"contact": coded_contact})
coded_df = coded_df.replace({"poutcome": coded_poutcome})
coded_df = coded_df.replace({"y":coded_y})

coded_df[0:10]

#check which columns have NaN in them
coded_df.isnull().any()
#show rows where yt field is NaN
#show rows where iq field is NaN
# lets clean up the codes
# ref: https://www.python-course.eu/lambda.php, http://book.pythontips.com/en/latest/lambdas.html
nan_rows = lambda df: df[df.isnull().any(axis=1)]
nan_rows(coded_df)
cleaned_df = coded_df.dropna()
cleaned_df.describe()

"""# **切割出train/test set**"""

# importing scikit-learn library to help us split the dataset into training and validation sets
from sklearn.model_selection import train_test_split
yy = cleaned_df.pop('y') # this is our target label
X = cleaned_df # this is our data
yy2 = yy
X2 = X
#X2 跟 yy2 做 random undersampling 
X4 = X
yy4 = yy
#X4 跟 yy4 做 random oversampling

X_train, X_test, yy_train, yy_test = train_test_split(X, yy, test_size=0.33, random_state=42)

X2_train, X2_test, yy2_train, yy2_test = train_test_split(X2, yy2, test_size=0.33, random_state=42)

X4_train, X4_test, yy4_train, yy4_test = train_test_split(X4, yy4, test_size=0.33, random_state=42)

"""# **random undersampling**"""

from imblearn.under_sampling import RandomUnderSampler #導入做random undersampling 
rus = RandomUnderSampler(random_state=42)
X2_resampled, yy2_resampled = rus.fit_sample(X2_train, yy2_train)
X2_train= X2_resampled
yy2_train = yy2_resampled

"""# **random oversampling**"""

from imblearn.over_sampling import RandomOverSampler #導入做random oversampling 
ros = RandomOverSampler(random_state=42)
X4_resampled, yy4_resampled = ros.fit_sample(X4_train, yy4_train)
X4_train = X4_resampled
yy4_train = yy4_resampled

"""# **建立Decision tree**"""

#建立decision tree相關（圖形,model)
import sklearn.datasets as datasets
#DT用來處理initial dataset
dtree = DecisionTreeClassifier(random_state=42)
dtree.fit(X_train, yy_train)
#DT2用來處理resampling(undersampling)後的dataset
dtree2 =DecisionTreeClassifier(random_state=42)
dtree2.fit(X2_train, yy2_train)
#DT3用來處理resampling(oversampling)後的dataset
dtree3 =DecisionTreeClassifier(random_state=42)
dtree3.fit(X4_train, yy4_train)

#驗證decision tree
predicted_ans = dtree.predict(X_test) 
predicted_ans2 = dtree2.predict(X2_test) 
predicted_ans3 = dtree3.predict(X4_test)

"""# **(dtree)Initial data**"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(yy_test, predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(yy_test, predicted_ans)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
#===================================================================
from sklearn import metrics
#print(metrics.precision_score(y_test, predicted_ans, average='micro'))
#print(metrics.recall_score(y_test, predicted_ans, average='micro'))
labels = [1,-1]
targets_name = ['no','yes']
print(metrics.classification_report(yy_test, predicted_ans,labels=labels,target_names = targets_name))



"""# (dtree)Undersampling"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(yy2_test, predicted_ans2)

print('Average precision-recall2 score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(yy2_test, predicted_ans2)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
from sklearn import metrics
#print(metrics.precision_score(y_test, predicted_ans, average='micro'))
#print(metrics.recall_score(y_test, predicted_ans, average='micro'))

labels = [1,-1]
targets_name = ['no','yes']
print(metrics.classification_report(yy2_test, predicted_ans2,labels=labels,target_names = targets_name))

"""# (dtree)Oversampling"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(yy4_test, predicted_ans3)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(yy4_test, predicted_ans3)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
#===================================================================
from sklearn import metrics
#print(metrics.precision_score(y_test, predicted_ans, average='micro'))
#print(metrics.recall_score(y_test, predicted_ans, average='micro'))

labels = [1,-1]
targets_name = ['no','yes']
print(metrics.classification_report(yy4_test, predicted_ans3,labels=labels,target_names = targets_name))

"""# **導入跟建立random forest**"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
# 載入資料

from sklearn.preprocessing import StandardScaler #導入standardscaler 

sc = StandardScaler()  
X_train = sc.fit_transform(X_train)  
X_test = sc.transform(X_test)  

from sklearn.ensemble import RandomForestClassifier #導入RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=120, random_state=2)  
regressor.fit(X_train, yy_train)  
r_predicted_ans = regressor.predict(X_test)

"""# **(rf)Initial data**"""

from sklearn.metrics import average_precision_score
average_precision = average_precision_score(yy_test, r_predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(yy_test, r_predicted_ans)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
#===================================================================
from sklearn import metrics
#print(metrics.precision_score(y_test, predicted_ans, average='micro'))
#print(metrics.recall_score(y_test, predicted_ans, average='micro'))

labels = [1,-1]
targets_name = ['no','yes']
print(metrics.classification_report(yy_test, r_predicted_ans,labels=labels,target_names = targets_name))

"""# **(rf)undersampling**"""

from sklearn.preprocessing import StandardScaler #導入standardscaler 
sc = StandardScaler() 
X2_train = sc.fit_transform(X2_train)  
X2_test = sc.transform(X2_test)  
from sklearn.ensemble import RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=120, random_state=2) 
regressor.fit(X2_train, yy2_train)  
r_predicted_ans2 = regressor.predict(X2_test)

from sklearn.metrics import average_precision_score
average_precision = average_precision_score(yy2_test, r_predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(yy2_test, r_predicted_ans)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
#===================================================================
from sklearn import metrics
#print(metrics.precision_score(y_test, predicted_ans, average='micro'))
#print(metrics.recall_score(y_test, predicted_ans, average='micro'))

labels = [1,-1]
targets_name = ['no','yes']
print(metrics.classification_report(yy2_test, r_predicted_ans2,labels=labels,target_names = targets_name))

"""# **(rf)oversampling**"""

from sklearn.preprocessing import StandardScaler #導入standardscaler 
sc = StandardScaler() 
X4_train = sc.fit_transform(X4_train)  
X4_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier 
regressor = RandomForestClassifier(n_estimators=120, random_state=2) 
regressor.fit(X4_train, yy4_train)  
r_predicted_ans4 = regressor.predict(X4_test)

from sklearn.metrics import average_precision_score
average_precision = average_precision_score(yy4_test, r_predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(yy4_test, r_predicted_ans)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
#===================================================================
from sklearn import metrics
#print(metrics.precision_score(y_test, predicted_ans, average='micro'))
#print(metrics.recall_score(y_test, predicted_ans, average='micro'))

labels = [1,-1]
targets_name = ['no','yes']
print(metrics.classification_report(yy4_test, r_predicted_ans4,labels=labels,target_names = targets_name))