from crypt import methods
from flask import Flask, render_template, Response, request, redirect, url_for
import random
from dir import whattodo

app = Flask(__name__)
my_value = 0
@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route("/forward/", methods=['GET', 'POST'])
def move_forward():
        if request.method == 'POST':           
         global my_value
         my_value = request.form['quantity']
         print(my_value)
    #Moving forward code
        return render_template('game.html')
count=0
@app.route("/play/", methods=['POST'])
def play():
    global  count
    print(count)
    count += 1
    
    if count == 20:
        count=0
        return redirect("http://127.0.0.1:5000/endgame/", code=302)
   
    #Moving forward code
    return render_template('game.html',rand=random.randint(1,int(my_value)),words=random.choice(whattodo),new=count)


@app.route("/endgame/", methods=['GET', 'POST'])
def end():
    return render_template('endGame.html')



   




    
     

    
    
     



     

