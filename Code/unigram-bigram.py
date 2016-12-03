
import numpy
import pandas
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import sklearn.linear_model as lm
from nltk.corpus import stopwords
import nltk
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from sklearn import pipeline,metrics, grid_search 
from sklearn.metrics import f1_score,precision_score
from numpy import genfromtxt
import random

with open('sarcasm_dataset.txt','r') as fname:
    file_content = fname.readlines()
random.shuffle(file_content)

output = 'tweets' + "\t" + 'label' + "\n"

for tweet_content in file_content:    
    tweet, label = tweet_content[:-3], tweet_content[-3]
    output += tweet + "\t" + label + "\n"
    
outputfile = open('dataset_csv.csv',"w")
outputfile.write(output)
outputfile.close() 

df = pandas.DataFrame()
train = pandas.DataFrame()
test = pandas.DataFrame()

df = pandas.read_csv("dataset_csv.csv", header=0, sep='\t')

train = df[0:1500]
test = df[1501:]

tfidf_vec = TfidfVectorizer(
            analyzer="word",max_features=None,
            token_pattern=r'\w{1,}',strip_accents='unicode',
            lowercase=True,ngram_range=(1,3),
            min_df=2,use_idf=True,
            smooth_idf=True,norm="l2",
            sublinear_tf=True)

x_train,x_test,y_train,y_test=train_test_split(train['tweets'],train['label'],test_size=0.4,random_state=2,stratify=train['label'])

train_tfidf_matrix=tfidf_vec.fit_transform(x_train)
test_tfidf_matrix=tfidf_vec.fit_transform(x_test)

train = pandas.DataFrame(train_tfidf_matrix.toarray())
test = pandas.DataFrame(test_tfidf_matrix.toarray())

svd = TruncatedSVD(algorithm="randomized", random_state=None, tol=0.0)
scl = StandardScaler()
lr = lm.LogisticRegression(class_weight="balanced", tol = 0.0001)
clf = pipeline.Pipeline([('svd', svd),
    						 ('scl', scl),
                    	     ('lr', lr)])

param_grid = {'svd__n_components' : [200,250,300,350,400],
                 'svd__n_iter':[3,4,5],
                 'lr__C': [10,11,12,13,14,15,16,17],
                  'lr__penalty':["l1","l2"]}

f_scorer = metrics.make_scorer(f1_score, greater_is_better = True)

model = grid_search.GridSearchCV(estimator = clf, param_grid=param_grid, scoring=f_scorer,
                                     verbose=10, n_jobs=-1, iid=True, refit=True, cv=10)



model.fit(train, y_train)
print("Best score: %0.3f" % model.best_score_)

print("Best parameters set:")
best_parameters = model.best_estimator_.get_params()
for param_name in sorted(param_grid.keys()):
	print("\t%s: %r" % (param_name, best_parameters[param_name]))

best_model = model.best_estimator_
best_model.fit(train,y_train)
preds = best_model.predict(x_test)
preds=list(preds)
target_labels=list(y_test)
print f1_score(target_labels,preds,average="weighted")





