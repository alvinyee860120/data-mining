# -*- coding: utf-8 -*-
"""[A2]104403039 BG.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pQS7Jz2Tp-c9AXQBPaTk61tE_m-YJ9EM
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()
uploaded2 = files.upload()

import io

df = pd.read_csv(io.BytesIO(uploaded['QuickML_data_utf8a.csv']))  #導入數據集（叫做df）
df2= pd.read_csv(io.BytesIO(uploaded2['1072_boy_or_girl.csv']))
# Dataset is now stored in a Pandas Dataframe

"""# **導入Decision Tree**"""

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image, display
import pydotplus

def jupyter_graphviz(m, **kwargs):
    dot_data = StringIO()
    export_graphviz(m, dot_data, **kwargs) #導出決策樹的設定
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())#圖形設定
    display(Image(graph.create_png())) #顯示圖形

"""# **transform跟調整**"""

df['phone_os'] = df['phone_os'].str.lower()
# removing leading and trailing whitespaces
df['phone_os'] = df['phone_os'].str.strip()
df=df.drop(columns=['id', 'timestamp','self_intro'])
coded_star_signs = {'水瓶座':1, '雙魚座':2, '牡羊座':3, '金牛座':4, '雙子座':5, '巨蟹座':6, '獅子座':7, '處女座':8, '天秤座':9, '天蠍座':10, '射手座':11, '摩羯座':12}
coded_phone_os = {'apple':1, 'android':2, 'windows phone':3, 'johncena':4}
coded_gender = {2:-1} #girls as -1

coded_df = df.replace({"star_sign": coded_star_signs})
coded_df = coded_df.replace({"phone_os": coded_phone_os})
coded_df = coded_df.replace({"gender": coded_gender})

coded_df[0:10]

#check which columns have NaN in them
coded_df.isnull().any()
#show rows where yt field is NaN
coded_df[coded_df['yt'].isnull()]
#show rows where iq field is NaN
coded_df[coded_df['iq'].isnull()]
# lets clean up the codes
# ref: https://www.python-course.eu/lambda.php, http://book.pythontips.com/en/latest/lambdas.html
nan_rows = lambda df: df[df.isnull().any(axis=1)]
nan_rows(coded_df)
cleaned_df = coded_df.dropna()

cleaned_df = cleaned_df[(cleaned_df['height']<200) & (cleaned_df['height']>140) & (cleaned_df['weight']<200) & (cleaned_df['height']>100) & (cleaned_df['fb_friends']<=5000)]

cleaned_df.describe()

"""# **TEST資料集處理**"""

df2['phone_os'] = df2['phone_os'].str.lower()
# removing leading and trailing whitespaces
df2['phone_os'] = df2['phone_os'].str.strip()
df2=df2.drop(columns=['id','timestamp','self_intro'])
coded_star_signs = {'水瓶座':1, '雙魚座':2, '牡羊座':3, '金牛座':4, '雙子座':5, '巨蟹座':6, '獅子座':7, '處女座':8, '天秤座':9, '天蠍座':10, '射手座':11, '摩羯座':12}
coded_phone_os = {'apple':1, 'android':2, 'windows phone':3, 'johncena':4}
coded_gender = {2:-1} #girls as -1

coded_df2 = df2.replace({"star_sign": coded_star_signs})
coded_df2 = coded_df2.replace({"phone_os": coded_phone_os})
coded_df2 = coded_df2.replace({"gender": coded_gender})

coded_df2[0:10]

#check which columns have NaN in them
coded_df2.isnull().any()
#show rows where yt field is NaN
coded_df2[coded_df2['yt'].isnull()]
#show rows where iq field is NaN
coded_df2[coded_df2['iq'].isnull()]
# lets clean up the codes
# ref: https://www.python-course.eu/lambda.php, http://book.pythontips.com/en/latest/lambdas.html
nan_rows = lambda df2: df2[df2.isnull().any(axis=1)]
nan_rows(coded_df2)
cleaned_df2 = coded_df2.dropna()

y_test107 = cleaned_df2.pop('gender') # this is our target label
X_test107 = cleaned_df2 # this is our 'data'

# importing scikit-learn library to help us split the dataset into training and validation sets
from sklearn.model_selection import train_test_split
# x2,y2用來進行resampling
y = cleaned_df.pop('gender') # this is our target label
X = cleaned_df # this is our 'data'
y2 = y
X2 =X
X3 = X
y3 = y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.25, random_state=42)

