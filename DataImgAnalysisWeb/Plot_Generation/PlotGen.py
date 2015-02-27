import sys, os
from bottle import route, request, run
from matplotlib import pyplot
from numpy import arange
import bisect

@route('/upload', method='POST')
def do_upload():
    type   = request.forms.get('type')
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    str = upload.filename
    upload.save('/Users/shedimbiprudhvirao/Desktop/Cloud')
    with open(upload.filename) as f:
        content = f.readlines()
    x=[]
    y=[]
    for temp in content:
        li = temp.split()
        if li[0] not in x:
            x.append(li[0])
            y.append(int(li[1]))
        else:
            t = x.index(li[0])
            y[t] = y[t] + int(li[1])
    
   
    if type == 'pie':
        piechart(x,y)
    elif type == 'bar':
        barplot(x,y)


def barplot(labels,data):
       pos=arange(len(data))
       pyplot.xticks(pos+0.4,labels) 
       pyplot.bar(pos,data)
       pyplot.savefig('dwwww')
       pyplot.show()

def piechart(labels,data):
    fig=pyplot.figure(figsize=(7,7))
    pyplot.pie(data,labels=labels,autopct='%1.2f%%')
    pyplot.savefig('dwwww')
    pyplot.show()

run(host='localhost', port=8680, debug=True)
