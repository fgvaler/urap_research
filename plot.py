
import matplotlib.pyplot as plt

def scatter(x, y):
    
    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])

    ax.scatter(x, y, color='r')

    plt.show()

def bar_graph(hist, col_names, ticks, xlabel, ylabel, title):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    langs = col_names
    students = hist
    ax.bar(langs,students)
    locs, labels = plt.xticks()
    plt.xticks(ticks)
    plt.show()