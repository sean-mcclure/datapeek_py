import pandas as pd
from fuzzywuzzy import fuzz

def encode_and_bind(frame, feature_to_encode):
    dummies = pd.get_dummies(frame[[feature_to_encode]])
    res = pd.concat([frame, dummies], axis=1)
    res = res.drop([feature_to_encode], axis=1)
    return(res)

def remove_features(frame, list_of_columns):
    res = frame.drop(frame[list_of_columns],axis=1)
    return(res)

def apply_function_to_column(frame, list_of_columns, new_col, funct):
    frame[new_col] = frame[list_of_columns].apply(lambda x: eval(funct))
    return(frame)

def get_closest_string(list_of_strings, search_string):
    all_dists = []
    all_strings = []
    for string in list_of_strings:
        dist = fuzz.partial_ratio(string, search_string)
        all_dists.append(dist)
        all_strings.append(string)
    top = max(all_dists)
    ind=0
    for i, x in enumerate(all_dists):
        if x == top:
            ind = i
    return(all_strings[ind])