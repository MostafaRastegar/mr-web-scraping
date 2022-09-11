import pandas as pd
import sys


def csvGenerator(dict, file_name, index=None):
    if (index):
        return pd.DataFrame(dict, index).to_csv(file_name)
    return pd.DataFrame(dict).to_csv(file_name)


sys.modules[__name__] = csvGenerator
