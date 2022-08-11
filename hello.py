from crypt import methods
import os
from threading import Timer
from flask import Flask, render_template, Response, request, redirect, url_for
import random
from dir import whattodo
import time


app = Flask(__name__)

my_value = 0
total_rounds=0

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

@app.route("/forward/", methods=['GET', 'POST'])
def move_forward():
        if request.method == 'POST':           
         global my_value
         my_value = request.form['quantity']
         print(my_value)
         
        if request.method == 'POST':           
            global total_rounds
            total_rounds = request.form['play']
            print(type(total_rounds))
            
        
    #Moving forward code
        return render_template('game.html')
count=0
@app.route("/play/", methods=['GET', 'POST'])
def play():
    
    
    global  count
    count += 1
    
    if int(count) == int(total_rounds)+1:
        count=0
        return redirect("http://127.0.0.1:5000/endgame/", code=302)
     
    #Moving forward code
    return render_template('game.html',rand=random.randint(1,int(my_value)),words=random.choice(whattodo),new=count,level=total_rounds)


@app.route("/endgame/", methods=['GET', 'POST'])
def end():
    return render_template('endGame.html')



     

    



    
     

    
    
     



     

