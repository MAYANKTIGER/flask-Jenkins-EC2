## flask app for hello world

from flask import Flask
import os

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "CI-CD pipeline is running successfully.......!!!!!"

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
    
