import plotly.express as px
import csv
import pandas
import numpy as np



def getDataSource():
    coffee=[]
    sleep=[]
    with open('cups of coffee vs hours of sleep.csv',newline="") as f:
        reader=csv.DictReader(f)

        for r in reader:
            coffee.append(float(r["Coffee in ml"]))
            sleep.append(float(r["sleep in hours"]))
    return{"x":coffee , "y":sleep}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

data=getDataSource()
findCorrelation(data)


