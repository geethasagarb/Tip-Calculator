import os
from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Set database location
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tips.db"
db = SQLAlchemy(app)

# Define the Tip model
class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_cost = db.Column(db.Float, nullable=False)
    tip_percent = db.Column(db.Float, nullable=False)
    tip_amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database and tables if not exist
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    tip = None
    if request.method == "POST":
        dollars = float(request.form["dollars"].replace("$", ""))
        percent = float(request.form["percent"].replace("%", "")) / 100
        tip = round(dollars * percent, 2)
        # Save to database
        new_tip = Tip(meal_cost=dollars, tip_percent=percent, tip_amount=tip)
        db.session.add(new_tip)
        db.session.commit()
    return render_template("index.html", tip=tip)

# Optional: Admin view to see all tips (just for testing)
@app.route("/admin")
def admin():
    records = Tip.query.order_by(Tip.timestamp.desc()).all()
    return "<br>".join([f"${t.meal_cost} @ {t.tip_percent*100:.1f}% = ${t.tip_amount}" for t in records])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)