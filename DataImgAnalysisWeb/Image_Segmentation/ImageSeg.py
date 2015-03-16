import matplotlib
matplotlib.use('Agg')
import sys, os
from bottle import route, request, run
from scipy import misc
import time as time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sklearn

@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename) 
    str = upload.filename
    upload.save('/home/ec2-user', overwrite=True) # appends upload.filename automatically 
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
    return static_file(filename, root='/home/ec2-user/Projects/DataImgAnalysisWeb/Image_Segmentation')



run(host='0.0.0.0', port=80, debug=True)
