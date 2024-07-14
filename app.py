from flask import Flask, render_template

app = Flask(__name__)

from database import query_db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/customers/<int:customer_id>/greet")
def greet(customer_id: int):

    customer = query_db(
        'SELECT * FROM customer_accounts WHERE id = ?', 
        [customer_id],
        single_result=True)

    return render_template("account.html", user_name=customer['name'])