X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.25, random_state=42)

"""# resample(undersample)"""

from imblearn.under_sampling import RandomUnderSampler #導入做random undersampling 
rus = RandomUnderSampler(random_state=42)
X2_resampled, y2_resampled = rus.fit_sample(X2_train, y2_train)
X2_train= X2_resampled
y2_train = y2_resampled

"""# **resample**(oversample)"""

from imblearn.over_sampling import RandomOverSampler #導入做random oversampling 
ros = RandomOverSampler(random_state=42)
X3_resampled, y3_resampled = rus.fit_sample(X3_train, y3_train)
X3_train= X3_resampled
y3_train = y3_resampled

#建立decision tree相關（圖形,model)
import sklearn.datasets as datasets

dtree = DecisionTreeClassifier(random_state=42)
#DT2用來處理resampling(SMOTE)後的dataset
dtree2 =DecisionTreeClassifier(random_state=42)
dtree.fit(X_train, y_train)
dtree2.fit(X2_train, y2_train)
dtree3 =DecisionTreeClassifier(random_state=42)
dtree3.fit(X3_train, y3_train)
#jupyter_graphviz(dtree, filled=True, rounded=True, special_characters=True)#

#驗證decision tree
predicted_ans = dtree.predict(X_test107)
predicted_ans2 = dtree2.predict(X_test107)
predicted_ans3 = dtree3.predict(X_test107)

"""# Decisiontree(initial data)"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test107, predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test107, predicted_ans)

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
targets_name = ['Boy','Girl']
print(metrics.classification_report(y_test107, predicted_ans,labels=labels,target_names = targets_name))

"""# **undersampling**"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test107, predicted_ans2)

print('Average precision-recall2 score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test107, predicted_ans2)

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
targets_name = ['Boy','Girl']
print(metrics.classification_report(y_test107, predicted_ans2,labels=labels,target_names = targets_name))

"""# oversampling"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test107, predicted_ans3)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test107, predicted_ans3)

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
targets_name = ['Boy','Girl']
print(metrics.classification_report(y_test107, predicted_ans3,labels=labels,target_names = targets_name))

"""# Randomforest"""

from sklearn.preprocessing import StandardScaler
XR_test=X_test107
XR2_test=X_test107
XR3_test=X_test107

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
# 載入資料




sc = StandardScaler()  
#X_train = sc.fit_transform(X_train)  
#XR_test = sc.transform(XR_test)  

from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(n_estimators=120, random_state=2)  
regressor.fit(X_train, y_train)  
r_predicted_ans = regressor.predict(XR_test)

"""# oversampling"""

#sc3 = StandardScaler()  
#X3_train = sc3.fit_transform(X3_train)  
#XR3_test = sc3.transform(XR3_test)  



regressor3 = RandomForestClassifier(n_estimators=120, random_state=2)  
regressor3.fit(X3_train, y3_train)  
r3_predicted_ans = regressor3.predict(XR3_test)

"""# **undersampling**"""

#sc2 = StandardScaler()  
#X2_train = sc2.fit_transform(X2_train)  
#XR2_test = sc2.transform(XR2_test) 

from sklearn.ensemble import RandomForestClassifier

regressor2 = RandomForestClassifier(n_estimators=120, random_state=2)  
regressor2.fit(X2_train, y2_train)  
r2_predicted_ans = regressor2.predict(XR2_test)

"""# (rf)inital data"""

#結果圖像化#inital
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test107, r_predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test107, r_predicted_ans)

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
targets_name = ['Boy','Girl']
print(metrics.classification_report(y_test107, r_predicted_ans,labels=labels,target_names = targets_name))

"""# **undersampling**"""

#結果圖像化#inital
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test107, r_predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test107, r_predicted_ans)

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
targets_name = ['Boy','Girl']
print(metrics.classification_report(y_test107, r2_predicted_ans,labels=labels,target_names = targets_name))

"""# oversampling"""

#結果圖像化
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test107, r3_predicted_ans)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test107, r3_predicted_ans)

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

labels = [1,-1]
targets_name = ['Boy','Girl']
print(metrics.classification_report(y_test107, r3_predicted_ans,labels=labels,target_names = targets_name))