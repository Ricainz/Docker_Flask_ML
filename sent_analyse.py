#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample


# In[2]:


df = pd.read_csv('Reviews.csv')


# In[3]:


df.head(5)


# In[4]:


df.info()


# In[5]:


df.dropna(inplace=True)


# In[6]:


df.info()


# In[7]:


df_needed = pd.DataFrame()


# In[8]:


df_needed['sentiment'] = df['Score'].apply(lambda x: 1 if x > 3 else -1 if x < 3 else 0)


# In[9]:


df_needed['text'] = df['Text']


# In[10]:


df_needed['summary'] = df.Summary


# In[47]:


df_needed


# In[12]:


df_needed.describe()


# In[13]:


df_needed['text_sum'] = df_needed.text + " " + df_needed.summary


# In[14]:


df_needed['text_sum'][0]


# In[50]:


df_majority = df_needed[df_needed.sentiment==1]
df_minority = df_needed[df_needed.sentiment==-1]
df_neutral = df_needed[df_needed.sentiment==0]
 
# Downsample majority class
df_majority_downsampled = resample(df_minority, 
                                 replace=True,    # sample without replacement
                                 n_samples=len(df_majority),  # to match minority class
                                 random_state=34) # reproducible results
 
# Combine minority class with downsampled majority class
df_downsampled = pd.concat([df_majority_downsampled, df_majority,df_neutral])
 
# Display new class counts
df_downsampled.info()


# In[51]:


df_downsampled


# In[ ]:





# In[ ]:





# In[52]:


X_train, X_test, y_train, y_test = train_test_split(df_downsampled['text_sum'],df_downsampled['sentiment'],test_size =0.25, random_state=32)


# In[53]:


vectorizer = TfidfVectorizer(stop_words='english')


# In[54]:


pipeline = Pipeline(steps=[('vect', vectorizer),
                     ('clf', RandomForestClassifier(n_jobs=8))])


# In[55]:


model = pipeline.fit(X_train.to_numpy(),y_train.to_numpy())


# In[ ]:


y_train[:10000]


# In[56]:


from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, model.predict(X_test)))
#print(confusion_matrix(y_test, model.predict(X_test)))


# In[25]:


import joblib
joblib.dump(model,'model.sav')


# In[39]:


model.predict(['Today is a good day']) 


# In[57]:


joblib.dump(model,'model.pkl.compressed', compress=('lzma', 3))


# In[ ]:




