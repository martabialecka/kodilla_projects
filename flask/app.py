from flask import Flask

app = Flask(__name__)

@app.route('/dott')
def dott():
    my_name = "Kropka"
    my_text = "Have a nice day!"
    return f'Hello, {my_name} :) {my_text}'

@app.route('/blog')
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

@app.route('/message', methods=['POST'])
def post_message():
    return "OK OK OK"

@app.route('/message_ugly', methods=['GET'])
def message_form_ugly():
    text = """
        <html>
            <head></head>

            <body>
                <form action="" method="POST">
                    <label>First Name</label>
                    <input name="firstname"/>
                    <input type="submit"/>
                </form>
            </body>
        </html  >
    """
    return text

from flask import render_template
from flask import request, redirect

@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/greeting')
def greeting():
    print("We received GET")
    return render_template("greeting.html")

@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse.html", items=items, errors=errors)

