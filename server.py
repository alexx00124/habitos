from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/habitos")
def habitos():
    return render_template("habitos.html")



if __name__ == "__main__":
    app.run(debug=True)
