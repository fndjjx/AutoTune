import numpy as np
from gray import gray2binary

class Hyperparameter():
    def __init__(self, config):
        self.config = config
        self.algo = config["algo"]
        del self.config["algo"]
        self.mapping = []
    def parse_config(self):
        index_count = 0
        for para, value in self.config.items():
            print(para)
            print(value)
            if value[0] == "bool":
                self.mapping.append([value[0], index_count, 1, para])
                index_count += 1
            if value[0] == "str":
                choice_length = len(value[1])
                str_mapping = dict(zip(range(choice_length),value[1]))
                bit_num = choice_length
                self.mapping.append([value[0], index_count, bit_num, str_mapping, para])
                index_count = index_count+bit_num
            if value[0] == "float" or value[0] == "int":
                value_min = value[1][0]
                value_max = value[1][1]
                value_num = value[1][2]
                bit_num = int(np.log2(value_num))+1
                self.mapping.append([value[0], index_count, bit_num, value_min,float(value_max-value_min)/value_num, para])
                index_count = index_count+bit_num

        return index_count
    
    def generate_parameter(self, bit_map, enable_gray=True):
        parameter = {}
        for para in self.mapping:
            para_type = para[0]
            para_name = para[-1]
            bit_start_position = para[1]
            bit_occupied_length = para[2]
            bit_map_current_value = bit_map[bit_start_position:bit_occupied_length+bit_start_position]
            #print("bit_map_current_value {}".format(bit_map_current_value))
            if para_type == "bool":
                if bit_map_current_value[0] == 0:
                    parameter[para_name] = False
                else:
                    parameter[para_name] = True
            if para_type == "str":
                if sum(bit_map_current_value)!=1 :
                    mapping = para[-2]
                    random_index = np.random.randint(0,len(bit_map_current_value)-1)
                    for index in range(len(bit_map_current_value)):
                        if index == random_index:
                            parameter[para_name]=mapping[index]
                else:
                    mapping = para[-2]
                    for index in range(len(bit_map_current_value)):
                        if bit_map_current_value[index]==1:
                            parameter[para_name]=mapping[index]
            if para_type == "float":
                min_value = para[3]
                interval = para[4]
                bit_map_current_value = [str(i) for i in bit_map_current_value]
                if enable_gray:
                    binary_value = int(gray2binary(bit_map_current_value),2)*interval+min_value
                else:
                    binary_value = int("".join(bit_map_current_value),2)*interval+min_value
                #print(binary_value)
                parameter[para_name]=binary_value
            if para_type == "int":
                min_value = para[3]
                interval = para[4]
                bit_map_current_value = [str(i) for i in bit_map_current_value]
                if enable_gray:
                    binary_value = int(gray2binary(bit_map_current_value),2)*interval+min_value
                else:
                    binary_value = int("".join(bit_map_current_value),2)*interval+min_value
                #print(binary_value)
                parameter[para_name]=int(binary_value)
        return parameter

if __name__ == "__main__":
    config = {"algo": "logistic", "penalty": ["str", ["l1","l2"]], "dual": ["bool", [True,False]], "C":["float", [0.01, 10, 100]], "max_iter": ["int", [10,1000,10]]}
    config = {"algo": "gb", "loss": ["str", ['deviance','exponential']], "presort": ["bool", [True,False]], "learning_rate":["float", [0.01, 10, 100]], "n_estimators": ["int", [10,1000,10]], "max_depth": ["int", [1,10,5]], "min_samples_split": ["float", [1, 10, 10]], "max_features": ["float", [0.01, 1, 20]], "max_leaf_nodes": ["int", [1, 10, 5]]}
    h = Hyperparameter(config)
    r = h.parse_config()
    print(h.mapping)
    print(r)
    sample = np.random.randint(0,2,r)
    print(sample)
    #print(h.generate_parameter([0,1,1,1,1,1,1,1,0,1,1,1,1,1]))

