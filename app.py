from flask import Flask, render_template, request, url_for
import mysql.connector
from werkzeug.utils import redirect

app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pavanait404",
    database="logisticcompany"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/UserData',methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    sql = "INSERT INTO tmsregister(name,email,password) VALUES (%s,%s,%s)"
    values = (name,email,password)
    cursor.execute(sql,values)
    db.commit()

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template(('success.html'))

if __name__ == '__main__':
    app.run(debug = True)


