
# importing libraries
import pandas as pd
import glob
import os


def pathJoinList(dir, fileNamePattern):
    # merging the files
    joined_files = os.path.join(dir, fileNamePattern)
    return glob.glob(joined_files)
