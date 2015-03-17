from google.appengine.api import users

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):

        user = users.get_current_user()
        self.response.write('<html><head>')
        self.response.write('<style>body {background-color:white} img#img1{ width:100%; height:30%; } form { width: 50px; margin: 0 auto;} input#next{width:5em; height:8em;} </style>')
        self.response.write('</head> <body>')
        self.response.write('<img id="img1" src="https://nhlbiepi.files.wordpress.com/2012/04/16153431-analyzing-graphs-and-charts.jpg" alt="Not found">')
        self.response.write('<h2 style="text-align:center"> Welcome to Data Analysis Tool!</h2>')
        self.response.write('<h3 style="text-align:center"> Are you logged into your Google Account?</h3>')
        if user:
            welText = ('Welcome, %s' % (user.nickname()))
            self.response.write('<h3 style="text-align:center">%s</h3>'%welText)
            self.response.write('''
            <form action="options">
                <input type="submit" value="Next" id="next">
            </form>
        ''')
        else:
            welText = ('You are not logged into your Google Account. Please <a href="%s"> Login or Register</a>' % users.create_login_url('/'))
            self.response.write('<h3 style="text-align:center">%s</h3>'%welText)


class optionsPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        self.response.write('<html><head>')
        self.response.write('<style>body {background-color:white} img#img1{ width:100%; height:30%;} div#picwpr{width:100%; text-align:center;} div#pic{display:inline-block; padding-left:50px; padding-right:50px;} </style>')
        self.response.write('</head> <body>')
        self.response.write('<img id="img1" src="https://nhlbiepi.files.wordpress.com/2012/04/16153431-analyzing-graphs-and-charts.jpg" alt="Not found">')
        self.response.write('<h2 style="text-align:center"> Welcome to Data Analysis Tool!</h2>')
        self.response.write('<h3 style="text-align:center"> Hello %s </h3>'% user.nickname())
        self.response.write('<h4 style="text-align:center"> Please choose one of the following options:</h4>') 
        self.response.write('<div id="picwpr">')
        self.response.write('<div class="pic" id="pic"> <h4 style="text-align:center">Image Segmentation by Clustering </h4> <a href="imgSeg"><img id="img2" src="kun/upload.png" alt="Image Segmentation" style="width:128px;height:128px"> </a> </div>')
        self.response.write('<div class="pic" id="pic"> <h4 style="text-align:center">K Means Clustering </h4> <a href="kmeans"><img id="img2" src="kun/cluster.png" alt="K Means Clustering" style="width:128px;height:128px"> </a> </div>')
        self.response.write('<div class="pic" id="pic"> <h4 style="text-align:center">Pie Chart Generator </h4><a href="plots"><img id="img3" src="kun/pie_chart.png" alt="Pie Chart" style="width:128px;height:128px"> </a> </div> </div>')

class kmeansHandler(webapp2.RequestHandler):
        
    def get(self): 
        user = users.get_current_user() 
        self.response.write('<html><head>')
        self.response.write('<style>body {background-color:white} img#img1{ width:100%; height:30%; } </style>')
        self.response.write('</head> <body>')
        self.response.write('<img id="img1" src="https://nhlbiepi.files.wordpress.com/2012/04/16153431-analyzing-graphs-and-charts.jpg" alt="Not found">')
        self.response.write('<h3 style="text-align:center"> Hello %s </h3>'% user.nickname())
        self.response.write('<h3 style="text-align:center"> K Means Clustering</h3>')
        self.response.write('<h4 style="text-align:center"> Select a data file on which K Means Clustering is to be performed. Files can be of .tab, .xlsx format. Give X-Axis and Y-Axis variables as per the input for result graph output. Link for sample data file: <a href="https://drive.google.com/folderview?id=0BwvuRwovIL2ffm02NF9jcTFaalVadTRWeFRnQmxVQmhDZmVqdDg2cXZQc2VTaFA0a1ZSTEk&usp=sharing"> Sample File </a>  X Axis - sepal length Y axis - petal length</h4>')
        self.response.write('<form action="http://ec2-54-152-163-30.compute-1.amazonaws.com:80/upload" method="post" enctype="multipart/form-data">')
        self.response.write('X-Axis:      <input type="text" name="xax" />')
        self.response.write('Y-Axis:      <input type="text" name="yax" />')
        self.response.write('Select a file: <input type="file" name="upload" />')
        self.response.write('<input type="submit" value="Start upload" />')
        self.response.write('</form>')
 
class plotHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        self.response.write('<html><head>')
        self.response.write('<style>body {background-color:white} img#img1{ width:100%; height:30%; } </style>')
        self.response.write('</head> <body>')
        self.response.write('<img id="img1" src="https://nhlbiepi.files.wordpress.com/2012/04/16153431-analyzing-graphs-and-charts.jpg" alt="Not found">')
        self.response.write('<h3 style="text-align:center"> Hello %s </h3>'% user.nickname())
        self.response.write('<h3 style="text-align:center"> Pie Chart Generator</h3>')
        self.response.write('<h4 style="text-align:center"> Select a data file for which Pie Chart has to be generated. File should be of txt format. Each row in a file should contain Class and Value seperated by blank space. Link to sample file: <a href="https://drive.google.com/folderview?id=0BwvuRwovIL2ffjIwaGhMaG9XcWdpNVZudjNkcW45eHl4VHBDMEdfdVBrc3NiU1ZubUFDZVU&usp=sharing"> Sample File </a></h4>')
        self.response.write('<form action="http://ec2-54-173-8-156.compute-1.amazonaws.com:80/upload" method="post" enctype="multipart/form-data">')
        self.response.write('Select a file: <input type="file" name="upload" />')
        self.response.write('<input type="submit" value="Start upload" />')
        self.response.write('</form>')


class imgSegHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        self.response.write('<html><head>')
        self.response.write('<style>body {background-color:white} img#img1{ width:100%; height:30%; } </style>')
        self.response.write('</head> <body>')
        self.response.write('<img id="img1" src="https://nhlbiepi.files.wordpress.com/2012/04/16153431-analyzing-graphs-and-charts.jpg" alt="Not found">')
        self.response.write('<h3 style="text-align:center"> Hello %s </h3>'% user.nickname())
        self.response.write('<h3 style="text-align:center"> Image Segmentation using Hierarchical Clustering</h3>')
        self.response.write('<h4 style="text-align:center"> Select an Image which you want to segment. Please do not select a high resolution image. Black and white image with 512 * 512 resolution would be good. Image with the mentioned specification typically takes 3-5 minutes to be segmented. Link to sample images that can be used: <a href="https://drive.google.com/folderview?id=0BwvuRwovIL2ffm1zbllmNzZUVl8zUUdGaTUwdzlOdnp4MzVxTEUxeEZfbjdxcGRHOVVIQ2s&usp=sharing"> Sample File </a> </h4>')
        self.response.write('<form action="http://ec2-52-11-140-90.us-west-2.compute.amazonaws.com:80/upload" method="post" enctype="multipart/form-data">')
        self.response.write('Select a file: <input type="file" name="upload" />')
        self.response.write('<input type="submit" value="Start upload" />')
        self.response.write('</form>')


ROUTES = [webapp2.Route(r'/options', optionsPage),
          webapp2.Route(r'/', MainPage), 
          webapp2.Route(r'/kmeans', kmeansHandler),
          webapp2.Route(r'/plots', plotHandler),
          webapp2.Route(r'/imgSeg', imgSegHandler)]
app = webapp2.WSGIApplication(ROUTES, debug=True)
