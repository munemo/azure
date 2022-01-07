import os
from azure.storage.blob import BlobClient




from flask import Flask, render_template, request
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
 
@app.route('/',methods=['POST','GET'])
@app.route('/home' ,methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route('/upload', methods = ['POST'])
def upload():
    
        conn_string = "DefaultEndpointsProtocol=https;AccountName=lexicon;AccountKey=dr5mn8/DXPBKwP6NvtJO96vKJFEZpLiVFHLyE0/jPrfe9Pmlpp2NYoJeutVJECCjILvGyf2cWa9D9QQIeywxfQ==;EndpointSuffix=core.windows.net"

        blob_client = BlobClient.from_connection_string(conn_string,
           container_name="lexicon-container", blob_name="flask_test21.txt")

        with open("./flask_test21.txt", "rb") as data:
            blob_client.upload_blob(data)
        output = request.form.to_dict()
        name = output["name"]
       
        
        return render_template("result.html", name = name)


if __name__ == '__main__':
    app.run()