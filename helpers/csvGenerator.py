import pandas as pd
import sys


def dataFrameSwitch(dict, index):
    if index:
        return pd.DataFrame(dict, index)
    return pd.DataFrame(dict)


def csvGenerator(dict, file_name, index=None):
    if (index):
        dataFrameSwitch(dict, index).to_csv(file_name)
    return dict


sys.modules[__name__] = csvGenerator
