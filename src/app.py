from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route('/set_counter', methods=['POST'])
def set_counter():
    value = request.form['value'] 
    cnt.set_value(int(value))
    return redirect("/")

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)
