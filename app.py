from flask import Flask,render_template,request
from db import get_connection

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        salary=request.form["salary"]

        cursor.execute(
            "INSERT INTO employee (name,salary) VALUES (%s,%s)",
            (name,salary)
        )
        
        conn.commit()

    cursor.execute("SELECT * FROM employee")
    employee = cursor.fetchall()

    conn.close()

    return render_template("index.html", employee=employee)

 

if __name__ == "__main__":

    app.run(debug=True)