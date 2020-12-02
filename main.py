#Make sure you have installed pytube3 on your system.
from pytube import YouTube
from flask import Flask,request,render_template,json
import os
app = Flask(__name__)

def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads/Video')
    return download_path

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == "POST":
        # # ask for the link from user
        youtubeurl = request.form.get('youtubeurl') 
        try:
            youtubeurl = youtubeurl
            yt = YouTube(youtubeurl)

            #Showing details
            views =  yt.views,
            length = yt.length,
            rating = yt.rating,
            ys = yt.streams.get_highest_resolution()

            #Starting download
            print("Downloading...")
            ys.download(file_path())
            print("Download completed!!") 
            
            data = 'Download Complete!! Your video saved at : {}'.format(file_path())
            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            path = format(file_path())
            # return'' response
            return render_template('index.html',views=views,length=length,rating=rating, success= data,path=path)
           
        except:
            return render_template('index.html',error="Something went Wrong!!")
  
        # return render_template('index.html',views=views,length=length,rating=rating)
    else:
        return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True, port=5000)