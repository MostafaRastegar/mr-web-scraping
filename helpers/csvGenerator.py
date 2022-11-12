import pandas as pd
import sys
import os


def csvGenerator(dict, file_name, path='.', index=None):
    os.makedirs(path, exist_ok=True)
    if (index):
        return pd.DataFrame(dict, index).to_csv(path+'/'+file_name)
    return pd.DataFrame(dict).to_csv(path+'/'+file_name)


sys.modules[__name__] = csvGenerator
