from helpers import pth, cc, csvGenerator
import pandas as pd
from datetime import datetime
now = datetime.now()  # current date and time


joinedList = pth.pathJoinList('csv/divar/', 'ex-divar*.csv')
cleanedDataFrame = cc.dropDuplicates(joinedList, "link")

for strContain in ["بریانک", 'خلیج', 'سلیمانی', 'اندیشه','شهرزیبا', 'بهشتی']:
    cleanedDataFrame = cc.dropRowStrContains(
        cleanedDataFrame, ["enterprise", 'title'], strContain)

# print(cleanedDataFrame)
date_time = now.strftime("%m-%d-%Y")

csvGenerator(cleanedDataFrame, date_time + '.csv', 'csv/divar/')
