import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv('Reviews.csv')

print(df.info())

df.dropna(inplace=True)

df_needed = pd.DataFrame()
df_needed['sentiment'] = df['Score'].apply(lambda x: 1 if x > 3 else -1 if x < 3 else 0)
df_needed['text'] = df['Text']
df_needed['summary'] = df.Summary
df_needed['text_sum'] = df_needed.text + " " + df_needed.summary

X_train, X_test, y_train, y_test = train_test_split(df_needed['text_sum'],df_needed['sentiment'],test_size =0.25, random_state=32)

vectorizer = TfidfVectorizer(stop_words='english')

pipeline = Pipeline(steps=[('vect', vectorizer),
                     ('clf', SVC())])

model = pipeline.fit(X_train.to_numpy()[:10000],y_train.to_numpy()[:10000])

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, model.predict(X_test)))
print(confusion_matrix(y_test, model.predict(X_test)))

import joblib
joblib.dump(model,'model.sav')
