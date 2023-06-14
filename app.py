#pip install Flask Flask-SocketIO 
#https://www.youtube.com/watch?v=mkXdvs8H7TA&ab_channel=TechWithTim


from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app=Flask(__name__)
app.config["SECRET_KEY"]="sdjkfalksd223sdas"
socketio=SocketIO(app)

rooms={}
rooms={"messages":[]}
#generates a unique code


@app.route('/button',methods=["POST","GET"])
def button():
   # session.clear()
   # rooms={"messages":[]}
            
    return render_template("button.html")
   
#rooms={"messages":[]} 



@socketio.on("message")
def message(data):
    
    print('message received with ', data)
    #content="Hello Python"
    #content=data["data"]
   # print("Content: ", content)
    #socketio.send(content, to=home)
    #rooms["messages"].append(data["data"])
   # print(rooms)
    #socketio.emit(rooms["messages"]) #namespace=)
 #  socketio.send("SERVER HELLO")
    socketio.send(data["data"])
    
    
    

@app.route("/", methods=["GET","POST"])
def home():
    print("Home rooms: ",rooms["messages"])
    print("HOME PRINT: ", rooms)
    return render_template('home.html')#, messages=rooms["messages"])#, messages=rooms["messages"]) #messages is doing so that one can see the history, what has been previously writtwn


    #content={
    #    "message": "Hello world"#data["data"]
   # }
    #send(content)
    #rooms["messages"].append(content)
    #print(f"sadi:{data['data']}")


#socket will be activated in  the room
""" @socketio.on("connect")
def connect():
    print("Connected")
 """
if __name__=='__main__':
    socketio.run(app,debug=True)