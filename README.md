# AutoTune
A python tool to automaticly adjust hyperparameters for sklearn algorithm.
-
## Install
`python setup install`
## Usage
```
>>> import autotune
>>> import pandas as pd
>>> from sklearn.linear_model import LogisticRegression
>>> df = pd.read_csv("train.csv")
>>> y = df["target"].values
>>> df = df.drop("target",axis=1)
>>> x = df.values
>>> 
>>> at=autotune.ParameterTune(LogisticRegression,x,y,roc_auc_score,1)
>>> at.run(pop_num=10, cxpb=0.5, mutpb=0.3, gen_num=10)     
...
>>> at.get_best(1)
[[0.89400183150183155, {'penalty': 'l1', 'dual': False, 'C': 2.008, 'max_iter': 329}]]

 ```
 pop_num is population num of each generation, cxpb is crossover rate, mutpb is mutation rate, gen_num is the number of generations.
