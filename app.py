from flask import Flask, render_template, request, jsonify
from models import db, Patient, Report, Plan
from config import DATABASE_URL
from services.genai_service import generate_report
from services.agentic_service import generate_plan
import markdown

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db.init_app(app)

# ---------- Simple Logger ----------
def log(step):
    print(f"[STEP] {step}")

# ---------- DB Init ----------
with app.app_context():
    log("Initializing database...")
    db.create_all()
    log("Database ready")

# ---------- Routes ----------
@app.route("/")
def home():
    log("Home page loaded")
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    log("Dashboard opened")
    return render_template("dashboard.html")


@app.route("/generate", methods=["GET"])
def generate():
    log("Generate page opened")
    return render_template("generate.html", report=None, plan=None)


# ---------- Report First ----------
@app.route("/report", methods=["POST"])
def report_only():
    log("Generating medical report...")

    age = request.form["age"]
    gender = request.form["gender"]
    symptoms = request.form["symptoms"]

    report = generate_report(age, gender, symptoms)
    formatted_report = markdown.markdown(report)

    log("Medical report ready")
    return jsonify({"report": formatted_report})


# ---------- Plan After ----------
@app.route("/plan", methods=["POST"])
def plan_only():
    log("Generating treatment plan...")

    symptoms = request.form["symptoms"]

    plan = generate_plan(symptoms)
    formatted_plan = markdown.markdown(plan)

    log("Treatment plan ready")
    return jsonify({"plan": formatted_plan})


# ---------- Run App ----------
if __name__ == "__main__":
    log("Starting Flask app...")
    app.run(debug=True)