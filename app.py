from flask import Flask, render_template, request
from model.model import classify_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        email = request.form.get("email")
        result = classify_email(email)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
