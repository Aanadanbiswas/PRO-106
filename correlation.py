import csv
import numpy as np
import plotly.express as px

def plotFigure(datapath):
    with open(datapath) as f:
        dataReader = csv.DictReader(f)
        fig = px.scatter(dataReader,x = 'Days Present',y = 'Marks In Percentage')
        fig.show()

def getDataSource(datapath):
    Marks_In_Percentage = []
    Days_Present = []
    with open(datapath) as g:
        dataReader = csv.DictReader(g)
        for row in dataReader:
            Marks_In_Percentage.append(float(row['Marks In Percentage']))
            Days_Present.append(float(row['Days Present']))
    
    return {'x': Days_Present,'y': Marks_In_Percentage}

def findCorrelation(dataSource):
    Correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(Correlation[0,1])

def setup():
    dataPath = 'correlation.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)

setup()