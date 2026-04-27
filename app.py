from flask import Flask, render_template, request
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


@app.route("/generate", methods=["GET", "POST"])
def generate():
    log("Generate route accessed")

    if request.method == "POST":
        log("Form submitted")

        age = request.form["age"]
        gender = request.form["gender"]
        symptoms = request.form["symptoms"]

        # ---- GenAI ----
        log("Generating medical report (GenAI)...")
        report = generate_report(age, gender, symptoms)
        log("Medical report generated")

        # ---- Agentic AI ----
        log("Running Agentic AI...")
        plan = generate_plan(symptoms + " " + report)
        log("Treatment plan generated")

        # ---- Format Markdown ----
        log("Formatting output...")
        formatted_report = markdown.markdown(report)
        formatted_plan = markdown.markdown(plan)

        log("Sending response to UI")

        return render_template(
            "generate.html",
            report=formatted_report,
            plan=formatted_plan
        )

    # GET request
    return render_template("generate.html", report=None, plan=None)


# ---------- Run App ----------
if __name__ == "__main__":
    log("Starting Flask app...")
    app.run(debug=True)