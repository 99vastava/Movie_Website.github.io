from flask import Flask, render_template, request
import json
import urllib.request as req
from flask_mail import Mail, Message
import ssl

app= Flask(__name__)

api_key= "4e44d9029b1270a757cddc766a1bcb63"
base_url= "https://api.themoviedb.org/3/discover/movie?api_key="+api_key

app.config['Mail_Server']= 'smtp.gmail.com'
app.config['Mail_Port']= '465'
app.config['Mail_Username']= 'srivastavasrishti333@gmail.com'
app.config['Mail_Password']= 'Srishti@official'
app.config['Mail_Use_TLS']= 'False'
app.config['Mail_Use_SSL']= 'True'

mail= Mail(app)


@app.route("/")
def index():

    conn= req.urlopen(base_url)
    json_data=json.loads(conn.read())
    print(json_data)
    return render_template("index.html", data=json_data["results"])

@app.route("/send_message", methods =['GET', 'POST'])
def send_message():
    if request.method == "POST":
        conn= req.urlopen(base_url)
        json_data=json.loads(conn.read())
        movie_data=json_data["results"]
        email= request.form['email']
        message = Message(subject="Movie detail", sender="srivastavasrishti333@gmail.com", recipients=['email'])
        
        message.body= json_data["results"]
  
        mail.send(message)
        success = "Mail sent"

        return render_template("sent.html", success=success)


if __name__=="__main__":
    app.run(debug=True)
  