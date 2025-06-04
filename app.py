from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tip = None
    if request.method == "POST":
        dollars = float(request.form["dollars"].replace("$", ""))
        percent = float(request.form["percent"].replace("%", "")) / 100
        tip = round(dollars * percent, 2)
    return render_template("index.html", tip=tip)

if __name__ == "__main__":
    app.run(debug=True)