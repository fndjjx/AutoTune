
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import f1_score, make_scorer, accuracy_score

import numpy as np
import pandas as pd
from parameter_tune import ParameterTune


df = pd.read_csv("/tmp/train_after_etl.csv")
y = df["y"].values
df = df.drop("y",axis=1)
x = df.values

pt = ParameterTune(GradientBoostingClassifier,"gradientboost",x,y)
#hs = logistic_config
#pt = ParameterTune(LogisticRegression,hs,x,y)
pt.run(10, 0.5, 0.3, 10)
print(pt.get_best(1))


scorer = make_scorer(f1_score)
scorer = make_scorer(accuracy_score)

clf = GradientBoostingClassifier()
#clf = LogisticRegression()
clf.fit(x,y)
score = np.mean(cross_val_score(clf, x, y, scoring=scorer))
print(score)


                            
