import random
import statistics

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")

# HEIGHT-
height = df["Height(Inches)"].tolist()
mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)
stdval = statistics.stdev(height)


print("height mean=",mean)
print("height median=",median)
print("height mode =",mode)
print("height stdval=",stdval)

stdvS1,stdvE1 = mean - stdval, mean + stdval
stdvS2,stdvE2 = mean - (2*stdval) , mean + (2*stdval)
stdvS3,stdvE3 = mean - (3*stdval) , mean + (3*stdval)

heightDataWithin1stStdDev = [result for result in height if result > stdvS1  and result < stdvE1]
heightDataWithin2ndStdDev = [result for result in height if result > stdvS2 and result < stdvE2]
heightDataWithing3rdStdDev = [result for result in height if result > stdvS3 and result < stdvE3]

print("Data within 1st stdv (height)= ", format(len(heightDataWithin1stStdDev)*100 / len(height)))
print("Data within 2nd stdv (height) = ", format(len(heightDataWithin2ndStdDev)*100 / len(height)))
print("Data within 3rd stdv (height) = ", format(len(heightDataWithing3rdStdDev)*100 / len(height)))


# WEIGHT -
weight = df["Weight(Pounds)"].tolist()
mean1 = statistics.mean(weight)
median1 = statistics.median(weight)
mode1 = statistics.mode(weight)
stdval1 = statistics.stdev(weight)


print("weight=",mean1)
print("weight=",median1)
print("weight=",mode1)
print("weight=",stdval1)

stdvStart1,stdvEnd1 = mean1 - stdval1 , mean1 + stdval1
stdvStart2,stdvEnd2 = mean1 - (2*stdval1) , mean1 + (2*stdval1)
stdvStart3,stdvEnd3 = mean1 - (3*stdval1) , mean1 + (3*stdval1)


weightDataWithin1stStdDev = [result for result in weight if result>stdvStart1 and result<stdvEnd1 ]
weightDataWithin2ndStdDev = [result for result in weight if result>stdvStart2 and result<stdvEnd2 ]
weightDataWithin3rdStdDev = [result for result in weight if result>stdvStart3 and result<stdvEnd3 ]



print("Data within 1st stdv (weight)= ", format(len(weightDataWithin1stStdDev)*100 / len(weight)))
print("Data within 2nd stdv (weight)= ", format(len(weightDataWithin2ndStdDev)*100 / len(weight)))
print("Data within 3rd stdv (weight)= ", format(len(weightDataWithin3rdStdDev)*100 / len(weight)))


