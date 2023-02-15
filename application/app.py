from collections import namedtuple
from flask import Flask, request, render_template
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

User = namedtuple("User", field_names=["username", "password"])
user = User(username="john", password="black")

@app.route("/login/", methods=["GET", "POST"])
def login():
   form = LoginForm()
   if request.method == "POST":
       if (
           form.username.data == user.username and
           form.password.data == user.password
       ):
           return "You are logged id"
       else:
           return "Wrong credentials!!"
   return render_template("login.html", form=form)


if __name__ == "__main__":
   app.run(debug=False)