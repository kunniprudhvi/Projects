import matplotlib
matplotlib.use('Agg')
import random
from matplotlib import pyplot as plt
import Orange
import sys, os
from bottle import route, request, run, static_file

table=Orange.data.Table("zoo")
xax='temp'
yax='temp'
tmp = 0

@route('/upload', method='POST')
def do_upload():
    global table
    global xax
    global yax
    upload     = request.files.get('upload')
    xax   = request.forms.get('xax')
    yax   = request.forms.get('yax')
    name, ext = os.path.splitext(upload.filename)
    str = upload.filename
    upload.save('/home/ubuntu')
    fl = '/home/ubuntu/' + str
    table = Orange.data.Table(fl)
    random.seed(42)
    km = Orange.clustering.kmeans.Clustering(table, 3, minscorechange=0, maxiters=10, inner_callback=in_callback)
    p = download('kmeans-scatter-%03d.png' % tmp)
    return p



def plot_scatter(table, km, attx, atty, filename="kmeans-scatter", title=None):
    #plot a data scatter plot with the position of centeroids
    global tmp
    plt.rcParams.update({'font.size': 8, 'figure.figsize': [4,3]})
    x = [float(d[attx]) for d in table]
    y = [float(d[atty]) for d in table]
    colors = ["c", "w", "b"]
    cs = "".join([colors[c] for c in km.clusters])
    plt.scatter(x, y, c=cs, s=10)
    
    xc = [float(d[attx]) for d in km.centroids]
    yc = [float(d[atty]) for d in km.centroids]
    plt.scatter(xc, yc, marker="x", c="k", s=200)
    tmp = km.iteration
    plt.xlabel(xax)
    plt.ylabel(yax)
    if title:
        plt.title(title)
    plt.savefig("%s-%03d.png" % (filename, km.iteration))
    plt.close()

def in_callback(km):
    global table
    global xax
    global yax
    print "Iteration: %d, changes: %d, score: %8.6f" % (km.iteration, km.nchanges, km.score)
    plot_scatter(table, km, xax, yax, title="Iteration %d" % km.iteration)

def download(filename):
    return static_file(filename, root='/home/ubuntu/Projects/DataImgAnalysisWeb/kMeans')


run(host='0.0.0.0', port=80, debug=True)
