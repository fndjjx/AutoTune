
logistic_config = {"algo": "logistic", "penalty": ["str", ["l1","l2"]], "dual": ["bool", [True,False]], "C":["float", [0.01, 10, 100]], "max_iter": ["int", [10,300,10]]}
gradient_boost_config = {"algo": "gb", "loss": ["str", ['deviance','exponential']], "presort": ["bool", [True,False]], "learning_rate":["float", [0.01, 10, 100]], "n_estimators": ["int", [10,1000,10]], "max_depth": ["int", [1,10,5]], "min_samples_split": ["float", [1, 10, 10]], "max_features": ["float", [0.01, 1, 20]], "max_leaf_nodes": ["int", [1, 10, 5]]}

