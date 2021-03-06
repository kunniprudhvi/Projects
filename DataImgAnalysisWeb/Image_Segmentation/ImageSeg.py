import matplotlib
matplotlib.use('Agg')
import sys, os
from bottle import route, request, run, static_file
from scipy import misc
import time as time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering

@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename) 
    str = upload.filename
    upload.save('/Users/shedimbiprudhvirao/Documents/Projects/DataImgAnalysisWeb/Image_Segmentation', overwrite=True) # appends upload.filename automatically 
    clusterImage(str)
    p = download('output.png')
    return p

def clusterImage(str):
    lena = misc.imread(str)  
    X = np.reshape(lena, (-1, 1))

    connectivity = grid_to_graph(*lena.shape)

    print("Compute structured hierarchical clustering...")
    st = time.time()
    n_clusters = 15  # number of regions
    ward = AgglomerativeClustering(n_clusters=n_clusters,
            linkage='ward', connectivity=connectivity).fit(X)
    label = np.reshape(ward.labels_, lena.shape)
    print("Elapsed time: ", time.time() - st)
    print("Number of pixels: ", label.size)
    print("Number of clusters: ", np.unique(label).size)

    plt.figure(figsize=(5, 5))
    plt.imshow(lena, cmap=plt.cm.gray)
    for l in range(n_clusters):
        plt.contour(label == l, contours=1,
                    colors=[plt.cm.spectral(l / float(n_clusters)), ])
    plt.xticks(())
    plt.yticks(())
    plt.savefig('output')
    
 
    
def download(filename):
    return static_file(filename, root='/Users/shedimbiprudhvirao/Documents/Projects/DataImgAnalysisWeb/Image_Segmentation')



run(host='localhost', port=8090, debug=True)
