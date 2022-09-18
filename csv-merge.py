from helpers import pth, cc, csvGenerator
import pandas as pd


joinedList = pth.pathJoinList('csv/divar/', 'ex-divar*.csv')
cleanedDataFrame = cc.dropDuplicates(joinedList, "link")

for strContain in ["بریانک", 'خلیج', 'سلیمانی']:
    cleanedDataFrame = cc.dropRowStrContains(
        cleanedDataFrame, ["enterprise", 'title'], strContain)

# print(cleanedDataFrame)
csvGenerator(cleanedDataFrame, 'merged.csv', 'csv/divar/')
