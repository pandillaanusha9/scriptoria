from flask import Flask, render_template, request, send_file
from services.automation import generate_full_plan
from utils.pdf_generator import create_pdf

app = Flask(__name__)

generated_data = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    title = request.form["title"]
    genre = request.form["genre"]
    idea = request.form["idea"]

    result = generate_full_plan(title, genre, idea)

    global generated_data
    generated_data = result

    return render_template("result.html", data=result)

@app.route("/export")
def export():
    filepath = create_pdf(generated_data)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)