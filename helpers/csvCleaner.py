import pandas as pd
import copy


def dropDuplicates(joinedList, subset, keep='first'):
    return pd.concat(map(pd.read_csv, joinedList), ignore_index=True).drop_duplicates(subset=[subset], keep=keep)


def dropRowStrContains(dataFrame, columns, text):
    cloneDataFrame = copy.copy(dataFrame)
    for item in columns:
        cloneDataFrame = cloneDataFrame[
            cloneDataFrame[item].str.contains(text) == False
        ]
    return cloneDataFrame
