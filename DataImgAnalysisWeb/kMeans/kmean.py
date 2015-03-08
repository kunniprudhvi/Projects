import random
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import Orange
import sys, os
from bottle import route, request, run, static_file


@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    str = upload.filename
    upload.save('/home/ubuntu') # appends upload.filename automatically
    table = Orange.data.Table("iris")
    random.seed(42)
    km = Orange.clustering.kmeans.Clustering(table, 3, minscorechange=0, maxiters=10, inner_callback=in_callback)
    p = download('kmeans-scatter-008')
    return p



def plot_scatter(table, km, attx, atty, filename="kmeans-scatter", title=None):
    #plot a data scatter plot with the position of centeroids
    plt.rcParams.update({'font.size': 8, 'figure.figsize': [4,3]})
    x = [float(d[attx]) for d in table]
    y = [float(d[atty]) for d in table]
    colors = ["c", "w", "b"]
    cs = "".join([colors[c] for c in km.clusters])
    plt.scatter(x, y, c=cs, s=10)
    
    xc = [float(d[attx]) for d in km.centroids]
    yc = [float(d[atty]) for d in km.centroids]
    plt.scatter(xc, yc, marker="x", c="k", s=200)
    
    plt.xlabel(attx)
    plt.ylabel(atty)
    if title:
        plt.title(title)
    plt.savefig("%s-%03d.png" % (filename, km.iteration))
    plt.close()

def in_callback(km):
    print "Iteration: %d, changes: %d, score: %8.6f" % (km.iteration, km.nchanges, km.score)
    plot_scatter(table, km, "petal width", "petal length", title="Iteration %d" % km.iteration)

def download(filename):
    return static_file(filename, root='/home/ubuntu')


run(host='localhost', port=80, debug=True)
