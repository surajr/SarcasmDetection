# Sarcasm Detection #

The objective of this project is to detect Sarcasm in a text or document. There are two parts in this task, one being the Sarcasm detection which is a classification problem and the next one being Sarcasm extraction which is an Information extraction problem.

### Goal ###

* Build a good dataset which has sarcastic documents
* Annotate the data as 0/1 (sarcastic/not sarcastic)
* Identify different patterns in the text that reveal sarcasm
* Build a model that classifies a new unseen text or tweet as Sarcastic or not sarcastic 
* Evaluate the model built using f1 score

### Methodology: ###

* Sarcasm detection relies on the assumption that a negative situation often appears after the positive situations in a sarcastic document. (document here refers to text or tweet)

* [positive verb phrase] + [negative verb phrase]

* The dataset consists of 1984 tweets and it consists of 1024 Sarcastic tweets and 984 as non-sarcastic tweets.
* We used one or more of the features like Sentiment analysis, topic modeling, POS tagging, n-grams, Stemming and Lemmatization, lexical characteristics of a tweet to build a model which uses Machine Learning algorithm like RandomForest, DecisionTree, Boosting algorithms, Gaussian Naïve bayes & Logistic regression. 


### Annotation ###

* We used inter-annotator reliability – Fleiss Kappa as a measure and obtained a score of 0.6433

### Evaluation ###

* We evaluated our approach with F1 score and obtained best score of 0.76 when used with features like sentiment analysis, POS bi grams and topic modeler and RandomForest as a classifier. 



