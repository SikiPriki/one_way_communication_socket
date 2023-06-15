#pip install Flask Flask-SocketIO 
#https://www.youtube.com/watch?v=mkXdvs8H7TA&ab_channel=TechWithTim


from flask import Flask, render_template
from flask_socketio import  SocketIO



app=Flask(__name__)
#app.config["SECRET_KEY"]="sdjkfalksd223sdas"
socketio=SocketIO(app)



@app.route('/button',methods=["POST","GET"])
def button():
    return render_template("button.html")


#on event message
@socketio.on("message")
def message(data):
    print('message received with ', data)
    #sends data
    socketio.send(data["data"])
    
    
@app.route("/") #methods=["GET","POST"])
def home():
    return render_template('home.html')


if __name__=='__main__':
    socketio.run(app,debug=True)