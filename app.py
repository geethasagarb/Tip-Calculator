from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tips.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_cost = db.Column(db.Float, nullable=False)
    tip_percent = db.Column(db.Float, nullable=False)
    tip_amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/", methods=["GET", "POST"])
def index():
    tip = None
    history = []

    if request.method == "POST":
        dollars = float(request.form["dollars"].replace("$", ""))
        percent = float(request.form["percent"].replace("%", "")) / 100
        tip = round(dollars * percent, 2)

        # Save to DB
        new_tip = Tip(meal_cost=dollars, tip_percent=percent, tip_amount=tip)
        db.session.add(new_tip)
        db.session.commit()

    history = Tip.query.order_by(Tip.timestamp.desc()).limit(5).all()

    return render_template("index.html", tip=tip, history=history)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    with app.app_context():
        db.create_all()  # Ensure DB is created on first run
    app.run(host="0.0.0.0", port=port)