from flask import Flask, redirect, url_for,render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

# Configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "rakam"

mysql = MySQL(app)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def login():
    return render_template("login.html")

@app.route("/rakam",methods=["POST","GET"])  # this sets the route to this page
def rakam():
    if request.method == 'POST':
        #fetch form data
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        resultVAlue = cur.execute(f'SELECT * FROM login where username = "{username}" AND password = "{password}" ')
        print(resultVAlue)
        if resultVAlue > 0:
            mysql.connection.commit()
            cur.close()
            return redirect("rakam")
        else:
            return redirect("/") 
    return render_template("rakam.html")

if __name__ == "__main__":
    app.run(debug=True)

