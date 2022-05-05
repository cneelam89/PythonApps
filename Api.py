from flask import Flask, jsonify
from flask.globals import request

app = Flask(__name__)  #instance

tasks = [
    {"id": 1,"title": "Buy Groceries", "description": "Milk, eggs, cheese, pizza, fruit", "done": False,},
    {"id": 2, "title": "Learn python", "description": "Neelam will help ", "done": True},
]


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route("/homepage", methods=["GET"])
def homepage():
    return "<HTML> <body bgcolor=Blue><h1><marquee>Welcome to My Website</marquee>"


@app.route("/mail")
def get_mail():
    return "<html><body><marquee><h1>Welcome to Gmail</h1></marquee></body></html>"


@app.route("/pythonhome")
def pythonhome():
    myfile = open("Shop.html")
    data = myfile.read()
    return data


@app.route("/uber", methods=["GET"])
def fb():
    return {
        "driver": "Rajendra",
        "OTP": "6969",
        "ETA": "10 Mins",
        "Vehicle": ["MH-01", 9999],
    }


@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user", "khula")
    pwd = request.form.get("pwd", "saand")
    if user == "khula" and pwd == "saand":
        return "Kundi mat khadkao raja, seedha andar aao raja"
    else:
        return "Tel lene jaa"


if __name__ == "__main__":
    app.run(debug=True, port=8080)

