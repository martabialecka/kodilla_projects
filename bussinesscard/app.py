from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/me')
def about_me():
    return render_template("me.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       return render_template('contact.html')
   elif request.method == 'POST':
       print(f"User sent a message '{request.form['message']}'")
       return redirect("/contact")
