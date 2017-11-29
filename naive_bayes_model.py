import pandas as pd
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.learning_curve import learning_curve
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords

train_df = pd.read_csv('prep_data.csv')

X = train_df['tweet']
y = train_df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size = .3, random_state=42)

pipeline = Pipeline([
    ('vect', CountVectorizer( strip_accents='ascii')), # lowercase=True by default
    ('tfidf', TfidfTransformer()),
    ('cls', MultinomialNB())
])
pipeline.fit(X_train, y_train)

preds = pipeline.predict(X_test)

print(classification_report(y_test, preds))