
logistic_config = {"penalty": ["str", ["l1","l2"]], "dual": ["bool", [True,False]], "C":["float", [0.01, 10, 100]], "max_iter": ["int", [10,300,10]]}
gradient_boost_config = {"loss": ["str", ['deviance','exponential']], "presort": ["bool", [True,False]], "learning_rate":["float", [0.01, 10, 100]], "n_estimators": ["int", [10,1000,10]], "max_depth": ["int", [1,10,5]], "min_samples_split": ["float", [0, 1, 10]], "max_features": ["float", [0.01, 1, 20]], "max_leaf_nodes": ["int", [1, 10, 5]]}
xgboost_config = {"learning_rate":["float", [0.01, 10, 100]], "n_estimators":["int", [10,500,20]],"max_depth": ["int", [1,20,20]], "colsample_bytree": ["float", [0, 1, 10]], "colsample_bylevel": ["float", [0, 1, 10]],"subsample": ["float", [0, 1, 10]]}
random_forest_config={"n_estimators":["int", [10,500,20]], "criterion":["str", ["gini","entropy"]], "max_features": ["float", [0.01, 1, 20]], "max_depth":["int", [1,10,5]], "min_samples_split": ["float", [0.01, 0.9, 10]], "min_samples_leaf": ["float", [0.01, 0.45, 10]],  "max_leaf_nodes": ["int", [1, 10, 5]]}


