import plotly.express as px
import csv

import numpy as np



def getDataSource():
    marks=[]
    daysPresent=[]
    with open('Student Marks vs Days Present.csv',newline="") as f:
        reader=csv.DictReader(f)

        for r in reader:
            daysPresent.append(float(r["Days Present"]))
            marks.append(float(r["Marks In Percentage"]))
    return{"x":daysPresent , "y":marks}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

data=getDataSource()
findCorrelation(data)