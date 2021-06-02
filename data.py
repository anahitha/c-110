import plotly.figure_factory as ff 
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as go

f = pd.read_csv('medium_data.csv')
data = f["claps"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
print(mean, stdev)

def randommeans(n):
    dataset = []
    for i in range(0, n):
        r = random.randint(0, len(data)-1)
        dataset.append(data[r])
    mean = statistics.mean(dataset)
    return mean

def graph(data, average, stdev):
    fig = ff.create_distplot([data], ["average"], show_hist = False)
    fig.add_trace(go.Scatter(x=[average, average], y = [0, 12], mode='lines', name = "mean"))
    fig.add_trace(go.Scatter(x=[stdev, stdev], y=[0, 12], mode= 'lines', name = "standard dev"))
    fig.show()

def st():
    meanlist = []
    for i in range(0, 100):
        m = randommeans(30)
        meanlist.append(m)
    stdev2 = statistics.stdev(meanlist)
    print(stdev2)
    graph(meanlist, mean, stdev)

st()
